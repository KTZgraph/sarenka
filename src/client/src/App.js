import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useContext } from "react";
import { v4 as uuidV4 } from "uuid";

import Sidebar from "./components/organisms/sidebar/Sidebar";
import Navbar from "./components/organisms/navbar/Navbar";

import Home from "./pages/dashboard/pages/Home";
import Search from "./pages/search/pages/Search";
import Login from "./pages/auth/Login";

// ---------------- vulnerabilities -------------------
import NewVulnerability from "./pages/vulnerabilities/pages/NewVulnerability";

// ------------- notes-service
import Notes from "./pages/notes/pages/Notes";
import NewNote from "./pages/notes/pages/NewNote";

import { DarkModeContext } from "./context/darkModeContext";

import "./App.scss";

function App() {
  const { darkMode } = useContext(DarkModeContext);

  return (
    <div className={darkMode ? "App dark" : "App"}>
      <BrowserRouter>
        {/* sidebar */}
        <Sidebar />
        <main>
          {/* navbar */}
          <Navbar />
          <Routes>
            {/* główne komponenty */}
            <Route path="/">
              <Route index element={<Home />} />
              <Route path="login" element={<Login />} />
              <Route path="search" element={<Search />} />
            </Route>

            {/* vulnerabilities */}
            <Route path="/vulns">
              <Route path="new" element={<NewVulnerability />} />
            </Route>

            {/* notes */}
            <Route path="/notes">
              <Route path=":noteId" element={<NewNote />} />
              <Route path=":vulnId" element={<Notes />} />
              <Route
                path="new"
                element={<Navigate to={`/notes/${uuidV4()}`} />}
              />
            </Route>
          </Routes>
        </main>
      </BrowserRouter>
    </div>
  );
}

export default App;
