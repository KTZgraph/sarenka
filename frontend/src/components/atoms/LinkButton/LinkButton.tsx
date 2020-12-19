import React from 'react';
import linkIcon from 'static/externalLinkIcon.svg';
import styled from 'styled-components';

const StyledLink = styled.a`
  display: inline-block;
  margin: 0 10px;
  transform: translateY(4px);
`;

type Props = {
  url: string;
};

const LinkButton: React.FC<Props> = ({ url }: Props) => (
  <StyledLink href={url} target="_blank" rel="noopener noreferrer">
    <img src={linkIcon} alt="External link." />
  </StyledLink>
);

export default LinkButton;
