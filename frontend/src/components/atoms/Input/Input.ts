import styled, { css } from 'styled-components';
import magnifierIcon from 'static/magnifierIcon.svg';

type Props = {
  search?: boolean;
};

const Input = styled.input<Props>`
  height: 34px;
  max-width: 550px;
  width: 100%;
  padding-left: 10px;
  border: none;
  border-radius: 6px;
  font-size: 1.8rem;
  transition: 0.3s;
  border: 1px solid #c10c27;
  font-weight: ${({ theme }: Record<string, any>) => theme.font.weight.medium};

  ${({ search }) =>
    search &&
    css`
      padding: 0 0 0 34px;
      background-image: url(${magnifierIcon});
      background-size: 34px;
      background-position: 0 50%;
      background-repeat: no-repeat;
    `}
`;

export default Input;
