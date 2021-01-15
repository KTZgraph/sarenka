import React from 'react';
import styled from 'styled-components';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import ListWrapper from 'components/atoms/List/ListWrapper';
import ListItem from 'components/atoms/List/ListItem';
import NoData from 'components/atoms/NoDataText/NoDataText';
import HardwareInfoData from 'interfaces/HardwareInfoData';

const StyledCardWrapper = styled(CardWrapper)`
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-gap: 20px;
  justify-content: center;

  @media (max-width: 2100px) {
    grid-template-columns: repeat(4, 1fr);
  }
  @media (max-width: 1800px) {
    grid-template-columns: repeat(3, 1fr);
  }
  @media (max-width: 1460px) {
    grid-template-columns: repeat(2, 1fr);
  }
  @media (max-width: 800px) {
    grid-template-columns: repeat(1, 1fr);
  }
`;

const StyledColumnWrapper = styled.div``;

type Props = {
  data: HardwareInfoData;
};

const HardwareInfoCard: React.FC<Props> = ({ data }: Props) => (
  <StyledCardWrapper>
    <StyledColumnWrapper>
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
    </StyledColumnWrapper>
    <StyledColumnWrapper>
      <Paragraph listTitle>Computer info</Paragraph>
      <ListWrapper>
        <ListItem>
          {`Name: `}
          {data.computer_information?.name || <NoData />}
        </ListItem>
        <ListItem>
          {`Serial number: `}
          {data.computer_information?.computer_serial_number || <NoData />}
        </ListItem>
        <ListItem>
          {`MAC Address: `}
          {data.computer_information?.mac_address || <NoData />}
        </ListItem>
        <ListItem>
          {`Total physical memory: `}
          {data.computer_information?.total_physical_memory || <NoData />}
        </ListItem>
        <ListItem>
          {`Computer manufacturer: `}
          {data.computer_information?.computer_manufacturer || <NoData />}
        </ListItem>
        <ListItem>
          {`System type: `}
          {data.computer_information?.system_type || <NoData />}
        </ListItem>
      </ListWrapper>
    </StyledColumnWrapper>
    <StyledColumnWrapper>
      <Paragraph listTitle>Operation system</Paragraph>
      <ListWrapper>
        <ListItem>
          {`Name: `}
          {data.operation_system?.name || <NoData />}
        </ListItem>
        <ListItem>
          {`Version: `}
          {data.operation_system?.version || <NoData />}
        </ListItem>
        <ListItem>
          {`Manufacturer: `}
          {data.operation_system?.manufacturer || <NoData />}
        </ListItem>
        <ListItem>
          {`Configuration: `}
          {data.operation_system?.configuration || <NoData />}
        </ListItem>
        <ListItem>
          {`Build type: `}
          {data.operation_system?.build_type || <NoData />}
        </ListItem>
        <ListItem>
          {`OS architecture: `}
          {data.operation_system?.os_architecture || <NoData />}
        </ListItem>
      </ListWrapper>
    </StyledColumnWrapper>
    <StyledColumnWrapper>
      <Paragraph listTitle>Motherboard information</Paragraph>
      <ListWrapper>
        <ListItem>
          {`Product: `}
          {data.motherboard_information?.product || <NoData />}
        </ListItem>
        <ListItem>
          {`Manufacturer: `}
          {data.motherboard_information?.manufacturer || <NoData />}
        </ListItem>
        <ListItem>
          {`Version: `}
          {data.motherboard_information?.version || <NoData />}
        </ListItem>
        <ListItem>
          {`Serial number: `}
          {data.motherboard_information?.serialnumber || <NoData />}
        </ListItem>
      </ListWrapper>
    </StyledColumnWrapper>
  </StyledCardWrapper>
);

export default HardwareInfoCard;
