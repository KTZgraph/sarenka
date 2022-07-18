import { useContext } from "react";
import LanguageOutlinedIcon from "@mui/icons-material/LanguageOutlined";
import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import DarkModeOutlinedIcon from "@mui/icons-material/DarkModeOutlined";
import FullscreenExitOutlinedIcon from "@mui/icons-material/FullscreenExitOutlined";
import NotificationsNoneOutlinedIcon from "@mui/icons-material/NotificationsNoneOutlined";
import ChatBubbleOutlineOutlinedIcon from "@mui/icons-material/ChatBubbleOutlineOutlined";
import ListOutlinedIcon from "@mui/icons-material/ListOutlined";
import { DarkModeContext } from "../../context/darkModeContext";
import styles from "./Navbar.module.scss";
// FIXME darkMode nie działa na tym elemencie
const Navbar = () => {
  const { dispatch } = useContext(DarkModeContext);

  return (
    <div className={styles.navbar}>
      <div className={styles.navbarContainer}>
        <div className={styles.search}>
          {/* serach input */}
          <input type="text" placeholder="Search..." />
          <SearchOutlinedIcon className={styles.searchIcon} />
        </div>
        <div className={styles.items}>
          {/* language options */}
          <div className={styles.item}>
            <LanguageOutlinedIcon className={styles.icon} />
            English
          </div>
          <div className={styles.item}>
            <DarkModeOutlinedIcon
              className={styles.icon}
              onClick={() => dispatch({ type: "TOOGLE" })}
            />
          </div>
          <div className={styles.item}>
            <FullscreenExitOutlinedIcon className={styles.icon} />
          </div>
          <div className={styles.item}>
            {/* notyfikacje powiadomienia */}
            <NotificationsNoneOutlinedIcon className={styles.icon} />
            <div className={styles.counter}>1</div>
          </div>
          <div className={styles.item}>
            <ChatBubbleOutlineOutlinedIcon className={styles.icon} />
            <div className={styles.counter}>2</div>
          </div>
          <div className={styles.item}>
            <ListOutlinedIcon className={styles.icon} />
          </div>
          <div className={styles.item}>
            {/* avatar */}
            <img
              src="https://avatars.githubusercontent.com/u/16176980?s=400&u=5054d0c27442f6a3eed09b1d78292128c8a80686&v=4"
              alt=""
              className={styles.avatar}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
