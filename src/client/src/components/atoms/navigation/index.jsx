import { Link } from "react-router-dom";
import classnames from "classnames";
import styles from "./style.scss";

// do przeklikiwania się w apcje
// np klikviecie na konretne cve żeby przejsć do strony
export const NavigationType = {
  DEFAULT: "default",
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
  const { type, to, children, theme, size, className, disabled } = props;

  const classProps = classnames(
    // styles.action,
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

// typy przycisków
Navigation.defaultProps = {
  type: NavigationType.DEFAULT,
  theme: NavigationTheme.DEFAULT,
  size: NavigationSize.LARGE,
  to: "/",
  className: "",
  disabled: false,
};

export default Navigation;
