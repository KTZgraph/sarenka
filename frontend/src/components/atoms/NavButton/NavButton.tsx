import styled from 'styled-components';

type Props = {
  icon?: any;
  iconactive?: any;
};

const NavButton = styled.button<Props>`
  display: block;
  text-decoration: none;
  border: none;
  padding: 0 0 0 64px;
  background: transparent url(${({ icon }) => icon}) no-repeat 15px 50%;
  background-size: 21px;
  width: 100%;
  height: 40px;
  line-height: 40px;
  text-align: left;
  font-size: 1.4rem;
  letter-spacing: 0.3px;
  color: #e0e0e0;
  transition: 0.3s;

  &.active {
    background-image: url(${({ iconactive }) => iconactive});
    background-color: rgba(193, 12, 39, 0.52);
    border-radius: 4px;
    color: #ffffff;
  }
`;

export default NavButton;
