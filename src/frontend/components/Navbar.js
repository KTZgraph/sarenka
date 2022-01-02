import Link from 'next/link';
import Image from 'next/image';
// reużywalny komponent - wazna sciezka

// TODO: podłaczyć font-awesome

const Navbar = () => {
    return ( 
        <nav className="sidebar">
          {/* menu z lewej */}
              {/* hamubrger ikona */}
              <div className="hamburger-menu">
                  <div className="line line-1"></div>
                  <div className="line line-2"></div>
                  <div className="line line-3"></div>
              </div>
              {/* ikona i nazwa admina */}
              <div className="card">
                  {/* obbrazek admina */}
                  <div className="card-img">
                      <Image src="/logo.png" className="admin-image" alt="Admin Image" width={128} height={77}/>
                  </div>
                  <div className="card-body">
                      <h2 className="card-title">SARENKA</h2>
                      <p className="card-subtitle">Administrator</p>
                  </div>    
              </div>
              {/* search input field */}
              <form class="search-form">
                  <input type="text" className="search-input" placeholder="Search"/>
                  {/* ważny jest typ przycisku w buttona w search */}
                  <button type="button" className="search-button">
                      <i className="fas fa-search"></i>
                  </button>
              </form>
              {/* lista w menu standardowa */}
              <ul className="nav-list">
                  {/* pierwsza opcja menu */}
                  <li className="nav-item">
                    <Link href="/">
                      <a href="#" className="nav-lisnk">
                          <i className="fas fa-tachometer-alt"></i>
                          <span className="nav-link-text">Dashboard</span>
                          <i className="fa fa-angle-right"></i>    
                      </a>
                    </Link>
                    {/* podmenu - nowa lista w liście tuż przez zamknieciem główenj li */}
                    <ul className="sub-nav-list">
                        {/* pierwsza opcja sumbenu */}
                        <li className="sub-nav-item">
                          <Link href="/">
                            <a href="#" className="sub-nav-link">
                                <i className="far fa-circle"></i>
                                <span>Dashboard 1</span>
                            </a>
                          </Link>
                        </li>
                        {/* druga opcja sumbenu */}
                        <li className="sub-nav-item">
                          <Link href="/"> 
                            <a className="sub-nav-link">
                                <i className="far fa-circle"></i>
                                <span>Dashboard 2</span>
                            </a>
                          </Link>
                        </li>
                        {/* trzecia opcja sumbenu */}
                        <li className="sub-nav-item">
                          <Link href="/">
                            <a className="sub-nav-link">
                                <i className="far fa-circle"></i>
                                <span>Dashboard 3</span>
                            </a>
                          </Link>
                        </li>
                    </ul>
                  </li>

{/* --------------------------------------- Vulnerabilities --------------------------------------- */}
                  {/* druga opcja menu */}
                  <li className="nav-item">
                    <Link href="/vulns">
                      <a className="nav-lisnk">
                          <i className="fas fa-shopping-cart"></i>
                          <span className="nav-link-text">Vulnerabilities</span>
                          <i className="fa fa-angle-right"></i>    
                      </a>
                    </Link>
                    {/* podmenu - nowa lista w liście tuż przez zamknieciem główenj li */}
                    <ul className="sub-nav-list">
                        {/* pierwsza opcja sumbenu */}
                        <li className="sub-nav-item">
                          <Link href="/">
                            <a href="#" className="sub-nav-link">
                                <i className="far fa-circle"></i>
                                <span>CWE list</span>
                            </a>
                          </Link>
                        </li>
                        {/* druga opcja sumbenu */}
                        <li className="sub-nav-item">
                            <a className="sub-nav-link">
                                <i className="far fa-circle"></i>
                                <span>CVE list</span>
                            </a>
                        </li>
                        {/* trzecia opcja sumbenu */}
                        <li className="sub-nav-item">
                          <Link href="/">
                            <a href="#" className="sub-nav-link">
                                <i className="far fa-circle"></i>
                                <span>Vendors</span>
                            </a>
                          </Link>
                        </li>
                        {/* czwarta opcja sumbenu */}
                        <li className="sub-nav-item">
                          <Link href="/">
                            <a href="#" className="sub-nav-link">
                                <i className="far fa-circle"></i>
                                <span>Products</span>
                            </a>
                          </Link>
                        </li>
                        {/* piąta opcja sumbenu */}
                        <li className="sub-nav-item">
                          <Link href="/">
                            <a href="#" className="sub-nav-link">
                                <i className="far fa-circle"></i>
                                <span>Technologies</span>
                            </a>
                          </Link>
                        </li>
                    </ul>
                  </li>
{/* --------------------------------------- Geolocation --------------------------------------- */}
                  {/* druga opcja menu */}
                  <li className="nav-item">
                    <Link href="/geo">
                      <a className="nav-lisnk">
                          <i className="fas fa-shopping-cart"></i>
                          <span className="nav-link-text">Geolocation</span>
                          <i className="fa fa-angle-right"></i>    
                      </a>
                    </Link>
                  </li>
                  {/* --------------------------------------- Credentials --------------------------------------- */}
                  {/* druga opcja menu */}
                  <li className="nav-item">
                    <Link href="/credentials">
                      <a className="nav-lisnk">
                          <i className="fas fa-shopping-cart"></i>
                          <span className="nav-link-text">Credentials</span>
                          <i className="fa fa-angle-right"></i>    
                      </a>
                    </Link>
                  </li>
                {/* koniec górnej listy menu */}
                </ul>

{/* --------------------------------------- BOTTOM LIST --------------------------------------- */}
                {/* bootom list */}
                <ul className="bottom-list">
                    {/* pierwsza opcja dolnej listy */}
                    <li className="bottom-list-item">
                      <Link href="/credentials">
                        <a className="bottom-list-link">
                            <span>5</span>
                            <i className="fa fa-bell"></i>
                        </a>
                      </Link>
                    </li>
                    {/* druga opcja dolnej listy */}
                    <li className="bottom-list-item">
                      <Link href="/credentials">
                        <a className="bottom-list-link">
                            <span>7</span>
                            <i className="fa fa-envelope"></i>
                        </a>
                      </Link>
                    </li>
                    {/* trzecia opcja dolnej listy */}
                    <li className="bottom-list-item">
                      <Link href="/credentials">
                        <a className="bottom-list-link">
                            <span>1</span>
                            <i className="fa fa-cog"></i>
                        </a>
                      </Link>
                    </li>
                    {/* trzecia opcja dolnej listy */}
                    <li className="bottom-list-item">
                      <Link href="/credentials">
                        <a className="bottom-list-link">
                            <i className="fa fa-power-off"></i>
                        </a>
                      </Link>
                    </li>
                </ul>
        </nav>
     );
}

export default Navbar;