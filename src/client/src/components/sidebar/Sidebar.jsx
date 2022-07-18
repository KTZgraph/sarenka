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
import styles from "./Sidebar.module.scss";

// FIXME darkMode nie działa na tym elemencie
const Sidebar = () => {
  const { dispatch } = useContext(DarkModeContext);

  return (
    <div className={styles.sidebar}>
      <div className={styles.top}>
        <Link to="/">
          <span className={styles.logoName}>sarenka</span>
        </Link>
      </div>
      <hr />
      <div className={styles.center}>
        <ul>
          <Link to="/">
            <li>
              <DashboardRoundedIcon className={styles.icon} />
              <span>home</span>
            </li>
          </Link>
          <p className={styles.title}>main</p>
          <Link to="/vulns">
            <li>
              <GppBadRoundedIcon className={styles.icon} />
              <span>vulnerabilities</span>
            </li>
          </Link>
          <Link to="/vulns/new">
            <li>
              <AddModeratorRoundedIcon className={styles.icon} />
              <span>add vulnerability</span>
            </li>
          </Link>
          <Link to="/">
            <li>
              <PolicyRoundedIcon className={styles.icon} />
              <span>search</span>
            </li>
          </Link>
          <Link to="/">
            <li>
              <WidgetsRoundedIcon className={styles.icon} />
              <span>software</span>
            </li>
          </Link>
          <p className={styles.title}>settings</p>
          <Link to="/">
            <li>
              <ManageAccountsRoundedIcon className={styles.icon} />
              <span>user credentials</span>
            </li>
          </Link>
          <Link to="/">
            <li>
              <SettingsRoundedIcon className={styles.icon} />
              <span>settings</span>
            </li>
          </Link>
          <p className={styles.title}>statistics</p>
          <Link to="/">
            <li>
              <StorageRoundedIcon className={styles.icon} />
              <span>database status</span>
            </li>
          </Link>
          <Link to="/">
            <li>
              <InsertChartRoundedIcon className={styles.icon} />
              <span>summary</span>
            </li>
          </Link>
          <p className={styles.title}>Notes</p>
          <Link to="/">
            <li>
              <DocumentScannerRoundedIcon className={styles.icon} />
              <span>public</span>
            </li>
          </Link>
          <Link to="/">
            <li>
              <ContactPageRoundedIcon className={styles.icon} />
              <span>my notes</span>
            </li>
          </Link>
        </ul>
      </div>
      <div className={styles.bottom}>
        <div
          className={styles.colorOption}
          onClick={() => dispatch({ type: "LIGHT" })}
        ></div>
        <div
          className={styles.colorOption}
          onClick={() => dispatch({ type: "DARK" })}
        ></div>
      </div>
      <footer className={styles.logoFooter}>
        <div className={styles.logoContainer}>
          <img src={process.env.PUBLIC_URL + "images/logo_cropped.png"} />
        </div>
      </footer>
    </div>
  );
};

export default Sidebar;
