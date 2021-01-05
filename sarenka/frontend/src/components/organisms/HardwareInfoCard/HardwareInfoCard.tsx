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
      <Paragraph listTitle>Computer name</Paragraph>
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
    </StyledColumnWrapper>
    <StyledColumnWrapper>
      <Paragraph listTitle>Computer info</Paragraph>
      <ListWrapper>
        <ListItem>
          {`Serial number: `}
          {data.commputer_information?.commputer_serial_number || <NoData />}
        </ListItem>
        <ListItem>
          {`MAC Address: `}
          {data.commputer_information?.[`mac_address???`] || <NoData />}
        </ListItem>
        <ListItem>
          {`Total physical memory: `}
          {data.commputer_information?.total_physical_memory || <NoData />}
        </ListItem>
        <ListItem>
          {`Computer manufacturer: `}
          {data.commputer_information?.computer_manufacturer || <NoData />}
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
          {data.baseboard_information?.product || <NoData />}
        </ListItem>
        <ListItem>
          {`Manufacturer: `}
          {data.baseboard_information?.manufacturer || <NoData />}
        </ListItem>
        <ListItem>
          {`Version: `}
          {data.baseboard_information?.version || <NoData />}
        </ListItem>
        <ListItem>
          {`Serial number: `}
          {data.baseboard_information?.serialnumber || <NoData />}
        </ListItem>
      </ListWrapper>
    </StyledColumnWrapper>
  </StyledCardWrapper>
);

export default HardwareInfoCard;
