// reużywalny komponent - wazna sciezka
import BottomList from "./navbar_components/BottomList";
import HamburgerIcon from "./navbar_components/HamburgerIcon";
import AdminImage from "./navbar_components/AdminImage";
import SearchForm from "./navbar_components/SearchForm";
import VulnerabilitiesList from "./navbar_components/VulnerabilitiesList";
import CredentialsList from "./navbar_components/CredentialsList";
import GeolocationList from "./navbar_components/GeolocationList";
import DashboardList from "./navbar_components/DashboardList";
import ChartList from "./navbar_components/ChartList";
// TODO: podłaczyć font-awesome

const Navbar = () => {
    return (
        <nav className="sidebar"> {/* menu z lewej */}
              {/* górna cześc menu - logo, search-form */}
              <HamburgerIcon/> {/* hamubrger ikona */}
              <AdminImage/> {/* ikona i nazwa admina */}
              <SearchForm/> {/* search input field */}

              {/* lista w menu standardowa Właściwe menu */}
              <ul className="nav-list">
                  <DashboardList/>
                  <VulnerabilitiesList/>
                  <GeolocationList />
                  <ChartList/>
                  <CredentialsList/>
              </ul> {/* koniec górnej listy menu */}

              {/* bootom list - małe śmieszczed ikonki z powiadomieniami*/}
              <BottomList/>
        </nav>
     );
}

export default Navbar;