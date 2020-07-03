import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import SSLInfo from 'components/molecules/SSLInfo/SSLInfo';
import ResultTemplate from 'templates/VulnerabilityResultTemplate';
import Search from 'components/molecules/Search/Search';
import { fetchData } from 'actions/remoteHostActions';
import LoadingAnimation from 'components/atoms/LoadingAnimation/LoadingAnimation';

const RemoteHostInfoResult = () => {
  const [searchHost, setSearchHost] = useState('');
  const dispatch = useDispatch();
  const { isLoading, data } = useSelector(
    ({ remoteHost }: Record<string, any>) => remoteHost,
  );
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    dispatch(fetchData(searchHost));
  };
  return (
    <ResultTemplate
      search={
        <Search
          name="searchHostInfo"
          handleSubmit={handleSubmit}
          searchWord={searchHost}
          setSearchWord={setSearchHost}
          title="Search for errors on your domain"
          placeholder="Type host address e.g. 8.8.8.8"
        />
      }
      result={
        isLoading ? (
          <LoadingAnimation />
        ) : (
          <>
            <SSLInfo httpsData={data.https} />
          </>
        )
      }
    />
  );
};

export default RemoteHostInfoResult;
