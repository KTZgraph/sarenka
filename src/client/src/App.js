import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useContext } from "react";
import { v4 as uuidV4 } from "uuid";

import { DarkModeContext } from "./context/darkModeContext";
import { AuthContext } from "./context/AuthContext";

import Toast from "./UI/Toast";

// -------------- NOWE SCIEZKI DO PLIKOW
import Dashboard from "./core/dashboard/pages/Dashboard";
import Statistics from "./core/statistics/pages/Statistics";
import Login from "./core/login/pages/Login";
import VulnerabilityList from "./core/vulnerabilities/pages/VulnerabilityList";

import "./App.scss";

function App() {
  const { darkMode } = useContext(DarkModeContext);
  const { currentUser } = useContext(AuthContext);

  return (
    <div className={darkMode ? "App dark" : "App"}>
      <BrowserRouter>
        <Routes>
          <Route path="/">
            <Route index element={<Dashboard />} />
            <Route path="login" element={<Login />} />
            <Route path="vulnerabilities" element={<VulnerabilityList />} />
            <Route path="statistics" element={<Statistics />} />

            {/* <Route path="register" element={<Register />} /> */}
          </Route>

        </Routes>
        <Toast
          position="notification-position__bottom-right"
          autoDeleteInterval={4000}
        />
      </BrowserRouter>
    </div>
  );
}

export default App;
