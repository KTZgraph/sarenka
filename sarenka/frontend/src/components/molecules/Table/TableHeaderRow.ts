import styled, { css } from 'styled-components';
import FromTop from 'components/animations/FromTop';

const TableHeaderRow = styled.tr<{ sticky?: boolean; animate?: boolean }>`
  & > th {
    ${({ sticky }) =>
      sticky &&
      css`
        position: sticky;
        top: 0;
        z-index: 1;
      `};
    ${({ animate }) =>
      animate &&
      css`
        opacity: 0;
        animation: ${FromTop} 0.2s ease-out forwards;
      `};
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
