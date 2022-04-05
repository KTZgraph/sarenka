import { useRef, useState, useContext } from "react";
import useTranslation from "next-translate/useTranslation";

import classes from "./search-form.module.css";
import ArrowRightIcon from "../icons/arrow-right-icon";
import ShodanData from "./shodan-data/shodan-data";
import NotificationContext from "../../store/notification-context";

function SearchForm() {
  const notificationCtx = useContext(NotificationContext);

  let { t } = useTranslation();

  const searchRef = useRef();
  const [shodanData, setShodanData] = useState();

  async function submitHandler(event) {
    event.preventDefault();

    const enteredSearch = searchRef.current.value;

    // walidacja po stronie klienta
    if (!enteredSearch || enteredSearch.trim() === "") {
      console.log("ip address is empty");
      return;
    }
    notificationCtx.showNotification({
      title: "Search",
      message: "Geting data from shodan",
      status: "pendind",
    });

    const response = await fetch("/api/search", {
      method: "POST",
      body: JSON.stringify({ ipAddress: enteredSearch }),
      headers: {
        "Content-Type": "application/json",
      },
    });

    try {
      const data = await response.json(); // też zwraca Promise
      if (!response.ok) {
        // throw new Error(data.message || "Something went wrong");
        notificationCtx.showNotification({
          title: "Error",
          message: data.message || "Couldn't get data from shodan",
          status: "error",
        });
      } else {
        setShodanData(JSON.stringify(data)); //nie moze obiektu - musi być jsona
        notificationCtx.showNotification({
          title: "Success",
          message: "Data from shodan are fetched correctly",
          status: "success",
        });
      }
    } catch (error) {
      notificationCtx.showNotification({
        title: "Error",
        message: error.message || "Couldn't get data from shodan",
        status: "error",
      });
    }
  }

  return (
    <section className={classes.section}>
      <h2>{t("search:search")}</h2>

      <form className={classes.form} onClick={submitHandler}>
        <div className={classes.userSearch}>
          <label htmlFor="userSearch"></label>
          <input
            type="text"
            id="userSearch"
            placeholder="input ip address"
            required
            ref={searchRef}
          />
          <button className={classes.action}>
            <span className={classes.icon}>
              <ArrowRightIcon />
            </span>
          </button>
        </div>
      </form>

      {/* dane z shodana */}
      {shodanData && <ShodanData data={shodanData} />}
    </section>
  );
}

export default SearchForm;