import React from 'react';
import styled from 'styled-components';
import { storiesOf } from '@storybook/react';
import Item from './VulnerabilitiesListItem';

const StyledWrapper = styled.ul`
  background: #070809;
  padding: 10px 40px;
`;

storiesOf('Molecules/VulnerabilitiesListItem', module).add('Normal', () => (
  <StyledWrapper>
    <Item
      cveId="CVE-2019-16223"
      cweId="79"
      publishDate="2019-09-11"
      updateDate="2019-09-12"
      complexity="Medium"
      access="Remote"
      score={3.5}
      auth="Single system"
      description="In WordPress before 5.2.3, validation and sanitization of a URL in wp_validate_redirect in wp-includes/pluggable.php could lead to an open redirect."
    />
  </StyledWrapper>
));
