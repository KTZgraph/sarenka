import React from 'react';
import styled from 'styled-components';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';
import ListWrapper from 'components/atoms/List/ListWrapper';
import ListItem from 'components/atoms/List/ListItem';
import NoData from 'components/atoms/NoDataText/NoDataText';

const StyledCardWrapper = styled(CardWrapper)`
  column-count: 3;
  @media (max-width: 1360px) {
    column-count: 2;
  }
  @media (max-width: 850px) {
    column-count: 1;
  }
`;

type Props = {
  protocolsPort: Record<string, any>;
  longitude?: number;
  latitude?: number;
  timezone?: string;
  continent?: string;
  registeredCountry?: Record<string, string>;
  description?: string;
  rir?: string;
  routedPrefix?: string;
  path?: number[];
  asn?: number;
  name?: string;
  dnsNames?: string[];
  dnsErrors?: string[];
  os?: string[];
  updatedAt?: string;
};

const GeneralHostInfo: React.FC<Props> = ({
  protocolsPort = {},
  longitude,
  latitude,
  timezone,
  continent,
  registeredCountry,
  description,
  rir,
  routedPrefix,
  path,
  asn,
  name,
  dnsNames,
  dnsErrors,
  os,
  updatedAt,
}: Props) => {
  return (
    <StyledCardWrapper>
      <div>
        <Paragraph listTitle>Protocols port</Paragraph>
        <ListWrapper>
          {Object.keys(protocolsPort).map((key) => (
            <ListItem key={key}>
              {`${key}: ${protocolsPort[key].toString()}`}
            </ListItem>
          ))}
        </ListWrapper>
      </div>
      <Paragraph>
        {`Longitude: `}
        {longitude || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Latitude: `}
        {latitude || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Timezone: `}
        {timezone || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Continent: `}
        {continent || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Registered country: `}
        {registeredCountry ? (
          Object.keys(registeredCountry).map(
            (key) => `${registeredCountry[key].toString()}, `,
          )
        ) : (
          <NoData />
        )}
      </Paragraph>
      <Paragraph>
        {`Description: `}
        {description || <NoData />}
      </Paragraph>
      <Paragraph>
        {`RIR: `}
        {rir || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Routed prefix: `}
        {routedPrefix || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Path: `}
        {path?.toString() || <NoData />}
      </Paragraph>
      <Paragraph>
        {`ASN: `}
        {asn || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Name: `}
        {name || <NoData />}
      </Paragraph>
      <Paragraph>
        {`DNS names: `}
        {dnsNames?.toString() || <NoData />}
      </Paragraph>
      <Paragraph>
        {`DNS errors: `}
        {dnsErrors?.toString() || <NoData />}
      </Paragraph>
      <Paragraph>
        {`OS: `}
        {os?.toString() || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Updated at: `}
        {updatedAt || <NoData />}
      </Paragraph>
    </StyledCardWrapper>
  );
};

export default GeneralHostInfo;
