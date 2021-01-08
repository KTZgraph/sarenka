import axios from 'axios';
import UserCredentialsData from 'interfaces/UserCredentialsData';
import { serverRoutes } from '../routes';

export const getUserCredentials = () => {
  return axios.get(`${serverRoutes.userCredentials}`).then(({ data }) => {
    return data;
  });
};

export const setUserCredentials = (allCredentials: UserCredentialsData) => {
  const credentials = {
    'censys.api_id': allCredentials.censys.API_ID,
    'censys.secret': allCredentials.censys.Secret,
    'shodan.user': allCredentials.shodan.user,
    'shodan.api_key': allCredentials.shodan.api_key,
  };

  return axios
    .post(`${serverRoutes.userCredentials}`, credentials)
    .then(({ data }) => {
      return data;
    });
};
