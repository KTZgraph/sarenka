import React from 'react';
import styled from 'styled-components';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import {
  Table,
  TableBody,
  TableHeaderRow,
  TableItem,
} from 'components/molecules/Table';

const StyledParagraphRedBorder = styled(Paragraph)`
  max-width: 110px;
  padding: 10px;
  background: #c10c274f;
  transform: translate(-10px, -10px);
  border-radius: 4px;
`;

const StyledInnerWrapper = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  @media (max-width: 930px) {
    grid-template-columns: repeat(2, 1fr);
  }
  @media (max-width: 540px) {
    grid-template-columns: repeat(1, 1fr);
  }
`;

type Props = {
  title: string;
  cve: string;
  cwe: string;
  cvssvector: string;
  complexity: string;
  auth: string;
  score: string;
  availability: string;
  confidentiality: string;
  products: {
    vendor: string;
    name: string;
    version: string;
    system: string;
  }[];
};

const CveSearchResult: React.FC<Props> = ({
  title,
  cve,
  cwe,
  cvssvector,
  complexity,
  auth,
  score,
  availability,
  confidentiality,
  products,
}: Props) => {
  return (
    <CardWrapper>
      <StyledInnerWrapper>
        <Paragraph>
          <strong>Title: </strong>
          {title}
        </Paragraph>
        <Paragraph>
          <strong>CVE: </strong>
          {cve}
        </Paragraph>
        <Paragraph>
          <strong>CWE: </strong>
          {cwe}
        </Paragraph>
        <Paragraph>
          <strong>CVSS Vector: </strong>
          {cvssvector}
        </Paragraph>
        <Paragraph>
          <strong>Complexity: </strong>
          {complexity}
        </Paragraph>
        <Paragraph>
          <strong>Authentication: </strong>
          {auth}
        </Paragraph>
        <Paragraph>
          <strong>Availability: </strong>
          {availability}
        </Paragraph>
        <Paragraph>
          <strong>Confidentiality: </strong>
          {confidentiality}
        </Paragraph>
        <StyledParagraphRedBorder>
          <strong>Score: </strong>
          {score}
        </StyledParagraphRedBorder>
      </StyledInnerWrapper>
      <Paragraph>Products</Paragraph>
      <Table>
        <thead>
          <TableHeaderRow>
            <Paragraph as="th">Vendor</Paragraph>
            <Paragraph as="th">Name</Paragraph>
            <Paragraph as="th">Version</Paragraph>
            <Paragraph as="th">System</Paragraph>
          </TableHeaderRow>
        </thead>
        <TableBody>
          {products?.map(({ vendor, name, version, system }, index) => (
            <TableItem
              key={index}
              columns={[vendor, name, version, system]}
              wordBreak={1}
            />
          ))}
        </TableBody>
      </Table>
    </CardWrapper>
  );
};

export default CveSearchResult;
