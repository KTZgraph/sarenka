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
});
