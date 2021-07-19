import logo from './logo.svg';
import {BrowserRouter as Router, Route} from 'react-router-dom';

import Header from "./components/Header";
import HomeScreen from "./screens/HomeScreen";
import CVEScreen from "./screens/CVEScreen";
import CWEScreen from "./screens/CWEScreen";
import CPEScreen from "./screens/CPEScreen";
import ReferenceScreen from "./screens/ReferenceScreen";
import VectorScreen from "./screens/VectorScreen";

function App() {
  return (
    <Router>
      <Header/>
      <main className="py-3">
        <div>
          <Route path='/' component={HomeScreen} exact/>
          {/*vulns*/}
          <Route path='/cwe/:id' component={CWEScreen}/>
          <Route path='/cve-list' component={CVEScreen}/>
          <Route path='/cpe-list' component={CPEScreen}/>
          <Route path='/reference-list' component={ReferenceScreen}/>
          <Route path='/vector-list' component={VectorScreen}/>

          {/*id z cart opcjonalny parametr*/}
          {/*<Route path='/cart/:id?' component={CartScreen}/>*/}
        </div>
      </main>
      {/*<Footer/>*/}
    </Router>
  );
}

export default App;
