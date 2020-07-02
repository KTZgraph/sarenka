import React, { useState } from 'react';
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
import regeditIconActive from 'static/regeditIconActive.svg';
import regeditIcon from 'static/regeditIcon.svg';
import HamburgerButton from 'components/atoms/NavButton/HamburgerButton';
import routes from '../../../routes';

const StyledWrapper = styled.nav<{ isVisible: boolean }>`
  position: fixed;
  top: 0;
  left: 0;
  background: #252525;
  max-width: 315px;
  width: 100%;
  height: 100vh;
  padding: 160px 0 0;
  overflow: hidden;
  z-index: 3;
  transition: 0.3s;
  transform: translateX(0);
  @media (max-width: 1100px) {
    transform: ${({ isVisible }) =>
      isVisible ? 'translateX(0%)' : 'translateX(-100%)'};
  }
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
    background: ${({ theme }) => theme.colors.grey};
    margin-bottom: 15px;
    margin-left: -20px;
  }
  }
`;

const NavBar = () => {
  const [isVisible, setIsVisible] = useState(false);

  const handleButtonClick = () => setIsVisible(!isVisible);
  return (
    <>
      <HamburgerButton isOpen={isVisible} onClick={handleButtonClick} />
      <StyledWrapper isVisible={isVisible}>
        <NavButton
          as={NavLink}
          to={routes.remoteHostInfo}
          activeClassName="active"
          icon={magnifierIcon}
          iconactive={magnifierIconActive}
          onClick={handleButtonClick}
        >
          Remote host info
        </NavButton>
        <NavButton
          as={NavLink}
          to={routes.exploits}
          activeClassName="active"
          icon={exploitsIcon}
          iconactive={exploitsIconActive}
          onClick={handleButtonClick}
        >
          Exploits
        </NavButton>
        <NavButton
          as={NavLink}
          to={routes.cveSearch}
          activeClassName="active"
          icon={exploitsIcon}
          iconactive={exploitsIconActive}
          onClick={handleButtonClick}
        >
          Search CVE
        </NavButton>
        <NavButton
          as={NavLink}
          to={routes.registry}
          activeClassName="active"
          onClick={handleButtonClick}
          icon={regeditIcon}
          iconactive={regeditIconActive}
        >
          Windows registry
        </NavButton>
        <NavButton
          as={NavLink}
          to={routes.documentation}
          activeClassName="active"
          icon={docsIcon}
          iconactive={docsIconActive}
          onClick={handleButtonClick}
        >
          Documentation
        </NavButton>
        <StyledSettingsParagraph>Settings</StyledSettingsParagraph>
        <NavButton
          as={NavLink}
          to={routes.settings}
          activeClassName="active"
          icon={settingsIcon}
          iconactive={settingsIconActive}
          onClick={handleButtonClick}
        >
          Settings
        </NavButton>
      </StyledWrapper>
    </>
  );
};

export default NavBar;
