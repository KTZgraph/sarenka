import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import routes, { routesWithoutTab } from 'routes';
import { fetchData } from 'actions/cveSearchActions';
import VulnerabilityTemplate from 'templates/VulnerabilityTemplate';
import Search from 'components/molecules/Search/Search';
import { useParams } from 'react-router';
import { updateTabUrl } from 'actions/TabsActions';

const CveSearch = () => {
  const [searchCve, setSearchCve] = useState('');
  const dispatch = useDispatch();
  const { page } = useParams();
  const history = useHistory();

  const handleSubmit = (
    event: React.FormEvent<HTMLFormElement>,
    searchWord: string,
  ) => {
    event.preventDefault();
    dispatch(fetchData(searchWord, page));
    dispatch(updateTabUrl(routesWithoutTab.cveSearchResults, page, searchCve));
    history.push(
      `${routes.tabsWOpage}${page}${routesWithoutTab.cveSearchResults}`,
    );
  };

  return (
    <VulnerabilityTemplate>
      <Search
        handleSubmit={handleSubmit}
        searchWord={searchCve}
        setSearchWord={setSearchCve}
        title="Search information about specific CVE or CWE"
        placeholder="Type CVE or CWE number e.g CVE-2010-3333, CWE-246"
        pattern="((CVE|cve)-\d{4}-\d+)|((CWE|cwe)-\d+)"
      />
    </VulnerabilityTemplate>
  );
};

export default CveSearch;
