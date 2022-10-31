/* do reguxtoolki
 on teraz jak nie ma samego Reduxa upraszcza wiele rzeczy
 dodatkowo jak się apkę react stworzy z templatu Reduxa to też tworzy folder `features`
 */

//  https://redux-toolkit.js.org/api/createSlice kopia kodu JS
import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

// https://redux-toolkit.js.org/api/createAsyncThunk

const initialState = {
  isAuthenticated: false,
  user: null,
  //   można pokazywać spinnery jak się ładuje
  loading: false,
  //   będzie true jak prawidłowo zarejestrujemy konto
  registered: false,
  // FIXME można dodać błąd
  error: null,
  // FIXME - można dodać message np po porwanym zalgoowaniu się
  message: "",
};

// https://redux-toolkit.js.org/api/createAsyncThunk
// udeżam do endpoint a z sarenka\src\frontend\routes\auth\register.js
// awsync jeden parametr któy jest obiektem
// WARNING register is actionCreator
// export bo chcę tę funkcję do registerPage
export const register = createAsyncThunk(
  // https://redux-toolkit.js.org/api/createAsyncThunk#type
  // WARNING liczba mnoga "users/register"
  "users/register",
  // https://redux-toolkit.js.org/api/createAsyncThunk#payloadcreator
  // If you need to pass in multiple values, pass them together in an object when you dispatch the thunk, like dispatch(fetchUsers({status: 'active', sortBy: 'name'})).
  async ({ first_name, last_name, email, password }, thunkAPI) => {
    //WARNING alternatywnie https://youtu.be/cvu6a3P9S0M?t=1010
    // async (arg, thunkAPI) => {
    // const body = JSON.strignify(arg)

    // żadanie do servera express
    const body = JSON.stringify({
      first_name,
      last_name,
      email,
      password,
    });

    try {
      // BUG CORS
      // const res = await fetch(`${API_URL}/api/users/register`, {
      // WARNIGN - teraz używam proxy z develmpnetu, ale na priodukcji i tak to będzi ena localhost 5000
      const res = await fetch("/api/users/register", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          first_name,
          last_name,
          email,
          password,
        }),
      });

      // dane z RegisterView z sarenka\src\service-core\users\views.py
      const data = await res.json();

      if (res.status === 201) {
        // WARNING https://youtu.be/cvu6a3P9S0M?t=1164
        // tu też możnaby aktualizaowac user z initialState, ale osobny handler będzie lepszy
        // FIXME można zmienić stan wartosci message
        return data;
      } else {
        // WARNING /api/users/register/rejected z dokumentacji
        return thunkAPI.rejectWithValue(data);
      }
    } catch (err) {
      // ttuaj nie mam data
      return thunkAPI.rejectWithValue(err.response.data);
    }
  }
);

// do pobierania dancyh usera, nie przyjmuje żadnych argumentów więc używam podłogi _
const getUser = createAsyncThunk("users/me", async (_, thunkAPI) => {
  // trzeba pamietać, zeby dodać user/me/pending user/me/fullfiled user/me/rejected z dokumentacji redux toolkit

  try {
    // url do express servera
    // cookies powinny być send along with this request
    const res = await fetch("/api/users/me", {
      // ttuaj nie trzeba być authorized żeby dostać się do tego route handler
      method: "GET",
      headers: {
        accept: "application/json",
        // tui nei dam Atugorization Beare bo po prostu nie mam do niego dostępu, bo to httpOnly cookie czego chcemy
        // WARNING NIE chcemy żeby klient miał dostęp do cookie
      },
    });

    const data = await res.json();

    if (res.status === 200) {
      // zwraca data jako payload
      return data;
    } else {
      return thunkAPI.rejectWithValue(data);
    }
  } catch (err) {
    // err.response.data bo w catch nie mam dostępu do data
    return thunkAPI.rejectWithValue(err.response.data);
  }
});

export const login = createAsyncThunk(
  "users/login", // type
  async ({ email, password }, thunkAPI) => {
    const body = JSON.stringify({
      email,
      password,
    });

    try {
      const res = await fetch("/api/users/login", {
        // sarenka\src\frontend\routes\auth\login.js enpoint z expressa
        method: "POST",
        headers: {
          accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email,
          password,
        }),
      });

      const data = await res.json();

      if (res.status === 200) {
        // BUG przez literówkę z destrukturyzacji NIE działało
        const { dispatch } = thunkAPI;

        dispatch(getUser());

        return data;
      } else {
        return thunkAPI.rejectWithValue(data);
      }
    } catch (err) {
      return thunkAPI.rejectWithValue(err.response.data);
      // return thunkAPI.rejectWithValue("tutaj w loginie coś nie pykło");
    }
  }
);

// weryfikacja tokenu
// WARNING https://youtu.be/GaKGYo2jQ2Y?t=1051
export const checkAuth = createAsyncThunk(
  "users/verify",
  async (_, thunkAPI) => {
    // potrzben do isAuthenticated i loading z state
    try {
      const res = await fetch("/api/users/verify", {
        // sarenka\src\frontend\routes\auth\login.js enpoint z expressa
        method: "GET",
        headers: {
          accept: "application/json",
        },
      });

      const data = await res.json(); //jak wszystko się uda to dane {} pochodzące z endpointu  path("api/token/verify/ z sarenka\src\service-core\auth_site\urls.py

      if (res.status === 200) {
        const { dispatch } = thunkAPI;

        dispatch(getUser());

        // FIXME - można wykorzystać te dane
        return data;
      } else {
        return thunkAPI.rejectWithValue(data);
      }
    } catch (err) {
      return thunkAPI.rejectWithValue(err.response.data);
    }
  }
);

export const logout = createAsyncThunk(
  // akcje do wylogowywania
  // https://youtu.be/oa_YvzYDyR8?t=2791
  "users/logout", // type
  async (_, thunkAPI) => {
    try {
      const res = await fetch("/api/users/logout", {
        // sarenka\src\frontend\routes\auth\login.js enpoint z expressa
        method: "GET",
        headers: {
          accept: "application/json",
        },
      });

      const data = await res.json();

      if (res.status === 200) {
        // sprawdzam czy jest wylogowany prawdiłowo zwrotka z sarenka\src\frontend\routes\auth\logout.js
        // FIXME - można użyć do alertu
        return data;
      } else {
        return thunkAPI.rejectWithValue(data);
      }
    } catch (err) {
      return thunkAPI.rejectWithValue(err.response.data);
    }
  }
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

  // WARNING https://redux-toolkit.js.org/api/createSlice#parameters
  extraReducers: (builder) => {
    // ddoanie actionCreator pending, fulfilled, rejected z  dokumendacji
    builder
      // .addCase(register.pending, (state, action) => {
      //WARNING  nie uzywam action to nie muszę brać argumentu
      .addCase(register.pending, (state) => {
        // można bezpośrednio zmieniać stan, nie koniecznei przez return i spread operator
        state.loading = true;
      })
      // .addCase(register.fulfilled, (state, action) => {
      .addCase(register.fulfilled, (state) => {
        // wszystko się udało, zmieniam wartośc- na podstawie jej będe przekierowywać usera to srony logowania
        state.loading = false;
        state.registered = true;
      })
      .addCase(register.rejected, (state, action) => {
        // NIE udało się
        state.loading = false;
        // FIXME można dodac błąd i zapisac go do state
      })
      // dodatkowy reducer dla logowania
      // .addCase(login.pending, (state, payload))
      // WARNING - nie uzywam payload to go nie biorę jako argumentu
      .addCase(login.pending, (state) => {
        state.loading = true;
      })
      .addCase(login.fulfilled, (state) => {
        state.loading = false;
        state.isAuthenticated = true;
      })
      .addCase(login.rejected, (state) => {
        state.loading = false;
      })

      // do pobierani dancyh users/me
      .addCase(getUser.pending, (state) => {
        state.loading = true;
      })
      .addCase(getUser.fulfilled, (state, action) => {
        state.loading = false;
        // WARNING - zapisuje dane usera z payload
        // https://youtu.be/oa_YvzYDyR8?t=2228
        state.user = action.payload;
      })
      .addCase(getUser.rejected, (state) => {
        state.loading = false;
      })
      // do werfyikacji tokenu
      .addCase(checkAuth.pending, (state) => {
        state.loading = true;
      })
      .addCase(checkAuth.fulfilled, (state) => {
        // WARNING nie ustiawiam żadnych danych to tez nie aktualizuję state.user
        // https://youtu.be/GaKGYo2jQ2Y?t=1229
        state.loading = false;
        state.isAuthenticated = true;
      })
      .addCase(checkAuth.rejected, (state) => {
        state.loading = false;
      })
      // do wylogowywania
      .addCase(logout.pending, (state) => {
        state.loading = true;
      })
      .addCase(logout.fulfilled, (state) => {
        state.loading = false;
        // tu pozmienkć stan, user dane na null i nieuatoryzowany
        state.user = null;
        state.isAuthenticated = false;
      })
      .addCase(logout.rejected, (state) => {
        state.loading = false;
      });
  },
});

export const { resetRegistered } = userSlice.actions;
export default userSlice.reducer;
