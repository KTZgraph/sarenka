import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import HomeScreen from "./screens/HomeScreen";
import CVEScreen from "./screens/CVEScreen";
import CWEScreen from "./screens/CWEScreen";
import CPEScreen from "./screens/CPEScreen";
import ReferenceScreen from "./screens/ReferenceScreen";
import VectorScreen from "./screens/VectorScreen";
import Navbar from "./components/Navbar";
import CWEDetails from "./components/CWEDetails";
import Spinner from './components/Spinner';
import SpinnerTwo from './components/SpinnerTwo';

function App() {
  return (
    <Router>
      <Navbar />
      <main className="content">
        <Switch>
          <Route exact path="/">
            <HomeScreen />
          </Route>

          {/* spinner */}
          <Route path="/spinner2" component={SpinnerTwo} />

          <Route path="/spinner" component={Spinner} />

          {/*settings*/}

          {/*search*/}

          {/*vulnerabilities*/}
          <Route path="/cwe-list" component={CWEScreen} />
          <Route path="/cwe/:id" component={CWEDetails} />

          <Route path="/cve-list" component={CVEScreen} />
          <Route path="/cve/:id" component={CVEScreen} />

          <Route path="/cpe-list">
            <CPEScreen />
          </Route>
          <Route path="/reference-list">
            <ReferenceScreen />
          </Route>
          <Route path="/vector-list">
            <VectorScreen />
          </Route>


        </Switch>
      </main>
    </Router>
  );
}

export default App;
