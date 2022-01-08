// reużywalny komponent - wazna sciezka
import BottomList from "../navbar_components/bottom-list";
import HamburgerMenu from "../navbar_components/hamburger-menu";
import AdminImage from "../navbar_components/admin-image";
import SearchForm from "../navbar_components/search-form";
import VulnerabilityList from "../navbar_components/vulnerability-list";
import CredentialList from "../navbar_components/credential-list";
import GeolocationList from "../navbar_components/geolocation-list";
import DashboardList from "../navbar_components/dashboard-list";
import ChartList from "../navbar_components/chart-list";
// TODO: podłaczyć font-awesome

const Navbar = () => {
    const handleSubmenu = (e) => {
        const el = e.target.parentElement;
        if(el.classList.contains('nav-link')){
            if(el.nextElementSibling){
                el.nextElementSibling.classList.toggle('change');
                el.classList.toggle('change');
            }
        }
    }

    return (
        <nav className="sidebar"> {/* menu z lewej */}
              {/* górna cześc menu - logo, search-form */}
              <HamburgerMenu/> {/* hamubrger ikona */}
              <AdminImage/> {/* ikona i nazwa admina */}
              <SearchForm/> {/* search input field */}

              {/* lista w menu standardowa Właściwe menu */}
              <ul className="nav-list" onClick={handleSubmenu}>
                  <DashboardList />
                  <VulnerabilityList/>
                  <GeolocationList />
                  <ChartList/>
                  <CredentialList/>
              </ul> {/* koniec górnej listy menu */}

              {/* bootom list - małe śmieszczed ikonki z powiadomieniami*/}
              <BottomList/>
        </nav>
     );
}

export default Navbar;