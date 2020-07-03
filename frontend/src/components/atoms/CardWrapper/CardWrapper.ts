import styled from 'styled-components';
import FadeIn from 'components/animations/FadeIn';

const CardWrapper = styled.section`
  background: #070809;
  border: 1px solid #333333;
  box-sizing: border-box;
  border-radius: 4px;
  padding: 30px;
  animation: 0.5s ${FadeIn} ease-out forwards;
`;

export default CardWrapper;
