import React, { useEffect } from 'react';
import { useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import routes from 'routes';
import { Helmet } from 'react-helmet-async';

const HomeView = () => {
  const history = useHistory();
  const page = window.location.href.split('/')[4];
  const tab = useSelector(({ tabs }: Record<string, any>) =>
    tabs[page] ? tabs[page] : tabs[Object.keys(tabs)[0]],
  );

  useEffect(() => {
    if (page !== tab.index) {
      history.push(`${routes.tabsWOpage}${tab.index}${tab.link}`);
    }
  }, [history, page, tab.index, tab.link]);

  return (
    <Helmet>
      <title>Sarenka</title>
      <link
        id="favicon"
        rel="icon"
        href="/frontend/src/static/favicon/favicon.ico"
        type="image/x-icon"
      />
    </Helmet>
  );
};

export default HomeView;
