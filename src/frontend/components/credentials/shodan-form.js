import useTranslation from "next-translate/useTranslation";
import Link from "next/link";
import { useState } from "react";

import classes from "./shodan-form.module.css";

function ShodanForm(props) {
  let { t } = useTranslation();

  const [enteredUsername, setEnteredUsername] = useState("");
  const [enteredApiKey, setEnteredApiKey] = useState("");

  function submitHandler(event) {
    event.preventDefault();
    // można na kliencie walidacje danych

    props.onChangeCredentials({
      shodanUsername: enteredUsername,
      shodanApiKey: enteredApiKey,
    });
  }

  return (
    <section className={classes.section}>
      <h1>Shodan API</h1>
      <form className={classes.form} onSubmit={submitHandler}>
        <div className={classes.credentials}>
          <div className={classes.credential}>
            <label htmlFor="username">{t("credentials:shodanUsername")}</label>
            <input
              type="text"
              id="username"
              placeholder={t("credentials:shodanUsernamePlaceholder")}
              required={true}
              value={enteredUsername}
              onChange={(event) => setEnteredUsername(event.target.value)}
            />
          </div>
          <div className={classes.credential}>
            <label htmlFor="apiKey">{t("credentials:shodanApiKey")}</label>
            <input
              type="text"
              id="apiKey"
              required={true}
              value={enteredApiKey}
              placeholder={t("credentials:shodanApiKeyPlaceholder")}
              onChange={(event) => setEnteredApiKey(event.target.value)}
            />
          </div>
        </div>

        <div className={classes.actions}>
          <button className={classes.action}>{t("common:save")}</button>
          <Link href="https://account.shodan.io/">
            <a className={classes.source}>{t("common:account")}</a>
          </Link>
        </div>
      </form>
    </section>
  );
}

export default ShodanForm;
