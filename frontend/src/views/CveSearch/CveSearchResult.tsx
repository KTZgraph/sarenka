import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import routes from 'routes';
import { fetchData } from 'actions/cveSearchActions';
import ResultTemplate from 'templates/VulnerabilityResultTemplate';
import SearchResult from 'components/organisms/CveSearchResult/CveSearchResult';
import Loading from 'components/atoms/LoadingAnimation/LoadingAnimation';
import Search from 'components/molecules/Search/Search';
import Heading from 'components/atoms/Heading/Heading';

const CveSearchResult = () => {
  const dispatch = useDispatch();
  const history = useHistory();

  const { isLoading, data } = useSelector(
    ({ cveSearch }: Record<string, any>) => cveSearch,
  );

  const [searchCve, setSearchCve] = useState(data.cve || '');

  const handleSubmit = (
    event: React.FormEvent<HTMLFormElement>,
    searchWord: string,
  ) => {
    event.preventDefault();
    dispatch(fetchData(searchWord));
    history.push(routes.cveSearchResults);
  };

  return (
    <>
      <ResultTemplate
        search={
          <Search
            handleSubmit={handleSubmit}
            searchWord={searchCve}
            setSearchWord={setSearchCve}
            title="Search information about specific CVE"
            placeholder="Type CVE number e.g CVE-2010-3333"
            pattern="(CVE|cve)-\d{4}-\d+"
          />
        }
        result={
          isLoading ? (
            <Loading />
          ) : (
            <>
              {JSON.stringify(data) !== '{}' ? (
                <SearchResult
                  title={data.title}
                  cve={data.cve}
                  cwe={data.cwe}
                  cvssvector={data.cvss_vector}
                  complexity={data.complexity}
                  auth={data.authentication}
                  score={data.cvss}
                  availability={data.availability}
                  confidentiality={data.confidentiality}
                  products={data.products}
                />
              ) : (
                <Heading as="h3">No result found</Heading>
              )}
            </>
          )
        }
      />
    </>
  );
};

export default CveSearchResult;
