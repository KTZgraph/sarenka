import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import routes from 'routes';
import { fetchData } from 'actions/cveSearchActions';
import VulnerabilityTemplate from 'templates/VulnerabilityTemplate';
import Search from 'components/molecules/Search/Search';

const CveSearch = () => {
  const [searchCve, setSearchCve] = useState('');
  const dispatch = useDispatch();
  const history = useHistory();
  const { data } = useSelector(
    ({ cveSearch }: Record<string, any>) => cveSearch,
  );

  const handleSubmit = (
    event: React.FormEvent<HTMLFormElement>,
    searchWord: string,
  ) => {
    event.preventDefault();
    dispatch(fetchData(searchWord));
    history.push(routes.cveSearchResults);
  };

  useEffect(() => {
    if (JSON.stringify(data) !== '{}') {
      history.push(routes.cveSearchResults);
    }
  }, [data, history]);

  return (
    <VulnerabilityTemplate>
      <Search
        handleSubmit={handleSubmit}
        searchWord={searchCve}
        setSearchWord={setSearchCve}
        title="Search infromation about specific CVE"
        placeholder="Type CVE number e.g CVE-2010-3333"
        pattern="(CVE|cve)-\d{4}-\d+"
      />
    </VulnerabilityTemplate>
  );
};

export default CveSearch;
