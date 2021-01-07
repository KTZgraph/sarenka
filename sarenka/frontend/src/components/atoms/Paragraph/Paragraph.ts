import styled, { css } from 'styled-components';
import theme from 'theme/theme';

type Props = {
  bold?: boolean;
  wordBreak?: boolean;
  listTitle?: boolean;
};

const Paragraph = styled.p<Props>`
  font-size: 1.7rem;
  color: ${theme.colors.font};
  font-weight: ${({ bold }) =>
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
