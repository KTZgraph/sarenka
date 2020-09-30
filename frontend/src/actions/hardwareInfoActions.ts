import axios from 'axios';

export const actions: Record<string, string> = {
  FETCH_REQUEST: 'FETCH_HARDWARE_INFO_REQUEST',
  FETCH_SUCCESS: 'FETCH_HARDWARE_INFO_SUCCESS',
  FETCH_FAILURE: 'FETCH_HARDWARE_INFO_FAILURE',
};

export const fetchHardwareInfo = () => (dispatch: Function) => {
  dispatch({ type: actions.FETCH_REQUEST });

  return axios
    .get(`http://127.0.0.1:8000/analyzer/local/windows/hardware`)
    .then(({ data }) => {
      dispatch({
        type: actions.FETCH_SUCCESS,
        payload: {
          data,
        },
      });
    })
    .catch((err) => {
      dispatch({
        type: actions.FETCH_FAILURE,
        payload: {
          error: err.message,
        },
      });
    });
};
