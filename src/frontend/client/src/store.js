// https://youtu.be/DGmX1FDdLZE?t=2211
// https://redux-toolkit.js.org/api/configureStore
import { configureStore } from "@reduxjs/toolkit";

export const store = configureStore({
  reducer: {},
});

const initialState = {
  first: {
    second: {
      third: {
        valOne: "",
        valTwo: "",
        isAuthenticated: false,
      },
      fifth: "asdf",
    },
    fourth: "asdf",
  },
  sixth: "asfasdf",
};
