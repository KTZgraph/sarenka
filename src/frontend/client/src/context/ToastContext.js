import { createContext, useReducer } from "react";

export const ToastContext = createContext();

export const ToastContextProvider = (props) => {
  const [state, dispatch] = useReducer((state, action) => {
    switch (action.type) {
      case "ADD_NOTIFICATION":
        return [...state, action.payload];
      case "DELETE_NOTIFICATION":
        return state.filter(
          (notification) => notification.id !== action.payload
        );
      default:
        return state;
    }
  }, []);

  return (
    <ToastContext.Provider value={{ state, dispatch }}>
      {props.children}
    </ToastContext.Provider>
  );
};
