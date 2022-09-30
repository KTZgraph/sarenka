import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import LogoutIcon from "@mui/icons-material/Logout";
import LoginIcon from "@mui/icons-material/Login";

import Navigation from "../../components/atoms/navigation";
import "./Navbar.scss";

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
  const { navbarType, userEmail } = props;
  if (navbarType === "default" || navbarType == null) {
    return <NavbarDefault userEmail={userEmail} />;
  }

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

export default Navbar;
