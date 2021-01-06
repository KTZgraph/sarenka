import axios from 'axios';
import { serverRoutes } from 'routes';

export enum actions {
  FETCH_DATA_REQUEST = 'FETCH_DATA_REQUEST',
  FETCH_DATA_SUCCESS = 'FETCH_DATA_SUCCESS',
  FETCH_DATA_FAILURE = 'FETCH_DATA_FAILURE',
}

export enum searchTypes {
  CVE = 'CVE',
  CWE = 'CWE',
}

const searchCVE = (searchCve: string, tabIndex: number, dispatch: Function) => {
  dispatch({ type: actions.FETCH_DATA_REQUEST, payload: { tabIndex } });

  return axios
    .get(`${serverRoutes.cveSearchData}${searchCve}`)
    .then(({ data }) => {
      dispatch({
        type: actions.FETCH_DATA_SUCCESS,
        payload: {
          tabIndex,
          data,
        },
      });
    })
    .catch((err) => {
      dispatch({
        type: actions.FETCH_DATA_FAILURE,
        payload: {
          searchType: searchTypes.CVE,
          tabIndex,
          error: err.message,
        },
      });
    });
};

const searchCWE = (searchCwe: string, tabIndex: number, dispatch: Function) => {
  dispatch({ type: actions.FETCH_DATA_REQUEST, payload: { tabIndex } });

  return axios
    .get(`${serverRoutes.cweSearchData}${searchCwe}`)
    .then(({ data }) => {
      dispatch({
        type: actions.FETCH_DATA_SUCCESS,
        payload: {
          searchType: searchTypes.CWE,
          tabIndex,
          data,
        },
      });
    })
    .catch((err) => {
      dispatch({
        type: actions.FETCH_DATA_FAILURE,
        payload: {
          tabIndex,
          error: err.message,
        },
      });
    });
};

export const fetchData = (search: string, tabIndex: number) => (
  dispatch: Function,
) => {
  return search.toLowerCase().includes(`cwe`)
    ? searchCWE(search, tabIndex, dispatch)
    : searchCVE(search, tabIndex, dispatch);
};
