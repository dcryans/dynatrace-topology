/*
Copyright 2023 Dynatrace LLC

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License.
*/

import { Typography } from '@mui/material';
import * as React from 'react';
import { TENANT_KEY_TYPE_MAIN, useTenant, useTenantKey } from '../context/TenantListContext';
import { DEFAULT_MONACO_CONCURRENT_REQUESTS } from '../credentials/TenantConfig';


export default function MonacoRequestsInfo({ tenantType = TENANT_KEY_TYPE_MAIN }) {

    const { tenantKey } = useTenantKey(tenantType)
    const { tenant } = useTenant(tenantKey)

    return (
        <React.Fragment>
            <Typography>The Monaco extraction will send {tenant.monacoConcurrentRequests?tenant.monacoConcurrentRequests:DEFAULT_MONACO_CONCURRENT_REQUESTS} concurrent requests.</Typography>
            <Typography>If the extraction fails, it could be caused by rate limiting.</Typography>
            <Typography>You can reduce the number of concurrent requests 'per tenant' in the Credentials tab.</Typography>
        </React.Fragment>
    );
}
