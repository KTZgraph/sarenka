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
      //   BUG - to źle it goes against Redux desgin  pattern; jeśli to  robię samemu
      //   state.first.second.third.isAuthenticated = true //nie manipulujemy bezpośrednio stanem


    //   jeśli robię to z paczką / narzędziem to mogę w ten sposób zrobić
    // bo pod maską robi całe te zagnieżdżenia
    state.first.second.third.isAuthenticated = true;
    // które są poniżej
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
