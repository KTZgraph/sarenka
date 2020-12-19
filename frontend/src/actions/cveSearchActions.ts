import axios from 'axios';
import { serverRoutes } from 'routes';

export const actions: Record<string, string> = {
  FETCH_DATA_REQUEST: 'FETCH_DATA_REQUEST',
  FETCH_DATA_SUCCESS: 'FETCH_DATA_SUCCESS',
  FETCH_DATA_FAILURE: 'FETCH_DATA_FAILURE',
};

export const fetchData = (searchCve: string, tabIndex: number) => (
  dispatch: Function,
) => {
  dispatch({ type: actions.FETCH_DATA_REQUEST, payload: { tabIndex } });

  return axios
    .get(`${serverRoutes.cveSearchData}${searchCve}`)
    .then(({ data }) => {
      console.log(data);
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
          tabIndex,
          error: err.message,
        },
      });
    });
};
