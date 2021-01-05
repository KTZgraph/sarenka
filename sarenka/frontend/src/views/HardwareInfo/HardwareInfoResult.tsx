import React from 'react';
import { useSelector } from 'react-redux';
import ResultTemplate from 'templates/VulnerabilityResultTemplate';
import Loading from 'components/atoms/LoadingAnimation/LoadingAnimation';
import logo from 'static/logo.svg';
import { useParams } from 'react-router';
import HardwareInfoCard from 'components/organisms/HardwareInfoCard/HardwareInfoCard';

const HardwareInfoResults: React.FC = () => {
  const { page } = useParams();
  const { isLoading, data } = useSelector(
    ({ hardwareInfo }: Record<string, any>) => hardwareInfo[page],
  );

  return (
    <ResultTemplate
      search={<img src={logo} alt="App logo." />}
      result={isLoading ? <Loading /> : <HardwareInfoCard data={data} />}
    />
  );
};

export default HardwareInfoResults;
