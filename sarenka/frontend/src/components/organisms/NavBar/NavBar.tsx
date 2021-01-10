import React, { useState } from 'react';
import styled from 'styled-components';
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
import hardwareIcon from 'static/hardwareIcon.svg';
import hardwareIconActive from 'static/hardwareIconActive.svg';
import HamburgerButton from 'components/atoms/NavButton/HamburgerButton';
import theme from 'theme/theme';
import { useDispatch } from 'react-redux';
import { routesWithoutTab } from 'routes';
import ScrollableTabButtons from 'views/TabsView/TabsView';
import { createNewTab } from 'actions/TabsActions';

const StyledWrapper = styled.nav<{ isVisible: boolean }>`
  position: fixed;
  top: 0;
  left: 0;
  background: ${theme.colors.darkGreyNoTransparency};
  max-width: 315px;
  width: 100%;
  height: 100vh;
  padding: 50px 0 0;
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
    background: ${theme.colors.grey};
    margin-bottom: 15px;
    margin-left: -20px;
  }
  }
`;

const NavBar = () => {
  const [isVisible, setIsVisible] = useState(false);
  const dispatch = useDispatch();
  const handleButtonClick = () => setIsVisible(!isVisible);

  const handleClick = (route: string, label: string) => {
    dispatch(createNewTab(route, label));
    setIsVisible(!isVisible);
  };
  return (
    <>
      <HamburgerButton isOpen={isVisible} onClick={handleButtonClick} />
      <StyledWrapper isVisible={isVisible}>
        <NavButton
          icon={magnifierIcon}
          iconactive={magnifierIconActive}
          onClick={() =>
            handleClick(routesWithoutTab.remoteHostInfo, 'Remote host info')}
        >
          Remote host info
        </NavButton>
        <NavButton
          icon={exploitsIcon}
          iconactive={exploitsIconActive}
          onClick={() => handleClick(routesWithoutTab.cveSearch, 'Search CVE')}
        >
          Search CVE / CWE
        </NavButton>
        <NavButton
          icon={regeditIcon}
          iconactive={regeditIconActive}
          onClick={() => handleClick(routesWithoutTab.registry, 'Registry')}
        >
          Windows registry
        </NavButton>
        <NavButton
          icon={hardwareIcon}
          iconactive={hardwareIconActive}
          onClick={() =>
            handleClick(routesWithoutTab.hardwareInfo, 'Hardware info')}
        >
          Hardware info
        </NavButton>
        <StyledSettingsParagraph>Settings</StyledSettingsParagraph>
        <NavButton
          icon={settingsIcon}
          iconactive={settingsIconActive}
          onClick={() => handleClick(routesWithoutTab.settings, 'Settings')}
        >
          Settings
        </NavButton>
        <NavButton
          icon={docsIcon}
          iconactive={docsIconActive}
          onClick={() =>
            handleClick(routesWithoutTab.documentation, 'Documentation')}
        >
          Documentation
        </NavButton>
        <StyledSettingsParagraph>Tabs</StyledSettingsParagraph>
        <ScrollableTabButtons />
      </StyledWrapper>
    </>
  );
};

export default NavBar;
