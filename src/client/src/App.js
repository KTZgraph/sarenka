import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useContext } from "react";

import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import List from "./pages/list/List";
import Single from "./pages/single/Single";
import New from "./pages/new/New";
// ---------------- vulnerabilities -------------------
import VulnList from "./pages/cve/list/List";
import VulnSingle from "./pages/cve/single/Single";
//CWE (Common Weakness Enumeration)
import CweList from "./pages/vulnerabilities/cwe/List";
import CweSingle from "./pages/vulnerabilities/cwe/Single";
// CVE (Common Vulnerabilities and Exposures)
import CveList from "./pages/vulnerabilities/cve/CveList";
import CveSingle from "./pages/vulnerabilities/cve/Single";

import { DarkModeContext } from "./context/darkModeContext";

function App() {
  const { darkMode } = useContext(DarkModeContext);

  return (
    <div className={darkMode ? "App dark" : "App"}>
      <BrowserRouter>
        <Routes>
          <Route path="/">
            <Route index element={<Home />} />
            <Route path="login" element={<Login />} />

            <Route path="users">
              <Route index element={<List />} />
              <Route path=":userId" element={<Single />} />
              <Route path="new" element={<New />} />
            </Route>
            <Route path="products">
              <Route index element={<List />} />
              <Route path=":productId" element={<Single />} />
              <Route path="new" element={<New />} />
            </Route>
            <Route path="vulns">
              <Route index element={<VulnList />} />
              <Route path=":vulnId" element={<VulnSingle />} />
              <Route path="new" element={<New />} />
              <Route path="cwes">
                <Route index element={<CweList />} />
                <Route path=":cweId" element={<CweSingle />} />
                {/* TODO pobieranie listy CVE dla dane CWE */}
                {/* <Route path=":cweId/cves" element={<New />} /> */}
              </Route>
              <Route path="cves">
                {/* TODO od groma */}
                <Route index element={<CveList />} />
                <Route path=":cveId" element={<CveSingle />} />
                {/* TODO pobieranie CWE dla dane CVE */}
              </Route>
            </Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
