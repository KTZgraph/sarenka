import { keyframes } from 'styled-components';

const FromTop = keyframes`
  0%{
    transform: translateY(-50px);
    opacity: 0;
  }
  100%{
    transform: translateY(0);
    opacity: 1;
  }
`;

export default FromTop;
