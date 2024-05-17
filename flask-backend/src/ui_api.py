# Copyright 2023 Dynatrace LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#      https://www.apache.org/licenses/LICENSE-2.0

#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import requests
import json
import time

# SERVICE
entity_details = "rest/configuration/deployment/entities"
# Add: /SERVICE/SERVICE-97A55F7A43425D84

# Get Hosts
get_hosts = "rest/hosts/new"
# Add: ?gtf=l_2_HOURS&gf=all

# Get Entities
get_entities = "rest/v2/entities"
# Add: /HOST-41EE93B4CEAFF254?fields=%2Bproperties&from=1697213166016&to=1697220366016

# Get Process Group
get_pg = "rest/processes/processGroups"
# Add: /PROCESS_GROUP-74500348BA882E1A?timeframe=last2h&gtf=l_2_HOURS

# Get Service
get_service = "rest/services"
# Add: /SERVICE-ABFA0853391003A6?demo=none&loadPgis=true&timeframe=last2h&gtf=l_2_HOURS

# Get Backtrace
get_backtrace = "rest/serviceanalysis/servicebacktrace"
# Add: ?serviceId=SERVICE-ABFA0853391003A6&sci=SERVICE-ABFA0853391003A6&timeframe=custom1697247287834to1697254487834&gtf=l_2_HOURS


def get_wait(config, api, url_trail, payload=None, method="GET"):
    response = get(config, api, url_trail, payload, method)

    url_trail_wait = ""
    working = True
    wait_token = "&prgtkn="
    try:
        while working:
            try:
                response_object = json.loads(response.text)
            except RecursionError as error:
                print(response.text)
                print(url_trail, url_trail_wait)
                print(error)
                return None
            if (
                "progressValue" in response_object
                and response_object["progressValue"] < 100
            ):
                url_trail_wait = url_trail + wait_token + response_object["token"]
                if(response_object["progressValue"] < 50):
                    time.sleep(1)
                response = get(config, api, url_trail_wait, payload, method)
                continue
            break
    except Exception as error:
        print(response.text)
        print(url_trail, url_trail_wait)
        raise error
    
    return response


def get(config, api, url_trail, payload=None, method="GET"):
    call_url = config["url"] + api + url_trail

    response = requests.request(
        method,
        call_url,
        headers=config["headers"],
        verify=config["verifySSL"],
        proxies=config["proxies"],
        data=payload,
    )
    if response.status_code == 404:
        pass
    else:
        response.raise_for_status()

    return response


def _post_put(config, api, url_trail, payload, method):
    call_url = config["url"] + api + url_trail

    response = requests.request(
        method,
        call_url,
        headers=config["headers"],
        data=payload,
        verify=config["verifySSL"],
        proxies=config["proxies"],
    )

    if response.status_code == 404:
        pass
    else:
        response.raise_for_status()

    return response


def post(config, api, url_trail, payload):
    return _post_put(config, api, url_trail, payload, "POST")


def put(config, api, url_trail, payload):
    return _post_put(config, api, url_trail, payload, "PUT")


def get_json(config, api, url_trail):
    response = get(config, api, url_trail)
    response_object = json.loads(response.text)

    return response_object


def post_json(config, api, url_trail, payload):
    response = post(config, api, url_trail, payload)
    response_object = json.loads(response.text)

    return response_object
