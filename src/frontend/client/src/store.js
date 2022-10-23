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


// ręczne zarządzanei stanem - ni eproblem jak jest mały
// https://www.youtube.com/watch?v=DGmX1FDdLZE 43:53
switch (action.type) {
  case "LOGIN_SUCCES":
    return {
      // tutja jest kopia stanu - jak używam reduxa nie manipuluję stanem bezpośrednio
      //   BUG - to źle it goes against Redux desgin  pattern
      //   state.first.second.third.isAuthenticated = true //nie manipulujemy bezpośrednio stanem
      ...state,
      first: {
        ...state.first,
        second: {
          ...state.first.second,
          third: {
            ...state.first.second.third,
            // WARNING - tutaj dopiero zmieniam wartość
            isAuthenticated: true,
          },
        },
      },
    };
}
