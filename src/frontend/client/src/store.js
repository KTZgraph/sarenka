// https://youtu.be/DGmX1FDdLZE?t=2211
// https://redux-toolkit.js.org/api/configureStore
import { configureStore } from "@reduxjs/toolkit";
// mój reducer
import userReducer from "./features/user";

export const store = configureStore({
  reducer: {
    /* kiedy chcę dostać się do wartości, które są zwiażane z userem, będe robić user.atrybutKtoryChce
    trzeba będize użyć hooka z react-redux
     import {useSelector} from 'react-redux'
     const user = useSelector(state => state.user)
    //  albo destrukturyzacja
    const {isAuthenticated} = useSelector(state => state.user)
     */
    user: userReducer,
  },
  /*  dodatkowe middleware on top of the default
     https://redux-toolkit.js.org/api/configureStore#devtools
     można dac też inne rzeczy - teraz możn aużyć dev tools extensions from Chrome/ Firefox*/
  // devTools: true,
  /*   WARNING - to można dac też LOGGER
  /  https://redux-toolkit.js.org/api/configureStore#full-example
  /  import logger from 'redux-logger'
  /   słowo klucz middleware z callback function*/

  /*
    devTools: process.env.NODE_ENV !== 'production',
trick ze sprtawdzeniem czy to produckaj
NODE_ENV zmienna środowiskowa globalna z sarenka\src\frontend\client\src\.env  
*/
  devTools: process.env.NODE_ENV !== "production",
});
