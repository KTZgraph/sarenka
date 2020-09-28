import axios from 'axios';

export const actions: Record<string, string> = {
  FETCH_DATA_REQUEST: 'FETCH_DATA_REQUEST',
  FETCH_DATA_SUCCESS: 'FETCH_DATA_SUCCESS',
  FETCH_DATA_FAILURE: 'FETCH_DATA_FAILURE',
};

export const fetchData = (searchCve: string) => (dispatch: Function) => {
  dispatch({ type: actions.FETCH_DATA_REQUEST });

  return axios
    .get(`http://localhost:8000/search/cve/${searchCve}`)
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
