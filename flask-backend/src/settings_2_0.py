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

import api_v2
import handler_api
import monaco_cli_download
import settings_2_0_schemas


def extract_function(config, use_cache, cache_only, analysis_object, input_params=None, run_info=None):

    use_monaco_cache = monaco_cli_download.is_finished_configs(config=config)
    schema_dict = None
    
    if (cache_only == True and use_monaco_cache == False):
        schema_dict = settings_2_0_schemas.extract_schemas(
            config, use_cache=cache_only, cache_only=cache_only)

        _ = extract_configs(
            schema_id_query_dict_extractor, config, schema_dict, use_cache, cache_only, analysis_object)
        
    else:
        if (cache_only):
            pass #return monaco_local_entity.analyze_configs(config, analysis_object)
        else:
            monaco_cli_download.extract_configs(
                run_info, config['tenant_key'])

    return schema_dict


def extract_specific_scope(config, use_cache, cache_only, analysis_object, scope, run_info=None):

    scope_array = []

    scope_array = add_scope_to_extract(scope, scope_array, run_info)
    scope_array = add_scope_to_extract('environment', scope_array, run_info)

    scope_dict = {"items": []}

    for input_scope in scope_array:
        scope_dict["items"].append({"scope": input_scope})

    _ = extract_configs(
        scope_query_dict_extractor, config, scope_dict, use_cache, cache_only, analysis_object)

    return scope_dict


def add_scope_to_extract(scope, scope_array, run_info):

    if (scope == 'environment'):
        if (run_info is None):
            pass
        elif (run_info['use_environment_cache'] == True):
            return scope_array

    if (scope in scope_array):
        pass
    else:
        scope_array.append(scope)

    return scope_array


def extract_configs(item_id_extractor, config, input_dict, use_cache, cache_only, analysis_object=None):

    handler_api.extract_pages_from_input_list(
        config, input_dict['items'],
        'objects', api_v2.settings_objects, item_id_extractor,
        use_cache, cache_only, analysis_object)

    return None


def schema_id_query_dict_extractor(item):

    item_id = item['schemaId']

    query_dict = {}
    query_dict['schemaIds'] = item_id
    query_dict['fields'] = "objectId,scope,schemaId,value,schemaVersion"

    url_trail = None

    return item_id, query_dict, url_trail


def scope_query_dict_extractor(item):

    scope = item['scope']

    query_dict = {}
    query_dict['scopes'] = scope
    query_dict['fields'] = "objectId,scope,schemaId,value,schemaVersion"

    url_trail = None

    return scope, query_dict, url_trail
