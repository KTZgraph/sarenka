import React from 'react';
import Heading from 'components/atoms/Heading/Heading';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import SettingsTemplate from 'templates/SettingsTemplate';
import logo from 'static/logo.svg';
import LinkButton from 'components/atoms/LinkButton/LinkButton';
import { documentationRoutes } from 'routes';

const DocsView = () => {
  return (
    <SettingsTemplate logo={<img src={logo} alt="App logo." />}>
      <Heading regularfont bigFont>
        Documentation
      </Heading>
      <Paragraph>
        API documentation
        <LinkButton url={documentationRoutes.apiDocumentation} />
      </Paragraph>
    </SettingsTemplate>
  );
};

export default DocsView;
