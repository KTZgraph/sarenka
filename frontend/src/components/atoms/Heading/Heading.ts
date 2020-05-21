import styled from 'styled-components';

type Props = {
  regularfont?: boolean;
};

const Heading = styled.h1<Props>`
  font-size: 3rem;
  color: #e0e0e0;
  font-weight: ${({ theme, regularfont }) =>
    regularfont ? theme.font.weight.regular : theme.font.weight.bold};
`;

export default Heading;
