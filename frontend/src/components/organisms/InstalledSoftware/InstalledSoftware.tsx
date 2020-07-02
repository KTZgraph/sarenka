import React, { useRef, useState } from 'react';
import styled from 'styled-components';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import arrowSvg from 'static/arrow-right.svg';
import {
  Table,
  TableBody,
  TableHeaderRow,
  TableItem,
} from 'components/molecules/Table';

const StyledParagraph = styled(Paragraph)`
  word-break: break-all;
`;

const StyledShowResultButton = styled.button<{ shouldRotate?: boolean }>`
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
    transform: ${({ shouldRotate }) =>
      shouldRotate ? 'rotateZ(90deg)' : 'rotateZ(0)'};
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

  const tableBodyRef = useRef<HTMLTableSectionElement>(null);
  const tableHeaderRef = useRef<HTMLTableRowElement>(null);

  return (
    <CardWrapper>
      <StyledParagraph>
        {`Search location: `}
        {searchLocation}
      </StyledParagraph>
      <StyledShowResultButton
        shouldRotate={showResults}
        onClick={() => setShowResults(!showResults)}
      >
        Show search results
      </StyledShowResultButton>
      <Table visible={showResults}>
        <thead>
          <TableHeaderRow ref={tableHeaderRef} sticky animate>
            <Paragraph as="th">Name</Paragraph>
            <Paragraph as="th">Location</Paragraph>
            <Paragraph as="th">Version</Paragraph>
            <Paragraph as="th">Date</Paragraph>
            <Paragraph as="th">Vendor</Paragraph>
          </TableHeaderRow>
        </thead>
        <TableBody ref={tableBodyRef}>
          {softwares?.map(
            ({ name, location, version, date, vendor }, index) => (
              <TableItem
                key={name}
                columns={[name, location, version, date, vendor]}
                wordBreak={1}
                delay={(index + 1) / 10}
              />
            ),
          )}
        </TableBody>
      </Table>
    </CardWrapper>
  );
};

export default InstalledSoftware;
