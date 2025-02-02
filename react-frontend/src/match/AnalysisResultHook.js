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

import * as React from 'react'
import _ from 'lodash';
import ResultTreeGroup from '../result/ResultTreeGroup';
import { useTenantKey } from '../context/TenantListContext';
import { ALPHABETIC } from '../options/SortOrderOption';
import ResultDrawer from '../result/ResultDrawer';

export const useAnalysisResult = () => {

    const { tenantKey } = useTenantKey()
    const [analysisResult, setAnalysisResult] = React.useState(undefined)
    const [initialFilterText, setInitialFilterText] = React.useState("")
    const [openDrawer, setOpenDrawer] = React.useState(false);

    React.useMemo(() => {
        setAnalysisResult(undefined)
        setOpenDrawer(false)
    }, [tenantKey])

    const hasAnalysisResult = React.useMemo(() => {
        setOpenDrawer(false)
        return !_.isEmpty(analysisResult)
    }, [analysisResult])

    return { tenantKey, initialFilterText, analysisResult, hasAnalysisResult, openDrawer, setAnalysisResult, setInitialFilterText, setOpenDrawer }
}

export const useTreeResult = (defaultSortOrder = ALPHABETIC) => {
    
    const { tenantKey, initialFilterText, analysisResult, hasAnalysisResult, openDrawer, setAnalysisResult, setInitialFilterText, setOpenDrawer } = useAnalysisResult()

    const treeComponent = React.useMemo(() => {
        setOpenDrawer(false)
        if (!_.isEmpty(analysisResult)) {
            return (
                <ResultTreeGroup data={analysisResult} defaultSortOrder={defaultSortOrder} initialFilterText={initialFilterText} setOpenDrawer={setOpenDrawer} />
            )
        }
        return null
    }, [analysisResult])

    const analysisResultComponent = React.useMemo(() => {
        if (!_.isEmpty(analysisResult)) {
            return (
                <ResultDrawer openDrawer={openDrawer} setOpenDrawer={setOpenDrawer}>
                    {treeComponent}
                </ResultDrawer>
            )
        }
        return null
    }, [treeComponent, openDrawer])

    return { tenantKey, hasAnalysisResult, setAnalysisResult, analysisResultComponent, setInitialFilterText }
}
