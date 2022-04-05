import useTranslation from "next-translate/useTranslation";
import { useRef } from "react";

import classes from "./change-password-form.module.css";

function ChangePasswordForm(props) {
  let { t } = useTranslation();

  const oldPasswordRef = useRef("");
  const newPasswordRef = useRef("");

  function submitHandler(event) {
    event.preventDefault();

    const enteredOldPassword = oldPasswordRef.current.value;
    const enteredNewPassword = newPasswordRef.current.value;
    // walidacja po stronie klienta TODO

    // funckja z komponentu rodzica
    props.onChangePassword({
      oldPassword: enteredOldPassword,
      newPassword: enteredNewPassword,
    });
  }

  return (
    <section className={classes.section}>
      <h1>{t("credentials:changePassword")}</h1>
      <form className={classes.form} onSubmit={submitHandler}>
        <div className={classes.credentials}>
          <div className={classes.credential}>
            <label htmlFor="oldPassword">{t("credentials:oldPassword")}</label>
            <input
              type="password"
              id="oldPassword"
              placeholder={t("credentials:oldPasswordPlaceholder")}
              required={true}
              ref={oldPasswordRef}
            />
          </div>
          <div className={classes.credential}>
            <label htmlFor="newPassword">{t("credentials:newPassword")}</label>
            <input
              type="password"
              id="password"
              required={true}
              ref={newPasswordRef}
              placeholder={t("credentials:newPasswordPlaceholder")}
            />
          </div>
        </div>

        <div className={classes.actions}>
          <button className={classes.action}>{t("common:save")}</button>
        </div>
      </form>
    </section>
  );
}

export default ChangePasswordForm;
