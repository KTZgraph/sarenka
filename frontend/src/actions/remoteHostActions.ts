import axios from 'axios';

export const actions: Record<string, string> = {
  FETCH_DATA_REQUEST: 'FETCH_HOST_INFO_REQUEST',
  FETCH_DATA_SUCCESS: 'FETCH_HOST_INFO_SUCCESS',
  FETCH_DATA_FAILURE: 'FETCH_HOST_INFO_FAILURE',
};

export const fetchData = (searchHost: string) => (dispatch: Function) => {
  dispatch({ type: actions.FETCH_DATA_REQUEST });

  return axios
    .get(`http://localhost:8000/search/censys/${searchHost}`)
    .then(({ data }) => {
      dispatch({
        type: actions.FETCH_DATA_SUCCESS,
        payload: {
          data,
        },
      });
    })
    .catch((err) => {
      dispatch({
        type: actions.FETCH_DATA_FAILURE,
        payload: {
          error: err.message,
        },
      });
    });
};
