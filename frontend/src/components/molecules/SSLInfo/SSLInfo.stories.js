import React from 'react';
import styled from 'styled-components';
import { storiesOf } from '@storybook/react';
import SSLInfo from './SSLInfo';

const StyledWrapper = styled.div`
  padding: 30px;
  background: #000000;
`;

storiesOf('Molecules/SSLInfo', module).add('Normal', () => (
  <StyledWrapper>
    <SSLInfo
      host=" 267.102.41.2"
      subjectDN=" CN=en.slovakiatatry.sk"
      issuerDN=" C=US, O=Let’s Encrypt. CN=Let’s Encrypt Authority X3"
      serial=" 28920623547880476758717595455198746335398775"
      validity=" 2020-03-10 12:45:34 to 2020-06-08 12:45:34 (90 days, 0:00:00)"
      names=" en.slovakiatatry.sk"
      sslv3
      exportDhe={false}
      exportRsa={false}
      dheSupport
    />
  </StyledWrapper>
));
