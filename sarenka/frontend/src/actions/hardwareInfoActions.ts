import axios from 'axios';
import { serverRoutes } from 'routes';

export const actions: Record<string, string> = {
  FETCH_REQUEST: 'FETCH_HARDWARE_INFO_REQUEST',
  FETCH_SUCCESS: 'FETCH_HARDWARE_INFO_SUCCESS',
  FETCH_FAILURE: 'FETCH_HARDWARE_INFO_FAILURE',
};

export const fetchHardwareInfo = (tabIndex: number) => (dispatch: Function) => {
  dispatch({ type: actions.FETCH_REQUEST, payload: { tabIndex } });

  return axios
    .get(serverRoutes.hardwareInfoData)
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

export const fetchReport = () => {
  const URL = serverRoutes.hardwareInfoReport;
  window.open(URL);
};
