const tabRoute = '/tabs/:page';
const serverIp = `http://localhost:8000`;

export const routesWithoutTab: Record<string, string> = {
  frontend: '/frontend',
  frontendResults: '/frontend/results',
  backend: '/backend',
  backendResults: '/backend/results',
  exploits: `/exploits`,
  exploitResults: '/exploits/results',
  registry: '/registry',
  registryResults: '/registry/results',
  documentation: '/docs',
  settings: '/settings',
  cveSearch: '/cvesearch',
  cveSearchResults: '/cvesearch/results',
  remoteHostInfo: '/remotehostinfo',
  remoteHostInfoResult: '/remotehostinfo/results',
  hardwareInfo: '/hardwareinfo',
  hardwareInfoResults: '/hardwareinfo/results',
};

const routes: Record<string, string> = {
  home: '/',
  homeRedirect: `/tabs/0${routesWithoutTab.remoteHostInfo}`,
  tabsWOpage: '/tabs/',
  tab: `${tabRoute}`,
  frontend: `${tabRoute}${routesWithoutTab.frontend}`,
  frontendResults: `${tabRoute}${routesWithoutTab.frontendResults}`,
  backend: `${tabRoute}${routesWithoutTab.backend}`,
  backendResults: `${tabRoute}${routesWithoutTab.backendResults}`,
  exploits: `${tabRoute}${routesWithoutTab.exploits}`,
  exploitResults: `${tabRoute}${routesWithoutTab.exploitResults}`,
  registry: `${tabRoute}${routesWithoutTab.registry}`,
  registryResults: `${tabRoute}${routesWithoutTab.registryResults}`,
  documentation: `${tabRoute}${routesWithoutTab.documentation}`,
  settings: `${tabRoute}${routesWithoutTab.settings}`,
  cveSearch: `${tabRoute}${routesWithoutTab.cveSearch}`,
  cveSearchResults: `${tabRoute}${routesWithoutTab.cveSearchResults}`,
  remoteHostInfo: `${tabRoute}${routesWithoutTab.remoteHostInfo}`,
  remoteHostInfoResult: `${tabRoute}${routesWithoutTab.remoteHostInfoResult}`,
  hardwareInfo: `${tabRoute}${routesWithoutTab.hardwareInfo}`,
  hardwareInfoResults: `${tabRoute}${routesWithoutTab.hardwareInfoResults}`,
};

export const serverRoutes: Record<string, string> = {
  remoteHostData: `${serverIp}/api/censys/`,
  remoteHostReport: `${serverIp}/reports/host_info/`,
  registryScanData: `${serverIp}/api/local/registry`,
  hardwareInfoData: `${serverIp}/api/local/hardware`,
  hardwareInfoReport: `${serverIp}/reports/hardware_info`,
  cveSearchData: `${serverIp}/vulns/cve/`,
  cweSearchData: `${serverIp}/vulns/cwe/`,
  userCredentials: `${serverIp}/api/user_credentials`,
};

export const documentationRoutes: Record<string, string> = {
  apiDocumentation: `${serverIp}/api`,
};

export default routes;
