import React from 'react';
import styled from 'styled-components';
import NavBar from 'components/organisms/NavBar/NavBar';

const StyledWrapper = styled.div`
  margin-left: 315px;
  @media (max-width: 1100px) {
    margin-left: 0px;
  }
`;

type Props = {
  children: React.ReactNode;
};

const MainTemplate = ({ children }: Props) => (
  <StyledWrapper>
    <NavBar />
    {children}
  </StyledWrapper>
);

export default MainTemplate;
