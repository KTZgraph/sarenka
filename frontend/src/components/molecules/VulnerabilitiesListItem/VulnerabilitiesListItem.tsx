import React from 'react';
import styled from 'styled-components';
import Paragraph from 'components/atoms/Paragraph/Paragraph';

const StyledWrapper = styled.li`
  list-style: none;
  padding: 10px 0;

  &::after {
    content: '';
    display: block;
    background: #333333;
    width: 100%;
    height: 1px;
  }
`;
const StyledParagraphWrapper = styled.div`
  display: grid;
  grid-template-columns: repeat(4, 1fr);
`;

const ParagraphRedBorder = styled(Paragraph)`
  max-width: 95px;
  align-content: center;
  padding: 10px;
  background: #c10c274f;
  transform: translateY(-10px);
  border-radius: 4px;
`;

type Props = {
  cveId?: string;
  cweId?: string;
  publishDate?: string;
  updateDate?: string;
  complexity?: string;
  access?: string;
  score?: number;
  auth?: string;
  description?: string;
};

const VulnerabilitiesListItem: React.FC<Props> = ({
  cveId,
  cweId,
  publishDate,
  updateDate,
  complexity,
  access,
  score,
  auth,
  description,
}: Props) => (
  <StyledWrapper>
    <StyledParagraphWrapper>
      <Paragraph>
        CVE ID:
        {cveId}
      </Paragraph>
      <Paragraph>
        CWE ID:
        {cweId}
      </Paragraph>
      <Paragraph>
        Publish Date:
        {publishDate}
      </Paragraph>
      <Paragraph>
        Update Date:
        {updateDate}
      </Paragraph>
      <Paragraph>
        Complexity:
        {complexity}
      </Paragraph>
      <Paragraph>
        Access:
        {access}
      </Paragraph>
      <ParagraphRedBorder>
        Score:
        {score}
      </ParagraphRedBorder>
      <Paragraph>
        Authentication:
        {auth}
      </Paragraph>
    </StyledParagraphWrapper>
    <Paragraph>
      Description:
      {description}
    </Paragraph>
  </StyledWrapper>
);

export default VulnerabilitiesListItem;
