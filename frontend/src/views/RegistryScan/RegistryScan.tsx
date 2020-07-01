import React from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import routes from 'routes';
import { fetchInstalledPrograms } from 'actions/registryScanActions';
import VulnerabilityTemplate from 'templates/VulnerabilityTemplate';
import Scan from 'components/molecules/Scan/Scan';

const RegistryScan = () => {
  const dispatch = useDispatch();
  const history = useHistory();

  const handleButtonClick = () => {
    dispatch(fetchInstalledPrograms());
    history.push(routes.registryResults);
  };

  return (
    <VulnerabilityTemplate>
      <Scan title="Check your desktop apps" onButtonClick={handleButtonClick} />
    </VulnerabilityTemplate>
  );
};

export default RegistryScan;
