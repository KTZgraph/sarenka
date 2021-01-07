import React, { useEffect, useState } from 'react';
import Heading from 'components/atoms/Heading/Heading';
import logo from 'static/logo.svg';
import SettingsTemplate from 'templates/SettingsTemplate';
import styled from 'styled-components';
import InputWithLabel from 'components/atoms/InputWithLabel/InputWithLabel';
import Button from 'components/atoms/Button/Button';
import {
  getUserCredentials,
  setUserCredentials,
} from 'actions/settingsActions';
import UserCredentialsData from 'interfaces/UserCredentialsData';

const StyledTokensWrapper = styled.section`
  margin-left: 40px;
`;

const StyledForm = styled.form`
  margin-left: 20px;
`;

const SettingsView = () => {
  const [allCredentials, setAllCredentials] = useState<UserCredentialsData>({
    censys_API_ID: '',
    censys_Secret: '',
    shodan_user: '',
    shodan_api_key: '',
  });

  const onSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setUserCredentials(allCredentials).then(
      (credentials: UserCredentialsData) => {
        setAllCredentials(credentials);
      },
    );
  };

  useEffect(() => {
    getUserCredentials().then((credentials: UserCredentialsData) => {
      setAllCredentials(credentials);
    });
  }, []);

  return (
    <SettingsTemplate logo={<img src={logo} alt="App logo." />}>
      <Heading regularfont bigFont>
        Settings
      </Heading>
      <StyledTokensWrapper>
        <Heading as="h2" regularfont>
          Type your API tokens
        </Heading>
        <StyledForm onSubmit={(event) => onSubmit(event)}>
          <InputWithLabel
            name="censysAPIID"
            label="censys.io"
            placeholder="Type here your API ID"
            defaultValue={allCredentials.censys_API_ID}
            onChange={(
              event:
                | React.ChangeEvent<HTMLInputElement>
                | React.FocusEvent<HTMLInputElement>,
            ) => {
              setAllCredentials({
                censys_API_ID: event.target.value,
                censys_Secret: allCredentials.censys_Secret,
                shodan_user: allCredentials.shodan_user,
                shodan_api_key: allCredentials.shodan_api_key,
              });
            }}
          />
          <InputWithLabel
            name="censysSecret"
            label="censys.io"
            placeholder="Type here your key"
            defaultValue={allCredentials.censys_Secret}
            onChange={(
              event:
                | React.ChangeEvent<HTMLInputElement>
                | React.FocusEvent<HTMLInputElement>,
            ) => {
              setAllCredentials({
                censys_API_ID: allCredentials.censys_API_ID,
                censys_Secret: event.target.value,
                shodan_user: allCredentials.shodan_user,
                shodan_api_key: allCredentials.shodan_api_key,
              });
            }}
          />
          <InputWithLabel
            name="shodanUser"
            label="shodan.io"
            placeholder="Type here your username"
            defaultValue={allCredentials.shodan_user}
            onChange={(
              event:
                | React.ChangeEvent<HTMLInputElement>
                | React.FocusEvent<HTMLInputElement>,
            ) => {
              setAllCredentials({
                censys_API_ID: allCredentials.censys_API_ID,
                censys_Secret: allCredentials.censys_Secret,
                shodan_user: event.target.value,
                shodan_api_key: allCredentials.shodan_api_key,
              });
            }}
          />
          <InputWithLabel
            name="shodanAPIKEY"
            label="shodan.io"
            placeholder="Type here your API key"
            defaultValue={allCredentials.shodan_api_key}
            onChange={(
              event:
                | React.ChangeEvent<HTMLInputElement>
                | React.FocusEvent<HTMLInputElement>,
            ) => {
              setAllCredentials({
                censys_API_ID: allCredentials.censys_API_ID,
                censys_Secret: allCredentials.censys_Secret,
                shodan_user: allCredentials.shodan_user,
                shodan_api_key: event.target.value,
              });
            }}
          />
          <Button type="submit" small displayBlock>
            Update tokens
          </Button>
        </StyledForm>
      </StyledTokensWrapper>
    </SettingsTemplate>
  );
};

export default SettingsView;
