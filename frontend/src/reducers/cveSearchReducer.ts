import { actions } from 'actions/cveSearchActions';

const initialState = {
  isLoading: false,
  data: {},
  error: '',
};

const rootReducer = (state = initialState, action: Record<string, any>) => {
  switch (action.type) {
    case actions.FETCH_DATA_REQUEST:
      return {
        ...state,
        [action.payload.tabIndex]: {
          isLoading: true,
        },
      };
    case actions.FETCH_DATA_SUCCESS:
      return {
        ...state,
        [action.payload.tabIndex]: {
          isLoading: false,
          error: '',
          ...action.payload,
        },
      };
    case actions.FETCH_DATA_FAILURE:
      return {
        ...state,
        [action.payload.tabIndex]: {
          isLoading: false,
          data: {},
          ...action.payload,
        },
      };
    default:
      return state;
  }
};

export default rootReducer;
