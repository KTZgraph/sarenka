import axios from 'axios';
import { serverRoutes } from 'routes';

export const actions: Record<string, string> = {
  FETCH_DATA_REQUEST: 'FETCH_HOST_INFO_REQUEST',
  FETCH_DATA_SUCCESS: 'FETCH_HOST_INFO_SUCCESS',
  FETCH_DATA_FAILURE: 'FETCH_HOST_INFO_FAILURE',
};

export const fetchData = (searchHost: string, tabIndex: number) => (
  dispatch: Function,
) => {
  dispatch({
    type: actions.FETCH_DATA_REQUEST,
    payload: {
      searchedHost: searchHost,
      tabIndex,
    },
  });

  return axios
    .get(`${serverRoutes.remoteHostData}${searchHost}`)
    .then(({ data }) => {
      dispatch({
        type: actions.FETCH_DATA_SUCCESS,
        payload: {
          searchedHost: searchHost,
          tabIndex,
          data,
        },
      });
    })
    .catch((err) => {
      dispatch({
        type: actions.FETCH_DATA_FAILURE,
        payload: {
          searchedHost: searchHost,
          tabIndex,
          error: err.message,
        },
      });
    });
};

export const fetchReport = (reportForIp: string) => {
  const URL = `${serverRoutes.remoteHostReport}${reportForIp}`;
  window.open(URL);
};
