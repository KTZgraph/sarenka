import KeyboardArrowUpIcon from "@mui/icons-material/KeyboardArrowUp";
import PersonOutlineIcon from "@mui/icons-material/PersonOutline";
import AccountBalanceWalletIcon from "@mui/icons-material/AccountBalanceWallet";
import ShoppingCartOutlinedIcon from "@mui/icons-material/ShoppingCartOutlined";
import MonetizationOnOutlinedIcon from "@mui/icons-material/MonetizationOnOutlined";

import styles from "./Widget.module.scss";

const Widget = ({ type }) => {
  let data;
  //TODO temporary
  const amount = 100;
  const diff = 20;

  switch (type) {
    case "user":
      data = {
        title: "USERS",
        isMoney: false,
        link: "See all users",
        icon: (
          <PersonOutlineIcon
            className={styles.icon}
            style={{ color: "crimson" }}
          />
        ),
      };
      break;
    default:
      break;
    case "order":
      data = {
        title: "ORDERS",
        isMoney: false,
        link: "View all orders",
        icon: (
          <ShoppingCartOutlinedIcon
            className={styles.icon}
            style={{ color: "goldenrod" }}
          />
        ),
      };
      break;
    case "earnings":
      data = {
        title: "EARNINGS",
        isMoney: true,
        link: "View all earnings",
        icon: (
          <MonetizationOnOutlinedIcon
            className={styles.icon}
            style={{ color: "green" }}
          />
        ),
      };
      break;
    case "balance":
      data = {
        title: "BALANCE",
        isMoney: true,
        link: "See details",
        icon: (
          <AccountBalanceWalletIcon
            className={styles.icon}
            style={{ color: "purple" }}
          />
        ),
      };
      break;
  }

  return (
    <div className={styles.widget}>
      <div className={styles.left}>
        <div className={styles.title}>{data.title}</div>
        <div className={styles.counter}>
          {data.isMoney && "$"} {amount}
        </div>
        <div className={styles.link}>{data.link}</div>
      </div>
      <div className={styles.right}>
        <div className={`${styles.percentage} ${styles.negative}`}>
          <KeyboardArrowUpIcon />
          {diff} %
        </div>
        {data.icon}
      </div>
    </div>
  );
};

export default Widget;
