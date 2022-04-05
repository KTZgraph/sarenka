import Link from "next/link";
import { useRouter } from "next/router";

import classes from "./language-switcher.module.css";

function LanguageSwitcher() {
  let router = useRouter();

  return (
    <div className={classes.languages}>
      {router.locales.map((locale) => (
        <Link href={router.asPath} locale={locale} key={locale}>
          <a
            className={`${
              locale === router.locale
                ? [classes.active, classes.btn].join(" ")
                : classes.btn
            }`}
          >
            {locale}
          </a>
        </Link>
      ))}
    </div>
  );
}

export default LanguageSwitcher;