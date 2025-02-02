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

import * as React from 'react';
import CredentialPanel from '../credentials/CredentialPanel';
import DocumPanel from '../docum/DocumPanel';
import ExtractionPanel from '../extraction/ExtractionPanel';
import MatchPanel from '../match/MatchPanel';
import Setting from '../setting/Setting';
import MigratePanel from '../migrate/MigratePanel';
import TabPanelBar, { genTabConfig } from './TabPanelBar';
import HistoryPanel from '../history/HistoryPanel';


const tabConfig = [
  genTabConfig("Credentials", <CredentialPanel />),
  genTabConfig("Extract", <ExtractionPanel />),
  //genTabConfig("Match", <MatchPanel />),
  genTabConfig("Manage Configs", <MigratePanel />),
  genTabConfig("History", <HistoryPanel />),
  //genTabConfig("Settings", <Setting />),
  genTabConfig("Documentation", <DocumPanel />),
]

export default function TabPanelMain() {
  return (
    <TabPanelBar tabConfig={tabConfig} />
  )
}
