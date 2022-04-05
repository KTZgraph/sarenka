// chronione - przekierować jeśli użytkownik not authenticated
import { useContext } from "react";
import useTranslation from "next-translate/useTranslation";

import ChangePasswordForm from "./change-password-form";
import ShodanForm from "./shodan-form";
import classes from "./credentials.module.css";
import NotificationContext from "../../store/notification-context";

function Credentials() {
  let { t } = useTranslation();
  // do notyfikacji
  const notificationCtx = useContext(NotificationContext);

  //wyrenderuje się jak jest zalogowany - tego pilnuje /pages/credentials.js w getServerSideProps logice
  async function changePasswordHandler(passwordData) {
    notificationCtx.showNotification({
      title: "Changing user password",
      message: "Saving new user password",
      status: "pendind",
    });

    const response = await fetch("/api/user/change-password", {
      method: "PATCH",
      body: JSON.stringify(passwordData),
      headers: {
        "Content-Type": "application/json",
      },
    });

    try {
      const data = await response.json();
      if (!response.ok) {
        console.log(data);
        throw new Error(data.message || "Something went wrong");
      }

      notificationCtx.showNotification({
        title: "Success",
        message: "Succesfuly changed user password",
        status: "success",
      });
    } catch (error) {
      notificationCtx.showNotification({
        title: "Error",
        message: error.message || "Couldn't change user password",
        status: "error",
      });
    }
  }

  async function changeShodanCredentialsHandler(credentialsData) {
    notificationCtx.showNotification({
      title: "Shodan Credentials",
      message: "Saving credeniatls for shodan",
      status: "pendind",
    });

    const response = await fetch("/api/user/shodan-credentials", {
      method: "PATCH",
      body: JSON.stringify(credentialsData),
      headers: {
        "Content-Type": "application/json",
      },
    });

    try {
      const data = await response.json();
      if (!response.ok) {
        console.log(data);
        throw new Error(data.message || "Something went wrong");
      }
      notificationCtx.showNotification({
        title: "Success",
        message: "Succesfuly saved credentials for shodan",
        status: "success",
      });
    } catch (error) {
      notificationCtx.showNotification({
        title: "Error",
        message: error.message || "Couldn't save shodan credentials",
        status: "error",
      });
    }
  }

  return (
    <div className={classes.credentials}>
      <h2>{t("credentials:credentials")}</h2>
      <div className={classes.credentialItems}>
        <ChangePasswordForm onChangePassword={changePasswordHandler} />
        <ShodanForm onChangeCredentials={changeShodanCredentialsHandler} />
      </div>
    </div>
  );
}

export default Credentials;
