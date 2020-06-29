import React, { useState } from 'react';
import styled from 'styled-components';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import TableItem from 'components/molecules/TableItem/TableItem';
import arrowSvg from 'static/arrow-right.svg';

const StyledTable = styled.table<{ visible: boolean }>`
  width: 100%;
  text-align: left;
  border-spacing: 0;
  display: ${({ visible }) => (visible ? 'block' : 'none')};
`;

const StyledTableHeader = styled.tr`
  & > th {
    padding: 10px;
    background-color: ${({ theme }) => theme.colors.redTransparent};
  }
  & > th:nth-child(1) {
    border-radius: 10px 0 0 0;
  }
  & > th:nth-last-child(1) {
    border-radius: 0 10px 0 0;
  }
`;

const StyledTableBody = styled.tbody`
  border-radius: 10px;
  & > tr:nth-child(even) {
    background: ${({ theme }) => theme.colors.darkGrey};
  }
`;

const StyledParagraph = styled(Paragraph)`
  word-break: break-all;
`;

const StyledShowResultButton = styled.button<{ rotate?: boolean }>`
  border: none;
  color: ${({ theme }) => theme.colors.font};
  cursor: pointer;
  margin-bottom: 15px;
  background: transparent;

  &::before {
    content: '';
    display: inline-block;
    width: 13px;
    height: 13px;
    margin-right: 5px;
    background: transparent url(${arrowSvg}) no-repeat 0 0;
    background-size: 15px 15px;
    transition: 0.3s;
    transform: ${({ rotate }) => (rotate ? 'rotateZ(90deg)' : 'rotateZ(0)')};
  }
`;

type Props = {
  searchLocation: string;
  softwares: Array<Record<string, string>>;
};

const InstalledSoftware: React.FC<Props> = ({
  searchLocation,
  softwares,
}: Props) => {
  const [showResults, setShowResults] = useState(false);
  return (
    <CardWrapper>
      <StyledParagraph>
        {`Search location: `}
        {searchLocation}
      </StyledParagraph>
      <StyledShowResultButton
        rotate={showResults}
        onClick={() => setShowResults(!showResults)}
      >
        Show search results
      </StyledShowResultButton>
      <StyledTable visible={showResults}>
        <thead>
          <StyledTableHeader>
            <Paragraph as="th">Name</Paragraph>
            <Paragraph as="th">Location</Paragraph>
            <Paragraph as="th">Version</Paragraph>
            <Paragraph as="th">Date</Paragraph>
            <Paragraph as="th">Vendor</Paragraph>
          </StyledTableHeader>
        </thead>
        <StyledTableBody>
          {softwares?.map(({ name, location, version, date, vendor }) => (
            <TableItem
              key={name}
              columns={[name, location, version, date, vendor]}
              wordBreak={1}
            />
          ))}
        </StyledTableBody>
      </StyledTable>
    </CardWrapper>
  );
};

export default InstalledSoftware;
