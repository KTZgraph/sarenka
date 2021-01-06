import React from 'react';
import styled from 'styled-components';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import ListWrapper from 'components/atoms/List/ListWrapper';
import ListItem from 'components/atoms/List/ListItem';
import CweSearchData from 'interfaces/CweSearchData';

const StyledInnerWrapper = styled.div`
  display: grid;
  grid-gap: 30px;
  grid-template-areas: 'cwe title likehood' 'technicalImpact causedBy causedBy';
  @media (max-width: 950px) {
    grid-template-areas: 'cwe title' 'likehood technicalImpact' 'causedBy causedBy';
  }
  @media (max-width: 540px) {
    grid-template-areas: 'cwe' 'title' 'likehood' 'technicalImpact' 'causedBy';
  }

  .cwe {
    grid-area: cwe;
  }
  .title {
    grid-area: title;
  }
  .likehood {
    grid-area: likehood;
  }
  .technical-impact {
    grid-area: technicalImpact;
  }
  .caused-by {
    grid-area: causedBy;
  }
`;

type Props = {
  data: CweSearchData;
};

const CweSearchResult: React.FC<Props> = ({ data }: Props) => (
  <CardWrapper>
    <StyledInnerWrapper>
      <Paragraph className="cwe">
        <strong>CWE: </strong>
        {data.ID_CWE}
      </Paragraph>
      <Paragraph className="title">
        <strong>Title: </strong>
        {data.title}
      </Paragraph>
      <Paragraph className="likehood">
        <strong>Likehood: </strong>
        {data.likehood}
      </Paragraph>
      <Paragraph as="div" className="technical-impact">
        <strong>Technical impact: </strong>
        {data.technical_impact.length <= 1 ? (
          data.technical_impact?.[0]
        ) : (
          <ListWrapper>
            {data.technical_impact.map((element, index) => (
              <ListItem key={index}>{element}</ListItem>
            ))}
          </ListWrapper>
        )}
      </Paragraph>
      <Paragraph as="div" className="caused-by">
        <strong>Caused by: </strong>
        <ListWrapper>
          <ListItem>
            <Paragraph as="span">
              <strong>Field: </strong>
              {data.caused_by?.field}
            </Paragraph>
          </ListItem>
          <ListItem>
            <Paragraph as="span">
              <strong>Process: </strong>
              {data.caused_by?.process}
            </Paragraph>
          </ListItem>
          <ListItem>
            <Paragraph as="span">
              <strong>Description: </strong>
              {data.caused_by?.description}
            </Paragraph>
          </ListItem>
        </ListWrapper>
      </Paragraph>
    </StyledInnerWrapper>
    <Paragraph>
      <strong>Description: </strong>
      {data.description}
    </Paragraph>
  </CardWrapper>
);

export default CweSearchResult;
