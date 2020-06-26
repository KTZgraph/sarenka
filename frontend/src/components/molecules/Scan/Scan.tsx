import React from 'react';
import logo from 'static/logo.svg';
import Heading from 'components/atoms/Heading/Heading';
import Button from 'components/atoms/Button/Button';

type Props = {
  title: string;
  onButtonClick: () => void;
};

const Scan: React.FC<Props> = ({ title, onButtonClick }: Props) => {
  return (
    <>
      <img src={logo} alt="App logo." />
      <Heading regularfont>{title}</Heading>
      <Button onClick={onButtonClick}>Scan</Button>
    </>
  );
};

export default Scan;
