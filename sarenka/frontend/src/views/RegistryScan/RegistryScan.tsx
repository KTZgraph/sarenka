import React from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import routes, { routesWithoutTab } from 'routes';
import { fetchInstalledPrograms } from 'actions/registryScanActions';
import VulnerabilityTemplate from 'templates/VulnerabilityTemplate';
import Scan from 'components/molecules/Scan/Scan';
import { useParams } from 'react-router';
import { updateTabUrl } from 'actions/TabsActions';

const RegistryScan = () => {
  const dispatch = useDispatch();
  const { page } = useParams();
  const history = useHistory();

  const handleButtonClick = () => {
    dispatch(fetchInstalledPrograms(page));
    dispatch(updateTabUrl(routesWithoutTab.registryResults, page));
    history.push(
      `${routes.tabsWOpage}${page}${routesWithoutTab.registryResults}`,
    );
  };

  return (
    <VulnerabilityTemplate>
      <Scan title="Check your desktop apps" onButtonClick={handleButtonClick} />
    </VulnerabilityTemplate>
  );
};

export default RegistryScan;
