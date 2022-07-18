import DashboardRoundedIcon from "@mui/icons-material/DashboardRounded";
import GppBadRoundedIcon from "@mui/icons-material/GppBadRounded";
import AddModeratorRoundedIcon from "@mui/icons-material/AddModeratorRounded";
import PolicyRoundedIcon from "@mui/icons-material/PolicyRounded";
import WidgetsRoundedIcon from "@mui/icons-material/WidgetsRounded";
import ManageAccountsRoundedIcon from "@mui/icons-material/ManageAccountsRounded";
import StorageRoundedIcon from "@mui/icons-material/StorageRounded";
import SettingsRoundedIcon from "@mui/icons-material/SettingsRounded";
import InsertChartRoundedIcon from "@mui/icons-material/InsertChartRounded";
import DocumentScannerRoundedIcon from "@mui/icons-material/DocumentScannerRounded";
import ContactPageRoundedIcon from "@mui/icons-material/ContactPageRounded";
import { Link } from "react-router-dom";
import { useContext } from "react";
import { DarkModeContext } from "../../context/darkModeContext";
import "./sidebar.scss";

// FIXME darkMode nie działa na tym elemencie
const Sidebar = () => {
  const { dispatch } = useContext(DarkModeContext);

  return (
    <div className="sidebar">
      <div className="top">
        <Link to="/">
          <span className="logoName">sarenka</span>
        </Link>
      </div>
      <hr />
      <div className="center">
        <ul>
          <Link to="/">
            <li>
              <DashboardRoundedIcon className="icon" />
              <span>home</span>
            </li>
          </Link>
          <p className="title">main</p>
          <Link to="/vulns">
            <li>
              <GppBadRoundedIcon className="icon" />
              <span>vulnerabilities</span>
            </li>
          </Link>
          <Link to="/vulns/new">
            <li>
              <AddModeratorRoundedIcon className="icon" />
              <span>add vulnerability</span>
            </li>
          </Link>
          <Link to="/">
            <li>
              <PolicyRoundedIcon className="icon" />
              <span>search</span>
            </li>
          </Link>
          <Link to="/">
            <li>
              <WidgetsRoundedIcon className="icon" />
              <span>software</span>
            </li>
          </Link>
          <p className="title">settings</p>
          <Link to="/">
            <li>
              <ManageAccountsRoundedIcon className="icon" />
              <span>user credentials</span>
            </li>
          </Link>
          <Link to="/">
            <li>
              <SettingsRoundedIcon className="icon" />
              <span>settings</span>
            </li>
          </Link>
          <p className="title">statistics</p>
          <Link to="/">
            <li>
              <StorageRoundedIcon className="icon" />
              <span>database status</span>
            </li>
          </Link>
          <Link to="/">
            <li>
              <InsertChartRoundedIcon className="icon" />
              <span>summary</span>
            </li>
          </Link>
          <p className="title">Notes</p>
          <Link to="/">
            <li>
              <DocumentScannerRoundedIcon className="icon" />
              <span>public</span>
            </li>
          </Link>
          <Link to="/">
            <li>
              <ContactPageRoundedIcon className="icon" />
              <span>my notes</span>
            </li>
          </Link>
        </ul>
      </div>
      <div className="bottom">
        <div
          className="colorOption"
          onClick={() => dispatch({ type: "LIGHT" })}
        ></div>
        <div
          className="colorOption"
          onClick={() => dispatch({ type: "DARK" })}
        ></div>
      </div>
      <footer className="logoFooter">
        <div className="logoContainer">
          <img src={process.env.PUBLIC_URL + "images/logo_cropped.png"} />
        </div>
      </footer>
    </div>
  );
};

export default Sidebar;
