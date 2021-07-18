
import React from "react";
import {Link} from 'react-router-dom';

function Header() {
  return (
    <header>
      <Link to='/'>Home</Link>
      {/*vulns*/}
      <Link to='/cwe-list'>cwe-list</Link>
      <Link to='/cve-list'>cve-list</Link>
      <Link to='/cpe-list'>cpe-list</Link>
      <Link to='/reference-list'>reference-list</Link>
      <Link to='/vector-list'>vector-list</Link>
      
    </header>
  )
}

export default Header;