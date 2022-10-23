import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import LogoutIcon from "@mui/icons-material/Logout";
import LoginIcon from "@mui/icons-material/Login";

// użycie Reduxa https://youtu.be/DGmX1FDdLZE?t=3180
import { useSelector } from "react-redux";

import Navigation from "../../components/atoms/navigation";
import "./Navbar.scss";

// FIXME - NavbarDefault już nie potrzebny
const NavbarDefault = ({ userEmail }) => {
  return (
    <div className="navbar">
      <div className="navbar__container">
        <div className="navbar__items">
          {userEmail && (
            <div className="navbar__item">
              <span style={{ color: "black" }}>{userEmail}</span>
            </div>
          )}
          {userEmail ? (
            <Navigation to="/logout" type="logout" className="navbar__item">
              <LogoutIcon className="navbar__icon" />
              <span className="navbar__text">logout</span>
            </Navigation>
          ) : (
            <Navigation to="/login" type="login" className="navbar__item">
              <LoginIcon className="navbar__icon" />
              <span className="navbar__text">login</span>
            </Navigation>
          )}
        </div>
        <hr />
      </div>
    </div>
  );
};

const Navbar = (props) => {
  // redux
  const { isAuthenticated } = useSelector((state) => state.user);

  const { navbarType, userEmail } = props;
  // if (navbarType === "default" || navbarType == null) {
  //   return <NavbarDefault userEmail={userEmail} />;
  // }

  return (
    <div className="navbar">
      <div className="navbar__container">
        <div className="navbar__search">
          <input
            className="navbar__input"
            type="text"
            placeholder="Search..."
          />
          <SearchOutlinedIcon className="navbar__icon" />
        </div>
        <div className="navbar__items">
          {userEmail && (
            <div className="navbar__item">
              <span style={{ color: "black" }}>{userEmail}</span>
            </div>
          )}
          {isAuthenticated ? (
            <Navigation to="/logout" type="logout" className="navbar__item">
              <LogoutIcon className="navbar__icon" />
              <span className="navbar__text">logout</span>
            </Navigation>
          ) : (
            <Navigation to="/login" type="login" className="navbar__item">
              <LoginIcon className="navbar__icon" />
              <span className="navbar__text">login</span>
            </Navigation>
          )}
        </div>
        <hr />
      </div>
    </div>
  );
};

export default Navbar;
