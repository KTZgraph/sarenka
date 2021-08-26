import {Link} from 'react-router-dom';

const Navbar = () => {
  return (
    <div className="navbar">
      <h1>SARENKA</h1>
      <div className="links">
        <Link to="/">Home</Link>
        <Link to="/search">Search</Link>
        <Link to="/vulns">Vulnerabilities</Link>
      </div>

    </div>
  );
};

export default Navbar;
