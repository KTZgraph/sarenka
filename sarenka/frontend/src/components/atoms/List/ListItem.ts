import styled from 'styled-components';

const ListItem = styled.li`
  word-break: break-all;
  font-size: 1.7rem;
  color: #e0e0e0;
  font-weight: ${({ theme }) => theme.font.weight.regular};
  list-style: none;
  line-height: 2.3rem;
`;

export default ListItem;
