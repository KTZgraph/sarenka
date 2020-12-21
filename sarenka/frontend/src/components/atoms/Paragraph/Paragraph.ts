import styled, { css } from 'styled-components';

type Props = {
  bold?: boolean;
  wordBreak?: boolean;
  listTitle?: boolean;
};

const Paragraph = styled.p<Props>`
  font-size: 1.7rem;
  color: #e0e0e0;
  font-weight: ${({ bold, theme }) =>
    bold ? theme.font.weight.bold : theme.font.weight.regular};
  word-break: ${({ wordBreak }) => (wordBreak ? 'break-all' : 'normal')};
  ${({ listTitle }) =>
    listTitle &&
    css`
      margin-top: 0;
      margin-bottom: 5px;
    `}
`;

export default Paragraph;
