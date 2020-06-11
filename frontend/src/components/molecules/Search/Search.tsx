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
};

const Search: React.FC<Props> = ({
  handleSubmit,
  searchWord,
  setSearchWord,
  placeholder,
  title,
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
          id="search"
          name="search"
          type="text"
          placeholder={placeholder}
          onChange={(event) => handleChange(event)}
          onBlur={(event) => handleChange(event)}
          search
          required
        />
      </form>
    </>
  );
};

export default Search;
