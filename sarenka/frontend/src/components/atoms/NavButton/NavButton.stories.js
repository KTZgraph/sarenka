/* eslint-disable import/no-unresolved */
import React from 'react';
import { storiesOf } from '@storybook/react';
import styled from 'styled-components';
import magnifierIcon from 'static/magnifierIcon.svg';
import magnifierIconActive from 'static/magnifierIconActive.svg';
import NavButton from './NavButton';

const StyledWrapper = styled.div`
  background: #252525;
  width: 315px;
  height: 500px;
  padding: 40px 10px;
`;

storiesOf('Atoms/NavButton', module)
  .add('Normal', () => (
    <StyledWrapper>
      <NavButton icon={magnifierIcon}>Frontend vulnerability</NavButton>
    </StyledWrapper>
  ))
  .add('Active', () => (
    <StyledWrapper>
      <NavButton className="active" iconActive={magnifierIconActive}>
        Frontend vulnerability
      </NavButton>
    </StyledWrapper>
  ));
