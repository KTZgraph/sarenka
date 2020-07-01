import styled from 'styled-components';

const TableHeaderRow = styled.tr<{ sticky?: boolean }>`
  & > th {
    ${({ sticky }) => sticky && `position: sticky`};
    ${({ sticky }) => sticky && `top: 0`};
    padding: 10px;
    background: ${({ theme }) => theme.colors.redDarker};
  }
  & > th:nth-child(1) {
    border-radius: 10px 0 0 0;
  }
  & > th:nth-last-child(1) {
    border-radius: 0 10px 0 0;
  }
`;

export default TableHeaderRow;
