import React from 'react';
import styled from 'styled-components';
import Paragraph from 'components/atoms/Paragraph/Paragraph';

const StyledWrapper = styled.tr`
  list-style: none;
  padding: 10px 0;
  width: 90%;

  & > td {
    border-bottom: 1px solid ${({ theme }) => theme.colors.grey};
  }
`;

type Props = {
  vendor: string;
  name: string;
  version: string;
  system: string;
};

const CveSearchListItem: React.FC<Props> = ({
  vendor,
  name,
  version,
  system,
}: Props) => (
  <StyledWrapper>
    <td>
      <Paragraph>{vendor}</Paragraph>
    </td>
    <td>
      <Paragraph>{name}</Paragraph>
    </td>
    <td>
      <Paragraph>{version}</Paragraph>
    </td>
    <td>
      <Paragraph>{system}</Paragraph>
    </td>
  </StyledWrapper>
);

export default CveSearchListItem;
