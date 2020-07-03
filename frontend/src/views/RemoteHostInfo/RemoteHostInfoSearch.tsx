import React, { useEffect, useState } from 'react';
import VulnerabilityTemplate from 'templates/VulnerabilityTemplate';
import Search from 'components/molecules/Search/Search';
import { useHistory } from 'react-router-dom';
import routes from 'routes';
import { useDispatch, useSelector } from 'react-redux';
import { fetchData } from 'actions/remoteHostActions';

const RemoteHostInfoSearch = () => {
  const [searchHost, setSearchHost] = useState('');
  const history = useHistory();
  const dispatch = useDispatch();
  const { data } = useSelector(
    ({ remoteHost }: Record<string, any>) => remoteHost,
  );
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    dispatch(fetchData(searchHost));
    history.push(routes.remoteHostInfoResult);
  };

  useEffect(() => {
    if (JSON.stringify(data) !== '{}') {
      history.push(routes.remoteHostInfoResult);
    }
  }, [history, data]);

  return (
    <VulnerabilityTemplate>
      <Search
        name="searchHostInfo"
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
