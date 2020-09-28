import React from 'react';
import styled from 'styled-components';

const StyledSpan = styled.span`
  color: darkslategray;
  font-style: italic;
`;

const NoData = () => <StyledSpan>No data available</StyledSpan>;

export default NoData;
