import React from 'react';
import styled, { css } from 'styled-components';
import removeIcon from 'static/removeIcon.svg';
import NavButton from '../NavButton/NavButton';

const StyledNavButton = styled(NavButton)`
  background: none;
  padding: 0;
  display: inline-block;
  &:focus {
    outline: 0;
  }
`;

const StyledRemoveButton = styled.button<{ icon: any }>`
  background: transparent url(${({ icon }) => icon}) no-repeat 15px 50%;
  background-size: 21px;
  border: none;
  width: 64px;
  height: 20px;
  display: inline-block;
  cursor: pointer;
  transform: translateY(20%);

  &:focus {
    outline: 0;
  }
`;

const StyledWrapper = styled.div<{ isActive: boolean }>`
  transition: 0.3s;
  ${({ isActive }) =>
    isActive &&
    css`
      background-color: rgba(193, 12, 39, 0.52);
      border-radius: 4px;
      color: #ffffff;
    `}
`;

type params = {
  index: number;
  label: string;
  onClick: Function;
  onRemoveClick: Function;
  isActive: boolean;
};

const Tab = ({ index, label, onClick, onRemoveClick, isActive }: params) => {
  return (
    <StyledWrapper isActive={isActive}>
      <StyledRemoveButton icon={removeIcon} onClick={() => onRemoveClick()} />
      <StyledNavButton onClick={() => onClick()} noHover>
        {label}
      </StyledNavButton>
    </StyledWrapper>
  );
};

export default Tab;
