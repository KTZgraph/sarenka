import Link from "next/link";
import useTranslation from "next-translate/useTranslation";

import classes from "./main-menu.module.css";
import AppImage from "./app-image";

function MainMenu() {
  let { t } = useTranslation();


  return (
    <nav className={classes.sidebar}>
      {/* Hamburger menu */}
      <div className={classes.hamburgerMenu}>
        <div className={[classes.line, classes.line1].join(" ")}></div>
        <div className={[classes.line, classes.line2].join(" ")}></div>
        <div className={[classes.line, classes.line3].join(" ")}></div>
      </div>
      {/* logo aplikacji */}
      {/* <AppImage userEmail={session.user.email} /> */}
      <AppImage userEmail={'UserEmailValue'} />
      <ul className={classes.list}>


      <li className={classes.item}>
            <Link href="/">
              <a className={classes.link}>
                <span className={classes.text}>{t("common:search")}</span>
              </a>
            </Link>
          </li>

        <li className={classes.item}>
          <Link href="/cwe">
            <a className={classes.link}>
              <span className={classes.text}>{t("common:cweList")}</span>
            </a>
          </Link>
        </li>

        <li className={classes.item}>
          <Link href="/cve">
            <a className={classes.link}>
              <span className={classes.text}>{t("common:cveList")}</span>
            </a>
          </Link>
        </li>

        {/* link widoczny tylko dla zalogowanych */}
          <li className={classes.item}>
            <Link href="/credentials">{t("common:credentials")}</Link>
          </li>
      </ul>
    </nav>
  );
}

export default MainMenu;