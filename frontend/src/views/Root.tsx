import React from 'react';
import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom';
import { ThemeProvider } from 'styled-components';
import routes from 'routes';
import theme from 'theme/theme';
import GlobalStyle from 'theme/GlobalStyle';
import MainTemplate from 'templates/MainTemplate';
import FrontendVulnerabilitySearch from 'views/FrontendVulnerabilitySearch';
import FrontendVulnerabilityResult from 'views/FrontendVulnerabilityResult';
import BackendVulnerabilitySearch from 'views/BackendVulnerabilitySearch';
import BackendVulnerabilityResult from 'views/BackendVulnerabilityResult';

function Root() {
  return (
    <BrowserRouter>
      <ThemeProvider theme={theme}>
        <GlobalStyle />
        <MainTemplate>
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
          </Switch>
        </MainTemplate>
      </ThemeProvider>
    </BrowserRouter>
  );
}

export default Root;
