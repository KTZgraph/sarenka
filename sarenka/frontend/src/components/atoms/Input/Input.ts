import styled, { css } from 'styled-components';
import magnifierIcon from 'static/magnifierIconInput.svg';

type Props = {
  search?: boolean;
  noBorder?: boolean;
};

const Input = styled.input<Props>`
  height: 35px;
  max-width: 550px;
  width: 100%;
  padding-left: 10px;
  border-radius: 6px;
  font-size: 1.8rem;
  transition: 0.3s;
  border: ${({ noBorder }) => (noBorder ? `none` : `1px solid #c10c27`)};
  font-weight: ${({ theme }: Record<string, any>) => theme.font.weight.regular};

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
