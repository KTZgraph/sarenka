import React from 'react';
import styled from 'styled-components';
import { storiesOf } from '@storybook/react';
import VulnerabilitiesList from './VulnerabilitiesList';

const StyledWrapper = styled.div`
  padding: 30px;
  background: #000000;
`;

const dummyData = [
  {
    cveId: 'CVE-2019-16223',
    cweId: '79',
    publishDate: '2019-09-11',
    updateDate: '2019-09-12',
    complexity: 'Medium',
    access: 'Remote',
    score: 3.5,
    auth: 'Single system',
    description:
      'In WordPress before 5.2.3, validation and sanitization of a URL in wp_validate_redirect in wp-includes/pluggable.php could lead to an open redirect.',
  },
  {
    cveId: 'CVE-2019-16220',
    cweId: '601',
    publishDate: '2019-09-11',
    updateDate: '2019-09-12',
    complexity: 'Medium',
    access: 'Remote',
    score: 7.5,
    auth: 'Single system',
    description:
      'In WordPress before 5.2.3, validation and sanitization of a URL in wp_validate_redirect in wp-includes/pluggable.php could lead to an open redirect.',
  },
];

storiesOf('Organisms/VulnerabilitiesList', module).add('Normal', () => (
  <StyledWrapper>
    <VulnerabilitiesList
      port={8080}
      title=" Example website title"
      foundTechnologies="Wordpress 5.2.2"
      vulnerabilitiesList={dummyData}
    />
  </StyledWrapper>
));
