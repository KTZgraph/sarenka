import React from 'react';
import styled from 'styled-components';
import background from 'static/settingsBackground.png';

const StyledWrapper = styled.div`
  background-image: url(${background});
  background-position: 50% 0;
  background-repeat: no-repeat;
  background-size: 100% 100%;
  height: 100vh;
`;

const StyledContentWrapper = styled.section`
  text-align: left;
  margin: 50px 110px 0 110px;
`;
const StyledLogoWrapper = styled.div`
  text-align: center;
  padding-top: 50px;
  margin: 0 10px;
`;

type Props = {
  logo: React.ReactNode;
  children: React.ReactNode;
};

const SettingsTemplate = ({ logo, children }: Props) => {
  return (
    <StyledWrapper>
      <StyledLogoWrapper>{logo}</StyledLogoWrapper>
      <StyledContentWrapper>{children}</StyledContentWrapper>
    </StyledWrapper>
  );
};

export default SettingsTemplate;
