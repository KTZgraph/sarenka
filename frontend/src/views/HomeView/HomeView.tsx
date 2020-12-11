import React, { useEffect } from 'react';
import { useParams } from 'react-router';
import { useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import routes from 'routes';

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

  return null;
};

export default HomeView;
