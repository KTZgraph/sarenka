import styled, { css } from 'styled-components';

type Props = {
  small?: boolean;
  displayBlock?: boolean;
};

const Button = styled.button<Props>`
  color: ${({ theme }) => theme.colors.font};
  background: ${({ theme }) => theme.colors.red};
  border: none;
  border-radius: 5px;
  padding: 15px 40px;
  cursor: pointer;
  display: ${({ displayBlock }) => (displayBlock ? `block` : `inline-block`)};

  ${({ small }) =>
    small &&
    css`
      max-width: 120px;
      max-height: 80px;
      padding: 10px;
      transform: translateY(25%);
    `}
`;

export const ButtonAlignToRight = styled.div`
  display: grid;
  justify-items: end;
  width: 100%;
`;

export default Button;
