import React, { useEffect, useRef, useState } from 'react';
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
import gsap from 'gsap';

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

  useEffect(() => {
    if (tableBodyRef.current !== null && tableHeaderRef.current !== null) {
      gsap.set([tableHeaderRef.current, ...tableBodyRef.current.children], {
        autoAlpha: 0,
      });
      const tableAnimation = gsap
        .fromTo(
          [tableHeaderRef.current, ...tableBodyRef.current.children],
          { y: '-50', autoAlpha: 0 },
          { duration: 0.2, y: '0', autoAlpha: 1, delay: 0.2, stagger: 0.1 },
        )
        .pause();
      if (showResults) {
        tableAnimation.play();
      } else if (!showResults) {
        tableAnimation.reverse();
      }
    }
  }, [tableBodyRef, showResults]);
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
          <TableHeaderRow ref={tableHeaderRef}>
            <Paragraph as="th">Name</Paragraph>
            <Paragraph as="th">Location</Paragraph>
            <Paragraph as="th">Version</Paragraph>
            <Paragraph as="th">Date</Paragraph>
            <Paragraph as="th">Vendor</Paragraph>
          </TableHeaderRow>
        </thead>
        <TableBody ref={tableBodyRef}>
          {softwares?.map(({ name, location, version, date, vendor }) => (
            <TableItem
              key={name}
              columns={[name, location, version, date, vendor]}
              wordBreak={1}
            />
          ))}
        </TableBody>
      </Table>
    </CardWrapper>
  );
};

export default InstalledSoftware;
