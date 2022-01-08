import Link from 'next/link';

const DashboardList = () => {
    return (
        <li className="nav-item">
        <Link href="/">
          <a href="#" className="nav-link">
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
    )
}

export default DashboardList;