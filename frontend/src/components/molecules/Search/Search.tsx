import React from 'react';
import Heading from 'components/atoms/Heading/Heading';
import Input from 'components/atoms/Input/Input';
import logo from 'static/logo.svg';

type Props = {
  handleSubmit: Function;
  searchWord: string;
  setSearchWord: Function;
  placeholder: string;
  title: string;
  pattern?: string;
  name?: string;
};

const Search: React.FC<Props> = ({
  handleSubmit,
  searchWord,
  setSearchWord,
  placeholder,
  title,
  pattern,
  name = 'search',
}: Props) => {
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchWord(event.target.value);
  };
  return (
    <>
      <img src={logo} alt="App logo." />
      <Heading regularfont>{title}</Heading>
      <form onSubmit={(event) => handleSubmit(event, searchWord)}>
        <Input
          id={name}
          name={name}
          type="text"
          placeholder={placeholder}
          onChange={(event) => handleChange(event)}
          onBlur={(event) => handleChange(event)}
          search
          required
          pattern={pattern}
        />
      </form>
    </>
  );
};

export default Search;
