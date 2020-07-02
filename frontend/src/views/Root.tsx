import React, { lazy, Suspense } from 'react';
import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom';
import { ThemeProvider } from 'styled-components';
import { Provider } from 'react-redux';
import store from 'store';
import routes from 'routes';
import theme from 'theme/theme';
import GlobalStyle from 'theme/GlobalStyle';
import MainTemplate from 'templates/MainTemplate';
import FrontendVulnerabilitySearch from 'views/FrontendVulnerabilitySearch';
import BackendVulnerabilitySearch from 'views/BackendVulnerabilitySearch';
import CveSearch from 'views/CveSearch';
import RegistryScan from 'views/RegistryScan/RegistryScan';
import Loading from 'components/atoms/LoadingAnimation/LoadingAnimation';

const FrontendVulnerabilityResult = lazy(() =>
  import('views/FrontendVulnerabilityResult'),
);
const BackendVulnerabilityResult = lazy(() =>
  import('views/BackendVulnerabilityResult'),
);
const CveSearchResult = lazy(() => import('views/CveSearchResult'));
const RegistryScanResult = lazy(() =>
  import('views/RegistryScan/RegistryScanResults'),
);
const ExploitsSearchView = lazy(() =>
  import('views/ExploitSearch/ExploitSearchView'),
);
const ExploitsResultView = lazy(() =>
  import('views/ExploitSearch/ExploitResultView'),
);
const SettingsView = lazy(() => import('views/Settings/SettingsView'));
const DocsView = lazy(() => import('views/DocsView/DocsView'));

function Root() {
  return (
    <Provider store={store}>
      <BrowserRouter>
        <ThemeProvider theme={theme}>
          <GlobalStyle />
          <MainTemplate>
            <Suspense fallback={<Loading bigView />}>
              <Switch>
                <Route
                  exact
                  path={routes.home}
                  render={() => <Redirect to={routes.frontend} />}
                />
                <Route
                  exact
                  path={routes.frontend}
                  component={FrontendVulnerabilitySearch}
                />
                <Route
                  exact
                  path={routes.frontendResults}
                  component={FrontendVulnerabilityResult}
                />
                <Route
                  exact
                  path={routes.backend}
                  component={BackendVulnerabilitySearch}
                />
                <Route
                  exact
                  path={routes.backendResults}
                  component={BackendVulnerabilityResult}
                />
                <Route exact path={routes.cveSearch} component={CveSearch} />
                <Route
                  exact
                  path={routes.cveSearchResults}
                  component={CveSearchResult}
                />
                <Route exact path={routes.registry} component={RegistryScan} />
                <Route
                  exact
                  path={routes.registryResults}
                  component={RegistryScanResult}
                />
                <Route
                  exact
                  path={routes.exploits}
                  component={ExploitsSearchView}
                />
                <Route
                  exact
                  path={routes.exploitResults}
                  component={ExploitsResultView}
                />
                <Route exact path={routes.documentation} component={DocsView} />
                <Route exact path={routes.settings} component={SettingsView} />
              </Switch>
            </Suspense>
          </MainTemplate>
        </ThemeProvider>
      </BrowserRouter>
    </Provider>
  );
}

export default Root;
