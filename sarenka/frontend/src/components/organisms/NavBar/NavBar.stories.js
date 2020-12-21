import React from 'react';
import { storiesOf } from '@storybook/react';
import StoryRouter from 'storybook-react-router';
import NavBar from './NavBar';

storiesOf('Organisms/NavButton', module)
  .addDecorator(StoryRouter())
  .add('Normal', () => <NavBar />);
