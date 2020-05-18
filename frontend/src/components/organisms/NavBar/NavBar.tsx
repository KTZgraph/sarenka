import React from 'react';
import styled from 'styled-components';
import { NavLink } from 'react-router-dom';
import NavButton from 'components/atoms/NavButton/NavButton';
import settingsIcon from 'static/settingsIcon.svg';
import settingsIconActive from 'static/settingsIconActive.svg';
import docsIcon from 'static/docsIcon.svg';
import docsIconActive from 'static/docsIconActive.svg';
import exploitsIconActive from 'static/exploitsIconActive.svg';
import exploitsIcon from 'static/exploitsIcon.svg';
import magnifierIconActive from 'static/magnifierIconActive.svg';
import magnifierIcon from 'static/magnifierIcon.svg';

const StyledWrapper = styled.nav`
  background: #252525;
  max-width: 315px;
  height: 100vh;
  padding: 160px 0 0;
  overflow: hidden;
`;

const StyledSettingsParagraph = styled.p`
  font-size: 1.4rem;
  color: #9e9e9e;
  letter-spacing: 0.25px;
  margin-left: 20px;
  &::before {
    content: '';
    display: block;
    width: 315px;
    height: 1px;
    background: #bdbdbd;
    margin-bottom: 15px;
    margin-left: -20px;
  }
`;

const NavBar = () => (
  <StyledWrapper>
    <NavButton
      as={NavLink}
      to="/frontend"
      activeClassName="active"
      icon={magnifierIcon}
      iconActive={magnifierIconActive}
    >
      Frontend vulnarbility
    </NavButton>
    <NavButton
      as={NavLink}
      to="/backend"
      activeClassName="active"
      icon={magnifierIcon}
      iconActive={magnifierIconActive}
    >
      Backend vulnarbility
    </NavButton>
    <NavButton
      as={NavLink}
      to="/exploits"
      activeClassName="active"
      icon={exploitsIcon}
      iconActive={exploitsIconActive}
    >
      Exploits
    </NavButton>
    <NavButton as={NavLink} to="/registry" activeClassName="active">
      Windows registry
    </NavButton>
    <NavButton
      as={NavLink}
      to="/docs"
      activeClassName="active"
      icon={docsIcon}
      iconActive={docsIconActive}
    >
      Documentation
    </NavButton>
    <StyledSettingsParagraph>Settings</StyledSettingsParagraph>
    <NavButton
      as={NavLink}
      to="/settings"
      activeClassName="active"
      icon={settingsIcon}
      iconActive={settingsIconActive}
    >
      Main Settings
    </NavButton>
  </StyledWrapper>
);

export default NavBar;
