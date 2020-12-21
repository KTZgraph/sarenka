import React from 'react';
import VulnerabilityTemplate from 'templates/VulnerabilityTemplate';
import Heading from 'components/atoms/Heading/Heading';

const DocsView = () => {
  return (
    <VulnerabilityTemplate>
      <Heading>
        In progress...
        <span role="img" aria-label="smile">
          😁
        </span>
      </Heading>
    </VulnerabilityTemplate>
  );
};

export default DocsView;
