import React from 'react';
import { storiesOf } from '@storybook/react';
import styled from 'styled-components';
import Input from './Input';

const StyledWrapper = styled.div`
  background: #252525;
  height: 500px;
  width: 700px;
  padding: 70px;
`;

storiesOf('Atoms/Input', module)
  .add('Normal', () => (
    <StyledWrapper>
      <Input id="name" name="name" type="text" placeholder="Type your name" />
    </StyledWrapper>
  ))
  .add('Search', () => (
    <StyledWrapper>
      <Input
        id="search"
        name="search"
        type="text"
        placeholder="Type website address"
        search
      />
    </StyledWrapper>
  ));
