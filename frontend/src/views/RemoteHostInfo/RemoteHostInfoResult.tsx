import React, { useState } from 'react';
import SSLInfo from 'components/molecules/SSLInfo/SSLInfo';
import ResultTemplate from 'templates/VulnerabilityResultTemplate';
import Search from 'components/molecules/Search/Search';

const RemoteHostInfoResult = () => {
  const [searchHost, setSearchHost] = useState('');

  const handleSubmit = (
    event: React.FormEvent<HTMLFormElement>,
    searchWord: string,
  ) => {
    event.preventDefault();
    console.log(event, searchWord);
  };
  return (
    <ResultTemplate
      search={
        <Search
          handleSubmit={handleSubmit}
          searchWord={searchHost}
          setSearchWord={setSearchHost}
          title="Search for errors on your domain"
          placeholder="Type website address"
        />
      }
      result={
        <>
          <SSLInfo host="test" />
        </>
      }
    />
  );
};

export default RemoteHostInfoResult;
