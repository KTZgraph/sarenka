import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav class="navbar-primary justify-between">
        <div class="container">
        <h1 class="site-title">SARENKA</h1>
        <ul class="display-f">
        <Link to="/shodan-queries" class="ml-1 text-hover-secondary">Shodan Queries</Link>

        <Link to="/" class="ml-1 text-hover-secondary" >Home</Link>
        <Link to="/shodan-queries" class="ml-1 text-hover-secondary">Shodan Queries</Link>
        <Link to="/search" class="ml-1 text-hover-secondary">Search</Link>
        <Link to="/vulns" class="ml-1 text-hover-secondary">Vulnerabilities</Link>
        <Link to="/cwe-list" class="ml-1 text-hover-secondary">CWE</Link>
        </ul>
        </div>
    </nav>

  );
};

export default Navbar;
