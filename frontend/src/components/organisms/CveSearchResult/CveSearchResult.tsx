import React from 'react';
import styled from 'styled-components';
import CardWrapper from 'components/atoms/CardWrapper/CardWrapper';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import LinkButton from 'components/atoms/LinkButton/LinkButton';
import NoData from 'components/atoms/NoDataText/NoDataText';

const StyledParagraphRedBorder = styled(Paragraph)`
  max-width: 180px;
  padding: 10px;
  background: #c10c274f;
  transform: translate(-10px, -10px);
  border-radius: 4px;
  white-space: nowrap;
  display: inline-block;
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

const StyledParagraph = styled(Paragraph)`
  white-space: nowrap;
  margin-right: 10px;
`;

const StyledLink = styled(Paragraph)`
  display: block;
  margin-top: 5px;
`;

type Props = {
  title: string;
  cve: string;
  cwe: string;
  cvss2: string;
  cvss2link: string;
  cvss3: string;
  cvss3link: string;
  score: string;
  publishedDate: string;
  modificationDate: string;
  source: string;
  hyperlinks: string[];
  cweLink: string;
};

const CveSearchResult: React.FC<Props> = ({
  title,
  cve,
  cwe,
  cvss2,
  cvss2link,
  cvss3,
  cvss3link,
  score,
  publishedDate,
  modificationDate,
  source,
  hyperlinks,
  cweLink,
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
          {cweLink && <LinkButton url={cweLink} />}
        </Paragraph>
        <StyledParagraph>
          <strong>CVSS 2.0: </strong>
          {cvss2 || <NoData />}
          {cvss2link?.includes('http') && <LinkButton url={cvss2link} />}
        </StyledParagraph>
        <StyledParagraph>
          <strong>CVSS 3.0: </strong>
          {cvss3 || <NoData />}
          {cvss3link?.includes('http') && <LinkButton url={cvss3link} />}
        </StyledParagraph>
        <div>
          <StyledParagraphRedBorder>
            <strong>Score: </strong>
            {score}
          </StyledParagraphRedBorder>
        </div>
        <Paragraph>
          <strong>Published date: </strong>
          {publishedDate}
        </Paragraph>
        <Paragraph>
          <strong>Modification date: </strong>
          {modificationDate}
        </Paragraph>
        <Paragraph>
          <strong>Source: </strong>
          {source}
        </Paragraph>
      </StyledInnerWrapper>
      <Paragraph>
        <strong>Description: </strong>
        {title}
      </Paragraph>
      <Paragraph>
        <strong>Useful links: </strong>
        {hyperlinks.map((link, index) => {
          return (
            <StyledLink
              key={index}
              as="a"
              href={link}
              target="_blank"
              rel="noopener noreferrer"
            >
              {link}
            </StyledLink>
          );
        })}
      </Paragraph>
    </CardWrapper>
  );
};

export default CveSearchResult;
