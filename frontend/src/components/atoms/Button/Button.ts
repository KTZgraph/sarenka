import styled from 'styled-components';

const Button = styled.button`
  color: ${({ theme }) => theme.colors.font};
  background: ${({ theme }) => theme.colors.red};
  border: none;
  border-radius: 5px;
  padding: 15px 40px;
`;

export default Button;
