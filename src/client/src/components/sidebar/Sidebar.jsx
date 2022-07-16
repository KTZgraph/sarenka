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
import styles from "./Sidebar.module.scss";

const Sidebar = () => {
  return (
    <div className={`${styles.sidebar} wrapper`}>
      <div className={styles.top}>
        <span className={styles.logoName}>sarenka</span>
      </div>
      <hr />
      <div className={styles.center}>
        <ul>
          <li>
            <DashboardRoundedIcon className={styles.icon} />
            <span>home</span>
          </li>
          <p className={styles.title}>main</p>
          <li>
            <GppBadRoundedIcon className={styles.icon} />
            <span>vulnerabilities</span>
          </li>
          <li>
            <AddModeratorRoundedIcon className={styles.icon} />
            <span>add vulnerability</span>
          </li>
          <li>
            <PolicyRoundedIcon className={styles.icon} />
            <span>search</span>
          </li>
          <li>
            <WidgetsRoundedIcon className={styles.icon} />
            <span>software</span>
          </li>
          <p className={styles.title}>settings</p>
          <li>
            <ManageAccountsRoundedIcon className={styles.icon} />
            <span>user credentials</span>
          </li>

          <li>
            <SettingsRoundedIcon className={styles.icon} />
            <span>settings</span>
          </li>

          <p className={styles.title}>statistics</p>
          <li>
            <StorageRoundedIcon className={styles.icon} />
            <span>database status</span>
          </li>
          <li>
            <InsertChartRoundedIcon className={styles.icon} />
            <span>summary</span>
          </li>
          <p className={styles.title}>Notes</p>
          <li>
            <DocumentScannerRoundedIcon className={styles.icon} />
            <span>public</span>
          </li>
          <li>
            <ContactPageRoundedIcon className={styles.icon} />
            <span>my notes</span>
          </li>
        </ul>
      </div>
      <div className={styles.bottom}>
        <div className={styles.colorOption}></div>
        <div className={styles.colorOption}></div>
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
