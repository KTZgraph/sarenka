import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';

import HomeScreen from "./screens/HomeScreen";
import CVEScreen from "./screens/CVEScreen";
import CWEScreen from "./screens/CWEScreen";
import CPEScreen from "./screens/CPEScreen";
import ReferenceScreen from "./screens/ReferenceScreen";
import VectorScreen from "./screens/VectorScreen";
import Navbar from "./components/Navbar";
import CWEDetails from "./components/CWEDetails";

function App() {
  return (
    <Router>
      <Navbar/>
      <div className="content">
        <Switch>
          <Route exact path="/">
            <HomeScreen/>
          </Route>
          {/*settings*/}

          {/*search*/}

          {/*vulnerabilities*/}
          <Route path="/cwe-list">
            <CWEScreen/>
          </Route>

          <Route path="/cwe/:id">
            <CWEDetails/>
          </Route>
          <Route path="/cve-list">
            <CVEScreen/>
          </Route>
          <Route path="/cpe-list">
            <CPEScreen/>
          </Route>
          <Route path="/reference-list">
            <ReferenceScreen/>
          </Route>
          <Route path="/vector-list">
            <VectorScreen/>
          </Route>


        </Switch>
      </div>
    </Router>
  );
}

export default App;
