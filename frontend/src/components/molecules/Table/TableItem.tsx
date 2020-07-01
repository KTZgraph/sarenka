import React from 'react';
import styled from 'styled-components';
import Paragraph from 'components/atoms/Paragraph/Paragraph';

const StyledWrapper = styled.tr`
  list-style: none;
  padding: 10px 0;
  width: 90%;

  & > td {
    padding: 0 10px;
  }
`;

const StyledParagraph = styled(Paragraph)`
  word-break: break-all;
`;

type Props = {
  columns: Array<string>;
  wordBreak?: number;
};

const CveSearchListItem: React.FC<Props> = ({ columns, wordBreak }: Props) => (
  <StyledWrapper>
    {columns.map((column, index) => (
      // eslint-disable-next-line react/no-array-index-key
      <td key={index}>
        {index === wordBreak ? (
          <StyledParagraph>{column}</StyledParagraph>
        ) : (
          <Paragraph>{column}</Paragraph>
        )}
      </td>
    ))}
  </StyledWrapper>
);

export default CveSearchListItem;
