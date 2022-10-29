/* do reguxtoolki
 on teraz jak nie ma samego Reduxa upraszcza wiele rzeczy
 dodatkowo jak się apkę react stworzy z templatu Reduxa to też tworzy folder `features`
 */

//  https://redux-toolkit.js.org/api/createSlice kopia kodu JS
import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

// https://redux-toolkit.js.org/api/createAsyncThunk
import { userAPI } from "./userAPI";

const initialState = {
  isAuthenticated: false,
  user: null,
  //   można pokazywać spinnery jak się ładuje
  loading: false,
  //   będzie true jak prawidłowo zarejestrujemy konto
  registered: false,
};

// https://redux-toolkit.js.org/api/createAsyncThunk
// udeżam do endpoint a z sarenka\src\frontend\routes\auth\register.js
// awsync jeden parametr któy jest obiektem
const register = createAsyncThunk(
  // https://redux-toolkit.js.org/api/createAsyncThunk#type
  "user/register",
  // https://redux-toolkit.js.org/api/createAsyncThunk#payloadcreator
  // If you need to pass in multiple values, pass them together in an object when you dispatch the thunk, like dispatch(fetchUsers({status: 'active', sortBy: 'name'})).
  async ({ first_name, last_name, email, password }) => {}
);

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    /* synchronous dispatches
  so synchronous dispatches now redux thunk has the thunk middleware by default, and then it has something called a create async thunk https://redux-toolkit.js.org/api/createAsyncThunk
  which is going to allow you to actually do the asynchronous dispatches
  so these async thunks are something that we can go ahead and utilize
  Now these  async thunks are something that we define outside of this slice

  So with this reduces whatever's inside of here it's generating actions creators, but now we're gonna have action creators that are defined outside of here
  */

    // synchroniczne reset na stronie login
    resetRegistered: (state) => {
      // po prawidłowej rejestracji i zalogowaniu
      state.registered = false;
    },
  },
});

export const { resetRegistered } = userSlice.actions;
export default userSlice.reducer;
