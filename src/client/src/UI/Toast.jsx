/*
https://www.youtube.com/watch?v=5ORd2kPpugw
*/

import { useContext } from "react";
import {
  FaCheck,
  FaExclamationCircle,
  FaExclamationTriangle,
  FaInfoCircle,
  FaRegWindowClose,
} from "react-icons/fa";

import { ToastContext } from "../context/ToastContext";

const Toast = ({ position, autoDeleteInterval }) => {
  const { state, dispatch } = useContext(ToastContext);

  const generateIcon = (type) => {
    switch (type) {
      case "INFO":
        return <FaInfoCircle />;
      case "WARNING":
        return <FaExclamationTriangle />;
      case "DANGER":
        return <FaExclamationCircle />;
      case "SUCCESS":
        return <FaCheck />;
      default:
        return;
    }
  };

  const generateBackgroundColor = (type) => {
    switch (type) {
      case "INFO":
        return "gray";
      case "WARNING":
        return "yellow";
      case "DANGER":
        return "orange";
      case "SUCCESS":
        return "red";
      default:
        return;
    }
  };

  return (
    <div className={`notification-container ${position}`}>
      {state.map((notification, idx) => {
        if (autoDeleteInterval) {
          setInterval(() => {
            dispatch({
              type: "DELETE_NOTIFICATION",
              payload: notification.id,
            });
          }, autoDeleteInterval);
        }
        return (
          <div
            key={notification.id}
            style={{
              backgroundColor: generateBackgroundColor(notification.type),
            }}
            className="notification toast"
          >
            <FaRegWindowClose
              onClick={() =>
                dispatch({
                  type: "DELETE_NOTIFICATION",
                  payload: notification.id,
                })
              }
              className="notification-close"
            />
            <div className="notification-image">
              {generateIcon(notification.type)}
            </div>
            <div>
              <p className="notification-title">{notification.title}</p>
              <p className="notification-message">{notification.message}</p>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default Toast;
