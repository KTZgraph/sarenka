import { createContext, useState, useEffect } from "react";

// nazwa z wielkiej żeby było wiadomo, że można Providera wyciągnąć
const NotificationContext = createContext({
  notification: null, //{title, messsage, status}
  showNotification: function (notificationData) {}, //inicjalizacyjnie pusta punckja
  hideNotification: function () {},
});

export function NotificationContextProvider(props) {
  const [activeNotification, setActiveNotification] = useState();

  // useEffect żeby reagowała od razu na zmiany
  useEffect(() => {
    if (
      activeNotification &&
      (activeNotification.status === "success" ||
        activeNotification.status === "error")
    ) {
      const timer = setTimeout(() => {
        setActiveNotification(null);
      }, 3000);

      // clenup funkcja
      return () => {
        // czyszczenie timera jeśli useEffect ponownie się uruchomi zanim timer 3s się skońcyz/wyłączy - żeby nie było wielu timerów w tym samym czasie
        clearTimeout(timer);
      };
    } //jak warunek nie spełniony to useEffect nic nie robi
  }, [activeNotification]); //dependency to activeNotification

  function showNotificationHandler(notificationData) {
    setActiveNotification(notificationData);
  }

  function hideNotificationHandler() {
    setActiveNotification(null);
  }

  // poniższy obiekt rozdytrubuuję do wszsytkich zainteresowanych komponentów
  const context = {
    notification: activeNotification,
    showNotification: showNotificationHandler,
    hideNotification: hideNotificationHandler,
  };

  return (
    <NotificationContext.Provider value={context}>
      {props.children}
    </NotificationContext.Provider>
  );
}

export default NotificationContext;