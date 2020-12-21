import React from 'react';
import { storiesOf } from '@storybook/react';
import Paragraph from './Paragraph';

storiesOf('Atoms/Paragraph', module)
  .add('Normal', () => <Paragraph>SSL certificate</Paragraph>)
  .add('Bold', () => <Paragraph bold>SSL certificate</Paragraph>);
