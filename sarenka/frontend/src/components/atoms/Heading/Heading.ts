import styled from 'styled-components';

type Props = {
  regularfont?: boolean;
  bigFont?: boolean;
};

const Heading = styled.h1<Props>`
  font-size: ${({ bigFont }) => (bigFont ? '4rem' : '2.6rem')};
  color: #e0e0e0;
  font-weight: ${({ theme, regularfont }) =>
    regularfont ? theme.font.weight.regular : theme.font.weight.bold};
`;

export default Heading;
