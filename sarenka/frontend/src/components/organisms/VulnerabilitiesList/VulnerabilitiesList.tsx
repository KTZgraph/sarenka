import React, { useState } from 'react';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';
import ListItem from 'components/molecules/VulnerabilitiesListItem/VulnerabilitiesListItem';
import Checkbox from 'components/atoms/Checkbox/Checkbox';

type Props = {
  port: number;
  title?: string;
  foundTechnologies?: string | string[];
  vulnerabilitiesList: {
    cveId: string;
    cweId?: string;
    publishDate?: string;
    updateDate?: string;
    complexity?: string;
    access?: string;
    score?: number;
    auth?: string;
    description?: string;
  }[];
};

const VulnerabilitiesList: React.FC<Props> = ({
  port,
  title,
  foundTechnologies,
  vulnerabilitiesList,
}: Props) => {
  const [criticalOnly, setCriticalOnly] = useState<boolean>(false);

  const handleCrticalOnly = () => {
    setCriticalOnly(!criticalOnly);
  };

  return (
    <CardWrapper>
      <Paragraph>
        Port:
        {port}
      </Paragraph>
      <Paragraph>
        Title:
        {title}
      </Paragraph>
      <Paragraph>
        Founded Technologies:
        {foundTechnologies}
      </Paragraph>
      <Paragraph as="label" htmlFor="criticalOnly">
        Show only critical errors
        <Checkbox
          type="checkbox"
          id="criticalOnly"
          name="criticalOnly"
          onClick={handleCrticalOnly}
        />
      </Paragraph>
      <Paragraph>Vulnerabilities</Paragraph>
      <ul>
        {vulnerabilitiesList.map(
          ({
            cveId,
            cweId,
            publishDate,
            updateDate,
            complexity,
            access,
            score = 0,
            auth,
            description,
          }) => {
            if (criticalOnly && score < 7) {
              return null;
            }
            return (
              <ListItem
                key={cveId}
                cweId={cweId}
                cveId={cveId}
                publishDate={publishDate}
                updateDate={updateDate}
                complexity={complexity}
                access={access}
                score={score}
                auth={auth}
                description={description}
              />
            );
          },
        )}
      </ul>
    </CardWrapper>
  );
};

export default VulnerabilitiesList;
