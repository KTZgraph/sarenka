import { Link } from "react-router-dom";
import classnames from "classnames";
import styles from "./style.scss";

export const NavigationType = {
  DEFAULT: "default",
  VIEW: "view",
  CREATE: "create",
  UPDATE: "update",
  DELETE: "delete",
};

export const NavigationTheme = {
  DEFAULT: "default",
  ROUNDED: "rounded",
};

export const NavigationSize = {
  SMALL: "small",
  MEDIUM: "medium",
  LARGE: "large",
};

const Navigation = (props) => {
  const { children, type, to, theme, size, className, disabled } = props;

  const classProps = classnames(
    styles[theme],
    styles[size],
    {
      [styles.disabled]: disabled,
    },
    className
  );

  return (
    <Link to={to} type={type} disabled={disabled} className={classProps}>
      {children}
    </Link>
  );
};

Navigation.defaultProps = {
  type: NavigationType.DEFAULT,
  theme: NavigationTheme.DEFAULT,
  size: NavigationSize.LARGE,
  to: "/",
  className: "",
  disabled: false,
};

export default Navigation;
