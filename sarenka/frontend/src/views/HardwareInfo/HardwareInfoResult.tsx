import React from 'react';
import { useSelector } from 'react-redux';
import ResultTemplate from 'templates/VulnerabilityResultTemplate';
import Loading from 'components/atoms/LoadingAnimation/LoadingAnimation';
import logo from 'static/logo.svg';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';
import ListWrapper from 'components/atoms/List/ListWrapper';
import ListItem from 'components/atoms/List/ListItem';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import NoData from 'components/atoms/NoDataText/NoDataText';
import { useParams } from 'react-router';

const HardwareInfoResults = () => {
  const { page } = useParams();
  const { isLoading, data } = useSelector(
    ({ hardwareInfo }: Record<string, any>) => hardwareInfo[page],
  );

  return (
    <ResultTemplate
      search={<img src={logo} alt="App logo." />}
      result={
        isLoading ? (
          <Loading />
        ) : (
          <CardWrapper>
            <div>
              <Paragraph listTitle>BIOS version</Paragraph>
              <ListWrapper>
                <ListItem>
                  {`Name: `}
                  {data.bios?.name || <NoData />}
                </ListItem>
                <ListItem>
                  {`Version: `}
                  {data.bios?.version || <NoData />}
                </ListItem>
              </ListWrapper>
            </div>
            <div>
              <Paragraph listTitle>Computer info</Paragraph>
              <ListWrapper>
                <ListItem>
                  {`Name: `}
                  {data.computer_name?.name || <NoData />}
                </ListItem>
                <ListItem>
                  {`Architecture: `}
                  {data.computer_name?.system_type || <NoData />}
                </ListItem>
              </ListWrapper>
            </div>
          </CardWrapper>
        )
      }
    />
  );
};

export default HardwareInfoResults;
