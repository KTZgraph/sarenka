import React from 'react';
import { useSelector } from 'react-redux';
import ResultTemplate from 'templates/VulnerabilityResultTemplate';
import Loading from 'components/atoms/LoadingAnimation/LoadingAnimation';
import Heading from 'components/atoms/Heading/Heading';
import logo from 'static/logo.svg';
import InstalledSoftware from 'components/organisms/InstalledSoftware/InstalledSoftware';
import { useParams } from 'react-router';

type scanResult = {
  key: string;
  softwares: Array<Record<string, string>>;
};

const RegistryScanResults = () => {
  const { page } = useParams();
  const { isLoading, data } = useSelector(
    ({ registryScan }: Record<string, any>) => registryScan[page],
  );

  return (
    <>
      <ResultTemplate
        search={<img src={logo} alt="App logo." />}
        result={
          isLoading ? (
            <Loading />
          ) : (
            <>
              {JSON.stringify(data) !== '{}' ? (
                <>
                  {data.map(({ key, softwares }: scanResult) => (
                    <InstalledSoftware
                      key={key}
                      searchLocation={key}
                      softwares={softwares}
                    />
                  ))}
                </>
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

export default RegistryScanResults;
