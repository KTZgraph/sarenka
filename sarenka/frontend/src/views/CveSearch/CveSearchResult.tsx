import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchData, searchTypes } from 'actions/cveSearchActions';
import ResultTemplate from 'templates/VulnerabilityResultTemplate';
import SearchResultCVE from 'components/organisms/CveSearchResult/CveSearchResult';
import Loading from 'components/atoms/LoadingAnimation/LoadingAnimation';
import Search from 'components/molecules/Search/Search';
import Heading from 'components/atoms/Heading/Heading';
import { useParams } from 'react-router';
import Paragraph from 'components/atoms/Paragraph/Paragraph';
import { updateTabLabel } from 'actions/TabsActions';
import CweSearchResult from '../../components/organisms/CweSearchResult/CweSearchResult';

const CveSearchResult = () => {
  const dispatch = useDispatch();
  const { page } = useParams();
  const { isLoading, data, error, searchType } = useSelector(
    ({ cveSearch }: Record<string, any>) => cveSearch[page],
  );

  const [searchCve, setSearchCve] = useState(data?.cve || '');

  const handleSubmit = (
    event: React.FormEvent<HTMLFormElement>,
    searchWord: string,
  ) => {
    event.preventDefault();
    dispatch(fetchData(searchWord, page));
    dispatch(updateTabLabel(searchCve, page));
  };

  return (
    <>
      <ResultTemplate
        search={
          <Search
            handleSubmit={handleSubmit}
            searchWord={searchCve}
            setSearchWord={setSearchCve}
            title="Search information about specific CVE or CWE"
            placeholder="Type CVE or CWE number e.g CVE-2010-3333, CWE-246"
            pattern="((CVE|cve)-\d{4}-\d+)|((CWE|cwe)-\d+)"
          />
        }
        result={
          isLoading ? (
            <Loading />
          ) : (
            <>
              {JSON.stringify(data) !== '{}' && !error ? (
                searchTypes.CWE === searchType ? (
                  <CweSearchResult data={data} />
                ) : (
                  <SearchResultCVE
                    title={data.cwe?.[0]?.cwe_title}
                    cve={data.cve}
                    cwe={data.cwe?.[0]?.ID_CWE}
                    cweLink={data.cwe?.[0]?.cwe_mitre_url}
                    cvss2={data.cvss2?.cvss2}
                    cvss2link={data.cvss2?.cvss2_url}
                    cvss3={data.cvss3?.cvss3}
                    cvss3link={data.cvss3?.cvss3_url}
                    score={
                      data.base_score_v3
                        ? data.base_score_v3
                        : data.base_score_v2
                    }
                    publishedDate={data.published_date}
                    modificationDate={data.modified_date}
                    source={data.vulnerability_source}
                    hyperlinks={data.hyperlinks}
                    description={data.description}
                  />
                )
              ) : (
                <>
                  <Heading as="h3">No result found</Heading>
                  <Paragraph>{error}</Paragraph>
                </>
              )}
            </>
          )
        }
      />
    </>
  );
};

export default CveSearchResult;
