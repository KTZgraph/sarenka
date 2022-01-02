import Link from 'next/link';


const ChartList = () => {
    return (
        <li className="nav-item">
        <Link href="/credentials">
          <a className="nav-link">
              <i className="fas fa-shopping-cart"></i>
              <span className="nav-link-text">Credentials</span>
              <i className="fa fa-angle-right"></i>    
          </a>
        </Link>
      </li>
    )
}

export default ChartList;