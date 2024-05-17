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

from flask import Flask, request, Blueprint
from flask_cors import cross_origin
import json

import flask_utils
import topology
import response_utils

blueprint_route_topology = Blueprint("blueprint_route_topology", __name__)


@blueprint_route_topology.route("/extract_topology", methods=["POST"])
@cross_origin(origin="*")
def extract_topology():
    tenant_key = flask_utils.get_arg("tenant_key", "0")

    def call_process():
        topology_list = topology.extract_topology(tenant_key)
        return topology_list

    return response_utils.call_and_get_response(call_process)


"""
@blueprint_route_topology.route('/topology_list', methods=['POST'])
@cross_origin(origin='*')
def topology_list_post():
    payload = json.loads(request.data.decode("utf-8"))

    def call_process():
        topology.save_topology_list(payload)
        return payload

    return response_utils.call_and_get_response(call_process)
"""
