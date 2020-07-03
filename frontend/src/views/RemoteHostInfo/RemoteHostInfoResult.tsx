import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import HTTPSInfo from 'components/molecules/HTTPSInfo/HTTPSInfo';
import ResultTemplate from 'templates/VulnerabilityResultTemplate';
import Search from 'components/molecules/Search/Search';
import { fetchData } from 'actions/remoteHostActions';
import LoadingAnimation from 'components/atoms/LoadingAnimation/LoadingAnimation';
import GeneralHostInfo from '../../components/molecules/GeneralHostInfo/GeneralHostInfo';
import TLSInfo from '../../components/molecules/TLSInfo/TLSInfo';

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
            <GeneralHostInfo
              protocolsPort={data.protocols_port}
              longitude={data.longitude}
              latitude={data.latitude}
              timezone={data.timezone}
              continent={data.continent}
              registeredCountry={data.registered_country}
              description={data.description}
              rir={data.rir}
              routedPrefix={data.routed_prefix}
              path={data.path}
              asn={data.asn}
              name={data.name}
              dnsNames={data.dns_names}
              dnsErrors={data.dns_errors}
              os={data.os}
              updatedAt={data.updated_at}
            />
            <HTTPSInfo httpsData={data.https} />
            {data.https?.tls?.chain?.map(
              (item: Record<string, any>, index: number) => (
                <TLSInfo tlsData={item} key={index} />
              ),
            )}
          </>
        )
      }
    />
  );
};

export default RemoteHostInfoResult;
