import styled from 'styled-components';

type Props = {
  bold?: boolean;
};

const Paragraphs = styled.p<Props>`
  font-size: 1.7rem;
  color: #e0e0e0;
  font-weight: ${({ bold, theme }) =>
    bold ? theme.font.weight.bold : theme.font.weight.regular};
`;

export default Paragraphs;
