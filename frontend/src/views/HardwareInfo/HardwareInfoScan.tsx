import React from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import routes from 'routes';
import VulnerabilityTemplate from 'templates/VulnerabilityTemplate';
import Scan from 'components/molecules/Scan/Scan';
import { fetchHardwareInfo } from '../../actions/hardwareInfoActions';

const HardwareInfoScan = () => {
  const dispatch = useDispatch();
  const history = useHistory();

  const handleButtonClick = () => {
    dispatch(fetchHardwareInfo());
    history.push(routes.hardwareInfoResults);
  };

  return (
    <VulnerabilityTemplate>
      <Scan title="Check your hardware" onButtonClick={handleButtonClick} />
    </VulnerabilityTemplate>
  );
};

export default HardwareInfoScan;
