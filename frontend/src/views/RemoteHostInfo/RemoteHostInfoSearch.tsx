import React, { useState } from 'react';
import VulnerabilityTemplate from 'templates/VulnerabilityTemplate';
import Search from 'components/molecules/Search/Search';
import { useHistory } from 'react-router-dom';
import routes from 'routes';

const RemoteHostInfoSearch = () => {
  const [searchHost, setSearchHost] = useState('');
  const history = useHistory();
  const handleSubmit = (
    event: React.FormEvent<HTMLFormElement>,
    searchWord: string,
  ) => {
    event.preventDefault();
    history.push(routes.frontendResults);
    console.log(event, searchWord);
  };

  return (
    <VulnerabilityTemplate>
      <Search
        handleSubmit={handleSubmit}
        searchWord={searchHost}
        setSearchWord={setSearchHost}
        title="Search for errors on remote domain"
        placeholder="Type host address e.g. 8.8.8.8"
      />
    </VulnerabilityTemplate>
  );
};

export default RemoteHostInfoSearch;
