import React, { useState } from 'react';
import VulnerabilityTemplate from 'templates/VulnerabilityTemplate';
import Search from 'components/molecules/Search/Search';
import { useHistory } from 'react-router-dom';
import routes, { routesWithoutTab } from 'routes';
import { useDispatch } from 'react-redux';
import { fetchData } from 'actions/remoteHostActions';
import { useParams } from 'react-router';
import { updateTabUrl } from 'actions/TabsActions';

const RemoteHostInfoSearch = () => {
  const [searchHost, setSearchHost] = useState('');
  const { page } = useParams();
  const history = useHistory();
  const dispatch = useDispatch();

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    dispatch(fetchData(searchHost, page));
    dispatch(updateTabUrl(routesWithoutTab.remoteHostInfoResult, page));
    history.push(
      `${routes.tabsWOpage}${page}${routesWithoutTab.remoteHostInfoResult}`,
    );
  };

  return (
    <VulnerabilityTemplate>
      <Search
        name="searchHostInfo"
        handleSubmit={handleSubmit}
        searchWord={searchHost}
        setSearchWord={setSearchHost}
        title="Passive reconnaissance data from your's host"
        placeholder="Type host address e.g. 8.8.8.8"
      />
    </VulnerabilityTemplate>
  );
};

export default RemoteHostInfoSearch;
