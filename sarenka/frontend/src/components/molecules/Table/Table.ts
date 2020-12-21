import styled from 'styled-components';

const Table = styled.table<{ visible?: boolean }>`
  position: relative;
  border-collapse: collapse;
  width: 100%;
  text-align: left;
  border-spacing: 0;
  display: ${({ visible = true }) => (visible ? 'table' : 'none')};
`;

export default Table;
