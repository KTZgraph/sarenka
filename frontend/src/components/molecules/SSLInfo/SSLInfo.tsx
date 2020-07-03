import React from 'react';
import styled from 'styled-components';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import { ReactComponent as WarningIcon } from 'static/warningIcon.svg';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';

const StyledCardWrapper = styled(CardWrapper)`
  margin-bottom: 40px;
`;

const StyledWarningIcon = styled(WarningIcon)`
  margin-left: 10px;
  transform: translateY(25%);
`;

const StyledListItem = styled.li`
  word-break: break-all;
  font-size: 1.7rem;
  color: #e0e0e0;
  font-weight: ${({ theme }) => theme.font.weight.regular};
  list-style: none;
  line-height: 2.3rem;
`;

const StyledListWrapper = styled.ul`
  margin: 0 0 0 15px;
  padding: 0;
`;

const StyledListTitle = styled(Paragraph)`
  margin-bottom: 5px;
`;

const StyledParagraphWithBreak = styled(Paragraph)`
  word-break: break-all;
`;

type Props = {
  httpsData: Record<string, any>;
};

const SSLInfo: React.FC<Props> = ({ httpsData }: Props) => {
  const NoData = 'No data available';
  return (
    <StyledCardWrapper>
      <Paragraph>
        {`Web page title: `}
        {httpsData?.webpage_title || NoData}
      </Paragraph>
      <StyledParagraphWithBreak>
        {`Web page body SHA256: `}
        {httpsData?.webpage_body_sha256 || NoData}
      </StyledParagraphWithBreak>
      <Paragraph>
        {`Status code: `}
        {httpsData?.status_code || NoData}
      </Paragraph>
      <StyledListTitle>Metadata</StyledListTitle>
      <StyledListWrapper>
        <StyledListItem>
          {`Product: `}
          {httpsData?.get_metadata.product || NoData}
        </StyledListItem>
        <StyledListItem>
          {`Version: `}
          {httpsData?.get_metadata.version || NoData}
        </StyledListItem>
        <StyledListItem>
          {`Description: `}
          {httpsData?.get_metadata.description || NoData}
        </StyledListItem>
        <StyledListItem>
          {`Manufacturer: `}
          {httpsData?.get_metadata.manufacturer || NoData}
        </StyledListItem>
      </StyledListWrapper>
      <Paragraph>
        {`RSA export: `}
        {httpsData?.rsa_export.toString() || NoData}
      </Paragraph>
      <Paragraph>
        {`RSA length: `}
        {httpsData?.rsa_length || NoData}
      </Paragraph>
      <StyledParagraphWithBreak>
        {`RSA modulus: `}
        {httpsData?.rsa_modulus || NoData}
      </StyledParagraphWithBreak>
      <Paragraph>
        {`RSA exponent: `}
        {httpsData?.rsa_exponent || NoData}
      </Paragraph>
      <Paragraph>
        {`DHE export: `}
        {httpsData?.dhe_export?.toString() || NoData}
      </Paragraph>
      <StyledListTitle>DH params</StyledListTitle>
      <StyledListWrapper>
        <StyledListItem>
          {`Prime length: `}
          {httpsData?.dh_params.prime_length || NoData}
        </StyledListItem>
        <StyledListItem>
          {`Prime value: `}
          {httpsData?.dh_params.prime_value || NoData}
        </StyledListItem>
        <StyledListItem>
          {`Generator length: `}
          {httpsData?.dh_params.generator_length || NoData}
        </StyledListItem>
        <StyledListItem>
          {`Generator value: `}
          {httpsData?.dh_params.generator_value || NoData}
        </StyledListItem>
      </StyledListWrapper>
      <Paragraph>
        {`DHE support: `}
        {httpsData?.dhe_support?.toString() || NoData}
      </Paragraph>
      <Paragraph>
        {`Heartbleed: `}
        {httpsData?.heartbleed?.toString() || NoData}
        {httpsData?.heartbleed && <StyledWarningIcon />}
      </Paragraph>
      <Paragraph>
        {`Logjam attack: `}
        {httpsData?.logjam_attack?.toString() || NoData}
        {httpsData?.logjam_attack && <StyledWarningIcon />}
      </Paragraph>
      <Paragraph>
        {`Freak attack: `}
        {httpsData?.freak_attack?.toString() || NoData}
        {httpsData?.freak_attack && <StyledWarningIcon />}
      </Paragraph>
      <Paragraph>
        {`Poodle attack: `}
        {httpsData?.poodle_attack?.toString() || NoData}
        {httpsData?.poodle_attack && <StyledWarningIcon />}
      </Paragraph>
    </StyledCardWrapper>
  );
};

export default SSLInfo;
