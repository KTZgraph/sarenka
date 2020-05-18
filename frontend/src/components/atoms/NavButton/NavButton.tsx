import styled from 'styled-components';

type Props = {
  icon?: any;
  iconActive?: any;
};

const NavButton = styled.button<Props>`
  display: block;
  text-decoration: none;
  background: transparent;
  border: none;
  padding: 0 0 0 64px;
  background-image: url(${({ icon }) => icon});
  background-size: 21px;
  background-position: 15px 50%;
  background-repeat: no-repeat;
  width: 100%;
  height: 40px;
  line-height: 40px;
  text-align: left;
  font-size: 1.4rem;
  letter-spacing: 0.3px;
  color: #e0e0e0;
  transition: 0.3s;

  &.active {
    background-image: url(${({ iconActive }) => iconActive});
    background-color: rgba(193, 12, 39, 0.52);
    border-radius: 4px;
    color: #ffffff;
  }
`;

export default NavButton;
