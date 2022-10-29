import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import "./index.css";
import "./styles/main.scss";
import { DarkModeContextProvider } from "./context/darkModeContext";
import { AuthContextProvider } from "./context/AuthContext";
import { ToastContextProvider } from "./context/ToastContext";
// redux
// WARNING https://youtu.be/GaKGYo2jQ2Y?t=1322
import { Provider } from "react-redux";
// Redux provider z biblioteki żeby iopakowac moja cała apkę i dać jej dostęp do sarenka\src\frontend\client\src\store.js
import { store } from "./store";

// MOCKED server
// WARNING tylko jeden plik z mockowanym serverem
// import "./server_mock/server";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Provider store={store}>
      {/* tu provider ze store zamiast w App.js */}
      <ToastContextProvider>
        <DarkModeContextProvider>
          <AuthContextProvider>
            <App />
          </AuthContextProvider>
        </DarkModeContextProvider>
      </ToastContextProvider>
    </Provider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
