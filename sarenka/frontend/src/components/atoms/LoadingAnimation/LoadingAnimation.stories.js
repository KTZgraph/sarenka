import React from 'react';
import { storiesOf } from '@storybook/react';
import LoadingAnimation from './LoadingAnimation';

storiesOf('Atoms/LoadingAnimation', module).add('Normal', () => (
  <LoadingAnimation bigView />
));
