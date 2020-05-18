import React from 'react';
import { storiesOf } from '@storybook/react';
import Checkbox from './Checkbox';

storiesOf('Atoms/Checkbox', module).add('Normal', () => (
  <Checkbox type="checkbox" />
));
