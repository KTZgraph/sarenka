import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import HTTPSInfo from 'components/molecules/HTTPSInfo/HTTPSInfo';
import ResultTemplate from 'templates/VulnerabilityResultTemplate';
import Search from 'components/molecules/Search/Search';
import { fetchData, fetchReport } from 'actions/remoteHostActions';
import LoadingAnimation from 'components/atoms/LoadingAnimation/LoadingAnimation';
import { useParams } from 'react-router';
import GeneralHostInfo from 'components/molecules/GeneralHostInfo/GeneralHostInfo';
import TLSInfo from 'components/molecules/TLSInfo/TLSInfo';
import Button, { ButtonAlignToRight } from 'components/atoms/Button/Button';
import { updateTabLabel } from 'actions/TabsActions';

const RemoteHostInfoResult = () => {
  const [searchHost, setSearchHost] = useState('');
  const { page } = useParams();
  const dispatch = useDispatch();
  const {
    isLoading,
    data,
    searchedHost,
  } = useSelector(({ remoteHost }: Record<string, any>) =>
    remoteHost[page]
      ? remoteHost[page]
      : { isLoading: true, data: {}, searchedHost: '' },
  );
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    dispatch(fetchData(searchHost, page));
    dispatch(updateTabLabel(searchHost, page));
  };

  const handleReportGenerate = () => {
    return fetchReport(searchHost);
  };

  useEffect(() => {
    setSearchHost(searchedHost);
  }, [searchedHost]);

  return (
    <ResultTemplate
      search={
        <Search
          name="searchHostInfo"
          handleSubmit={handleSubmit}
          searchWord={searchHost}
          setSearchWord={setSearchHost}
          title="Passive reconnaissance data from your's host"
          placeholder="Type host address e.g. 8.8.8.8"
        />
      }
      result={
        isLoading ? (
          <LoadingAnimation />
        ) : (
          <>
            <ButtonAlignToRight>
              <Button onClick={handleReportGenerate} small>
                Generate report
              </Button>
            </ButtonAlignToRight>
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
