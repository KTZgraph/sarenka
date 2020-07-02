import styled from 'styled-components';

const TableBody = styled.tbody`
  & > tr:nth-child(even) {
    background: ${({ theme }) => theme.colors.darkGrey};
  }
`;

export default TableBody;
