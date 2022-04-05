import { Fragment, useContext } from "react";

import MainNavigation from "./main-navigation";
import MainMenu from "./main-menu";
import Notification from "../ui/notification";
import NotificationContext from "../../store/notification-context"; //nie provider - tylko połączenie do obiketu defaultowego exportowanego

function Layout(props) {
  const notificationCtx = useContext(NotificationContext);

  const activeNotification = notificationCtx.notification; //jak nie jest nullem to pokazywać notyfikację

  return (
    <Fragment>
      <MainNavigation />
      <MainMenu />
      <main className="main">{props.children}</main>
      {/* notyfikacje dla każdego zainnteresowane komponentu - warunkowo*/}
      {activeNotification && (
        <Notification
          title={activeNotification.title}
          message={activeNotification.message}
          status={activeNotification.status}
        />
      )}
    </Fragment>
  );
}

export default Layout;