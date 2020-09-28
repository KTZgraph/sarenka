import React from 'react';
import styled from 'styled-components';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';
import ListItem from 'components/atoms/List/ListItem';
import ListWrapper from 'components/atoms/List/ListWrapper';
import WarningIcon from 'components/atoms/WarningIcon/WarningIcon';
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
  httpsData: Record<string, any>;
};

const HTTPSInfo: React.FC<Props> = ({ httpsData }: Props) => {
  return (
    <StyledCardWrapper>
      <Paragraph>
        {`Web page title: `}
        {httpsData?.webpage_title || <NoData />}
      </Paragraph>
      <Paragraph wordBreak>
        {`Web page body SHA256: `}
        {httpsData?.webpage_body_sha256 || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Status code: `}
        {httpsData?.status_code || <NoData />}
      </Paragraph>
      <div>
        <Paragraph listTitle>Metadata</Paragraph>
        <ListWrapper>
          <ListItem>
            {`Product: `}
            {httpsData?.get_metadata.product || <NoData />}
          </ListItem>
          <ListItem>
            {`Version: `}
            {httpsData?.get_metadata.version || <NoData />}
          </ListItem>
          <ListItem>
            {`Description: `}
            {httpsData?.get_metadata.description || <NoData />}
          </ListItem>
          <ListItem>
            {`Manufacturer: `}
            {httpsData?.get_metadata.manufacturer || <NoData />}
          </ListItem>
        </ListWrapper>
      </div>
      <Paragraph>
        {`RSA export: `}
        {httpsData?.rsa_export.toString() || <NoData />}
        {httpsData?.rsa_export && <WarningIcon />}
      </Paragraph>
      <Paragraph>
        {`RSA length: `}
        {httpsData?.rsa_length || <NoData />}
      </Paragraph>
      <Paragraph wordBreak>
        {`RSA modulus: `}
        {httpsData?.rsa_modulus || <NoData />}
      </Paragraph>
      <Paragraph>
        {`RSA exponent: `}
        {httpsData?.rsa_exponent || <NoData />}
      </Paragraph>
      <Paragraph>
        {`DHE export: `}
        {httpsData?.dhe_export?.toString() || <NoData />}
        {httpsData?.dhe_export && <WarningIcon />}
      </Paragraph>
      <div>
        <Paragraph listTitle>DH params</Paragraph>
        <ListWrapper>
          <ListItem>
            {`Prime length: `}
            {httpsData?.dh_params.prime_length || <NoData />}
          </ListItem>
          <ListItem>
            {`Prime value: `}
            {httpsData?.dh_params.prime_value || <NoData />}
          </ListItem>
          <ListItem>
            {`Generator length: `}
            {httpsData?.dh_params.generator_length || <NoData />}
          </ListItem>
          <ListItem>
            {`Generator value: `}
            {httpsData?.dh_params.generator_value || <NoData />}
          </ListItem>
        </ListWrapper>
      </div>
      <Paragraph>
        {`DHE support: `}
        {httpsData?.dhe_support?.toString() || <NoData />}
      </Paragraph>
      <Paragraph>
        {`Heartbleed: `}
        {httpsData?.heartbleed?.toString() || <NoData />}
        {httpsData?.heartbleed && <WarningIcon />}
      </Paragraph>
      <Paragraph>
        {`Logjam attack: `}
        {httpsData?.logjam_attack?.toString() || <NoData />}
        {httpsData?.logjam_attack && <WarningIcon />}
      </Paragraph>
      <Paragraph>
        {`Freak attack: `}
        {httpsData?.freak_attack?.toString() || <NoData />}
        {httpsData?.freak_attack && <WarningIcon />}
      </Paragraph>
      <Paragraph>
        {`Poodle attack: `}
        {httpsData?.poodle_attack?.toString() || <NoData />}
        {httpsData?.poodle_attack && <WarningIcon />}
      </Paragraph>
    </StyledCardWrapper>
  );
};

export default HTTPSInfo;
