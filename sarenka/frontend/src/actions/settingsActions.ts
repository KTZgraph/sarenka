import axios from 'axios';
import UserCredentialsData from 'interfaces/UserCredentialsData';
import { serverRoutes } from '../routes';

export const getUserCredentials = () => {
  return axios.get(`${serverRoutes.userCredentials}`).then(({ data }) => {
    return data;
  });
};

export const setUserCredentials = (credentials: UserCredentialsData) => {
  return axios
    .post(`${serverRoutes.userCredentials}`, credentials)
    .then(({ data }) => {
      return data;
    });
};
