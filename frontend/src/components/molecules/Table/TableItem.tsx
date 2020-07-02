import React from 'react';
import styled, { css } from 'styled-components';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import FromTop from 'components/animations/FromTop';

const StyledWrapper = styled.tr<{ delay?: number }>`
  list-style: none;
  padding: 10px 0;
  width: 90%;
  ${({ delay }) =>
    delay &&
    css`
      opacity: 0;
      animation: ${FromTop} 0.2s ease-out forwards;
      animation-delay: ${delay}s;
    `};

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
  delay?: number;
};

const TableItem: React.FC<Props> = ({ columns, wordBreak, delay }: Props) => (
  <StyledWrapper delay={delay}>
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

export default TableItem;
