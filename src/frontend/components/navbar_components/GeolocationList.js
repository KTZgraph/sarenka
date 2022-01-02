import Link from 'next/link';


const GeolocationList = () => {
    return (
        <li className="nav-item">
        <Link href="/geo">
          <a className="nav-link">
              <i className="fas fa-shopping-cart"></i>
              <span className="nav-link-text">Geolocation</span>
              <i className="fa fa-angle-right"></i>    
          </a>
        </Link>
      </li>
    )
}

export default GeolocationList;