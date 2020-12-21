import styled from 'styled-components';

const Checkbox = styled.input`
  position: relative;
  display: inline-block;
  appearance: none;
  cursor: pointer;
  margin: 0 20px;
  width: 45px;
  height: 25px;
  background-color: #787878;
  border: 1px solid #787878;
  border-radius: 50px;
  transition-duration: 0.2s;
  vertical-align: middle;

  &::after {
    content: '';
    display: inline-block;
    position: absolute;
    top: 1px;
    left: 1px;
    background-color: #ffffff;
    width: 21px;
    height: 21px;
    border-radius: 50%;
    transform: translateX(0);
    transition: 0.2s;
  }

  &:checked {
    border-color: #c10c27;
    background-color: #c10c27;
  }

  &:checked::after {
    transform: translateX(95%);
  }
`;

export default Checkbox;
