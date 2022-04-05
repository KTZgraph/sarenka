import Link from "next/link";
import useTranslation from "next-translate/useTranslation";

import classes from "./main-navigation.module.css";
import LanguageSwitcher from "./language-switcher";

function MainNavigation() {
  // do zmiany języka
  let { t } = useTranslation();


  function logoutHandler() {
    //zwraca promisa ale useSession się aktulizuje wiec tutaj nic nie robię
    //z automatu cookie z JWT się wyczyści
    // devtools -> Application -> cookies-> <serwer:port po lewej> -> next-auth.session.token
    signOut();
  }

  return (
    <header className={classes.header}>
      <LanguageSwitcher />
      <nav>
        <ul>
          {/* login tylko gdy niezalogowany - brak sesji i już dane są pobrane */}
            <li>
              <Link href="/auth">{t("common:login")}</Link>
            </li>

          {/* link widoczny tylko dla zalogowanych */}
            <li>
              <Link href="/credentials">{t("common:credentials")}</Link>
            </li>

          {/* logout tylko dla zalogowanych - gdy jest sesja */}
            <li>
              <button onClick={logoutHandler}>{t("common:logout")}</button>
            </li>
        </ul>
      </nav>
    </header>
  );
}

export default MainNavigation;