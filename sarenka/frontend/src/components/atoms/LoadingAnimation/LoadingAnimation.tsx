import React from 'react';
import styled, { keyframes } from 'styled-components';

const BounceAnimation = keyframes`
  0% { transform: translateY(0);}
  50% { transform: translateY(-100%); }
  100% { transform: translateY(0); }
`;
const StyledDotWrapper = styled.div<{ bigView: boolean }>`
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
  width: 100%;
  height: ${({ bigView }) => (bigView ? '100vh' : '100%')};
`;
const StyledDot = styled.div<{ delay: string }>`
  background-color: ${({ theme }) => theme.colors.red};
  border-radius: 50%;
  width: 10px;
  height: 10px;
  margin: 0 5px;
  transform: translateY(0);
  animation: ${BounceAnimation} 0.8s linear infinite;
  animation-delay: ${({ delay }) => delay};
`;
type Props = {
  bigView?: boolean;
};

const LoadingAnimation: React.FC<Props> = ({ bigView = false }: Props) => (
  <StyledDotWrapper bigView={bigView}>
    <StyledDot delay="0s" />
    <StyledDot delay=".2s" />
    <StyledDot delay=".4s" />
  </StyledDotWrapper>
);
export default LoadingAnimation;
