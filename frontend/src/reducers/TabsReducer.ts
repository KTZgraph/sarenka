import { actions } from 'actions/TabsActions';

const initialState = {
  0: {
    index: 0,
    link: '/remotehostinfo',
    label: 'Remote host info',
  },
};

const createNewTab = (state: any, action: any) => {
  const index =
    state[Object.keys(state)[Object.keys(state).length - 1]].index + 1;
  return {
    ...state,
    [index]: { index, ...action.payload },
  };
};

const removeTab = (state: any, action: any) => {
  const newState = state;
  delete newState[action.payload.index];
  return {
    ...newState,
  };
};

const updateUrl = (state: any, action: any) => {
  return {
    ...state,
    [action.payload.index]: {
      ...state[action.payload.index],
      link: action.payload.tabUrl,
    },
  };
};

const tabsReducer = (state = initialState, action: Record<string, any>) => {
  switch (action.type) {
    case actions.CREATE_NEW_TAB:
      return createNewTab(state, action);
    case actions.REMOVE_TAB:
      return removeTab(state, action);
    case actions.UPDATE_TAB_URL:
      return updateUrl(state, action);
    default:
      return state;
  }
};

export default tabsReducer;
