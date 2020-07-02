import React from 'react';
import styled from 'styled-components';

const StyledOpenNavButton = styled.button<{ isOpen: boolean }>`
  display: none;
  position: fixed;
  top: 20px;
  left: 20px;
  height: 30px;
  border: none;
  z-index: 4;
  background: transparent;
  outline: none;

  cursor: pointer;
  @media (max-width: 1100px) {
    display: block;
  }
`;

const StyledMenuIcon = styled.div<{ isOpen: boolean }>`
  display: inline-block;
  width: 30px;
  height: 20px;
  margin-right: 10px;
  position: relative;
  background: transparent;
  align-items: center;
  justify-content: center;

  & > .line {
    display: block;
    position: absolute;
    height: 0;
    border: 1.5px solid ${({ theme }) => theme.colors.grey};
    width: 100%;
    transition: 0.4s;
    background: ${({ theme }) => theme.colors.grey};
    border-radius: 10px;
  }

  & > .first-line {
    top: 0;
    left: 0;

    transform: ${({ isOpen }) =>
      isOpen ? 'translateY(10px) rotate(45deg)' : 'translateY(0) rotate(0)'};
  }
  & > .second-line {
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    opacity: ${({ isOpen }) => (isOpen ? '0' : '1')};
  }
  & > .third-line {
    top: 100%;
    left: 0;
    transform: ${({ isOpen }) =>
      isOpen
        ? 'translateY(-10px) rotate(-45deg)'
        : 'translateY(-100%) rotate(0)'};
  }
`;

interface MenuProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  isOpen: boolean;
}

const OpenNavMenuButton = ({ isOpen, onClick }: MenuProps) => (
  <StyledOpenNavButton isOpen={isOpen} onClick={onClick}>
    <StyledMenuIcon isOpen={isOpen}>
      <div className="line first-line" />
      <div className="line second-line" />
      <div className="line third-line" />
    </StyledMenuIcon>
  </StyledOpenNavButton>
);

export default OpenNavMenuButton;
