import axios from 'axios';
import { serverRoutes } from 'routes';

export const actions: Record<string, string> = {
  FETCH_REQUEST: 'FETCH_REQUEST',
  FETCH_SUCCESS: 'FETCH_SUCCESS',
  FETCH_FAILURE: 'FETCH_FAILURE',
};

export const fetchInstalledPrograms = (tabIndex: number) => (
  dispatch: Function,
) => {
  dispatch({ type: actions.FETCH_REQUEST, payload: { tabIndex } });

  return axios
    .get(serverRoutes.registryScanData)
    .then(({ data }) => {
      dispatch({
        type: actions.FETCH_SUCCESS,
        payload: {
          tabIndex,
          data,
        },
      });
    })
    .catch((err) => {
      dispatch({
        type: actions.FETCH_FAILURE,
        payload: {
          tabIndex,
          error: err.message,
        },
      });
    });
};
