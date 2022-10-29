import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import LogoutIcon from "@mui/icons-material/Logout";
import LoginIcon from "@mui/icons-material/Login";

// użycie Reduxa https://youtu.be/DGmX1FDdLZE?t=3180
import { useSelector, useDispatch } from "react-redux";
// https://youtu.be/oa_YvzYDyR8?t=2983
import { logout } from "../../features/user";

import Navigation from "../../components/atoms/navigation";
import "./Navbar.scss";

const Navbar = (props) => {
  // redux
  const { isAuthenticated } = useSelector((state) => state.user);

  const { navbarType, userEmail } = props;

  // do wylogowywania
  // https://youtu.be/oa_YvzYDyR8?t=2983
  const userDispatch = useDispatch();

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
            <a
              href="#!"
              className="navbar__item"
              onClick={() => userDispatch(logout())}
            >
              <LogoutIcon className="navbar__icon" />
              <span className="navbar__text">logout</span>
            </a>
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
