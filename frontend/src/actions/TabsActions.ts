export const actions: Record<string, string> = {
  CREATE_NEW_TAB: 'CREATE_NEW_TAB',
  REMOVE_TAB: 'REMOVE_TAB',
  UPDATE_TAB_URL: 'UPDATE_TAB_URL',
};

export const createNewTab = (link: string, label: string) => (
  dispatch: Function,
) => {
  return dispatch({
    type: actions.CREATE_NEW_TAB,
    payload: {
      link,
      label,
    },
  });
};

export const removeTab = (index: number) => (dispatch: Function) => {
  return dispatch({
    type: actions.REMOVE_TAB,
    payload: {
      index,
    },
  });
};

export const updateTabUrl = (tabUrl: string, index: number) => (
  dispatch: Function,
) => {
  return dispatch({
    type: actions.UPDATE_TAB_URL,
    payload: {
      index,
      tabUrl,
    },
  });
};
