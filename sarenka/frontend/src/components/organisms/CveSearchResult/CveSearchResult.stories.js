import React from 'react';
import styled from 'styled-components';
import { storiesOf } from '@storybook/react';
import CveSearchResult from './CveSearchResult';

const DummyData = {
  cve: 'CVE-2010-3333',
  cvss_vector: 'AV:N/AC:M/Au:N/C:C/I:C/A:C',
  complexity: 'medium',
  authentication: 'none',
  vector: 'network',
  cvss: '9.3',
  cwe: 'CWE-119',
  title: 'RTF Stack Buffer Overflow Vulnerability',
  availability: 'COMPLETE',
  confidentiality: 'COMPLETE',
  products: [
    {
      vendor: 'microsoft',
      name: 'office',
      version: '2003',
      system: 'sp3',
    },
    {
      vendor: 'microsoft',
      name: 'office',
      version: '2004',
      system: '*',
    },
    {
      vendor: 'microsoft',
      name: 'office',
      version: '2007',
      system: 'sp2',
    },
    {
      vendor: 'microsoft',
      name: 'office',
      version: '2008',
      system: '*',
    },
    {
      vendor: 'microsoft',
      name: 'office',
      version: '2010',
      system: '*',
    },
    {
      vendor: 'microsoft',
      name: 'office',
      version: '2011',
      system: '*',
    },
    {
      vendor: 'microsoft',
      name: 'office',
      version: 'xp',
      system: 'sp3',
    },
    {
      vendor: 'microsoft',
      name: 'open_xml_file_format_converter',
      version: '*',
      system: '*',
    },
  ],
};

const StyledWrapper = styled.div`
  padding: 30px;
  background: #000000;
`;

storiesOf('Organisms/CveSearchResult', module).add('Normal', () => (
  <StyledWrapper>
    <CveSearchResult
      title={DummyData.title}
      cve={DummyData.cve}
      cwe={DummyData.cwe}
      cvssvector={DummyData.cvss_vector}
      complexity={DummyData.complexity}
      auth={DummyData.authentication}
      score={DummyData.cvss}
      availability={DummyData.availability}
      confidentiality={DummyData.confidentiality}
      products={DummyData.products}
    />
  </StyledWrapper>
));
