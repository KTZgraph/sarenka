import React from 'react';
import { useSelector } from 'react-redux';
import ResultTemplate from 'templates/VulnerabilityResultTemplate';
import Loading from 'components/atoms/LoadingAnimation/LoadingAnimation';
import logo from 'static/logo.svg';
import { useParams } from 'react-router';
import HardwareInfoCard from 'components/organisms/HardwareInfoCard/HardwareInfoCard';
import Button, { ButtonAlignToRight } from 'components/atoms/Button/Button';
import { fetchReport } from 'actions/hardwareInfoActions';

const HardwareInfoResults: React.FC = () => {
  const { page } = useParams();
  const { isLoading, data } = useSelector(
    ({ hardwareInfo }: Record<string, any>) => hardwareInfo[page],
  );

  const handleReportGenerate = () => {
    return fetchReport();
  };

  return (
    <ResultTemplate
      search={<img src={logo} alt="App logo." />}
      result={
        isLoading ? (
          <Loading />
        ) : (
          <>
            <ButtonAlignToRight>
              <Button onClick={handleReportGenerate} small>
                Generate report
              </Button>
            </ButtonAlignToRight>
            <HardwareInfoCard data={data} />
          </>
        )
      }
    />
  );
};

export default HardwareInfoResults;
