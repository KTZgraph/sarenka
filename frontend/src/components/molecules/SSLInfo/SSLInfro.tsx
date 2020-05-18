import React from 'react';
import styled from 'styled-components';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import { ReactComponent as WarningIcon } from 'static/warningIcon.svg';

const StyledCardWrapper = styled.section`
  background: #070809;
  border: 1px solid #333333;
  box-sizing: border-box;
  border-radius: 4px;
  padding: 30px;
`;

const StyledWrapper = styled.div`
  display: grid;
  grid-gap: 40px;
  grid-template-columns: 1fr 1fr;
`;

const StyledParagraphWrapper = styled.div`
  margin-left: 15px;
`;

const StyledWarningIcon = styled(WarningIcon)`
  margin-left: 10px;
  transform: translateY(25%);
`;

type Props = {
  host: string;
  subjectDN?: string;
  issuerDN?: string;
  serial?: string;
  validity?: string;
  names?: string;
  sslv3?: boolean;
  exportDhe?: boolean;
  exportRsa?: boolean;
  dheSupport?: boolean;
};

const SSLInfo: React.FC<Props> = ({
  host,
  subjectDN,
  issuerDN,
  serial,
  validity,
  names,
  sslv3,
  exportDhe,
  exportRsa,
  dheSupport,
}: Props) => (
  <StyledWrapper>
    <StyledCardWrapper>
      <Paragraph>
        Host:
        {host}
      </Paragraph>
      <Paragraph>SSL Certificate</Paragraph>
      <StyledParagraphWrapper>
        <Paragraph>
          <strong>Subject DN: </strong>
          {subjectDN}
        </Paragraph>
        <Paragraph>
          <strong>Issuer DN:</strong>
          {issuerDN}
        </Paragraph>
        <Paragraph>
          <strong>Serial:</strong>
          {serial}
        </Paragraph>
        <Paragraph>
          <strong>Validity:</strong>
          {validity}
        </Paragraph>
        <Paragraph>
          <strong>Names:</strong>
          {names}
        </Paragraph>
      </StyledParagraphWrapper>
    </StyledCardWrapper>
    <StyledCardWrapper>
      <div>
        <Paragraph>
          <strong>SSLv3 Support:</strong>
          {` ${sslv3}`}
          {sslv3 && <StyledWarningIcon />}
        </Paragraph>
        <Paragraph>
          <strong>Export DHE:</strong>
          {` ${exportDhe}`}
        </Paragraph>
        <Paragraph>
          <strong>Export RSA:</strong>
          {` ${exportRsa}`}
        </Paragraph>
        <Paragraph>
          <strong>DHE Support:</strong>
          {` ${dheSupport}`}
        </Paragraph>
      </div>
    </StyledCardWrapper>
  </StyledWrapper>
);

export default SSLInfo;
