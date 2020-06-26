import React from 'react';
import styled from 'styled-components';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import TableItem from 'components/molecules/TableItem/TableItem';

const StyledTable = styled.table`
  width: 100%;
  text-align: left;
  padding: 0 30px;
  border-spacing: 0;

  & > tbody {
    border: 1px solid ${({ theme }) => theme.colors.grey};
    border-radius: 20px;
  }
`;

type Props = {
  searchLocation: string;
  softwares: Array<Record<string, string>>;
};

const InstalledSoftware: React.FC<Props> = ({
  searchLocation,
  softwares,
}: Props) => (
  <CardWrapper>
    <StyledTable>
      <thead>
        <tr>
          <Paragraph>
            Search location:
            {searchLocation}
          </Paragraph>
        </tr>
        <tr>
          <Paragraph as="th">Name</Paragraph>
          <Paragraph as="th">Location</Paragraph>
          <Paragraph as="th">Version</Paragraph>
          <Paragraph as="th">Date</Paragraph>
          <Paragraph as="th">Vendor</Paragraph>
        </tr>
      </thead>
      <tbody>
        {softwares?.map(({ name, location, version, date, vendor }) => (
          <TableItem
            key={name}
            columns={[name, location, version, date, vendor]}
          />
        ))}
      </tbody>
    </StyledTable>
  </CardWrapper>
);

export default InstalledSoftware;
