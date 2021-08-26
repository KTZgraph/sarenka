import {Link} from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar">
      <h1>SARENKA</h1>
      <div className="links">
        <Link to="/">Home</Link>
        <Link to="/search">Search</Link>
        <Link to="/vulns">Vulnerabilities</Link>
        <Link to="/cwe-list">CWE</Link>
      </div>

    </nav>
  );
};

export default Navbar;
