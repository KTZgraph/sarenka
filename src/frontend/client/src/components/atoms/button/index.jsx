import classnames from "classnames";
import styles from "./style.scss";

export const ButtonType = {
  BUTTON: "button",
  SUBMIT: "submit",
  VIEW: "view",
  UPDATE: "update",
  DELETE: "delete",
};

export const ButtonTheme = {
  DEFAULT: "default",
  ROUNDED: "rounded",
};

export const ButtonSize = {
  SMALL: "small",
  MEDIUM: "medium",
  LARGE: "large",
};

const Button = (props) => {
  const { children, type, onClick, theme, size, className, disabled } = props;

  const classProps = classnames(
    styles.button,
    styles[theme],
    styles[size],
    {
      [styles.disabled]: disabled,
    },
    className
  );

  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={classProps}
    >
      {children}
    </button>
  );
};

Button.defaultProps = {
  type: ButtonType.BUTTON,
  theme: ButtonTheme.DEFAULT,
  size: ButtonSize.LARGE,
  onClick: () => {},
  className: "",
  disabled: false,
};

export default Button;
