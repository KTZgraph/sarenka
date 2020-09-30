import { actions } from 'actions/hardwareInfoActions';

const initialState = {
  isLoading: false,
  data: {},
  error: '',
};

const rootReducer = (state = initialState, action: Record<string, any>) => {
  switch (action.type) {
    case actions.FETCH_REQUEST:
      return {
        isLoading: true,
      };
    case actions.FETCH_SUCCESS:
      return {
        isLoading: false,
        error: '',
        ...action.payload,
      };
    case actions.FETCH_FAILURE:
      return {
        isLoading: false,
        data: {},
        ...action.payload,
      };
    default:
      return state;
  }
};

export default rootReducer;
