import React from 'react';
import Heading from 'components/atoms/Heading/Heading';
import logo from 'static/logo.svg';
import SettingsTemplate from 'templates/SettingsTemplate';
import styled from 'styled-components';
import InputWithLabel from 'components/atoms/InputWithLabel/InputWithLabel';
import Button from 'components/atoms/Button/Button';
import Input from '../../components/atoms/Input/Input';

const StyledTokensWrapper = styled.section`
  margin-left: 40px;
`;

const StyledForm = styled.form`
  margin-left: 20px;
`;

const SettingsView = () => {
  const allKeys = {
    censys_API_ID: '',
    censys_Secret: '',
    shodan_user: '',
    shodan_api_key: '',
  };

  const onSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
  };

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
            defaultValue={allKeys.censys_API_ID}
            onChange={(
              event:
                | React.ChangeEvent<HTMLInputElement>
                | React.FocusEvent<HTMLInputElement>,
            ) => {
              allKeys.censys_API_ID = event.target.value;
            }}
          />
          <InputWithLabel
            name="censysSecret"
            label="censys.io"
            placeholder="Type here your key"
            defaultValue={allKeys.censys_Secret}
            onChange={(
              event:
                | React.ChangeEvent<HTMLInputElement>
                | React.FocusEvent<HTMLInputElement>,
            ) => {
              allKeys.censys_Secret = event.target.value;
            }}
          />
          <InputWithLabel
            name="shodanUser"
            label="shodan.io"
            placeholder="Type here your username"
            defaultValue={allKeys.shodan_user}
            onChange={(
              event:
                | React.ChangeEvent<HTMLInputElement>
                | React.FocusEvent<HTMLInputElement>,
            ) => {
              allKeys.shodan_user = event.target.value;
            }}
          />
          <InputWithLabel
            name="shodanAPIKEY"
            label="shodan.io"
            placeholder="Type here your API key"
            defaultValue={allKeys.shodan_api_key}
            onChange={(
              event:
                | React.ChangeEvent<HTMLInputElement>
                | React.FocusEvent<HTMLInputElement>,
            ) => {
              allKeys.shodan_api_key = event.target.value;
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
