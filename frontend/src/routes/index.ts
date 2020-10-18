const tabRoute = '/tabs/:page';

export const routesWithoutTab = {
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

export default routes;
