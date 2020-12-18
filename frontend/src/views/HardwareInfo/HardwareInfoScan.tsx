import React from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import routes, { routesWithoutTab } from 'routes';
import VulnerabilityTemplate from 'templates/VulnerabilityTemplate';
import Scan from 'components/molecules/Scan/Scan';
import { useParams } from 'react-router';
import { fetchHardwareInfo } from 'actions/hardwareInfoActions';
import { updateTabUrl } from 'actions/TabsActions';

const HardwareInfoScan = () => {
  const dispatch = useDispatch();
  const { page } = useParams();
  const history = useHistory();

  const handleButtonClick = () => {
    dispatch(fetchHardwareInfo(page));
    dispatch(updateTabUrl(routesWithoutTab.hardwareInfoResults, page));
    history.push(
      `${routes.tabsWOpage}${page}${routesWithoutTab.hardwareInfoResults}`,
    );
  };

  return (
    <VulnerabilityTemplate>
      <Scan title="Check your hardware" onButtonClick={handleButtonClick} />
    </VulnerabilityTemplate>
  );
};

export default HardwareInfoScan;
