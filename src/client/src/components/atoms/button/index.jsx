import styles from "./style.scss";
import classnames from "classnames";

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
  const { type, onClick, children, theme, size, className, disabled } = props;

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

// typy przycisków
Button.defaultProps = {
  type: ButtonType.BUTTON,
  theme: ButtonTheme.DEFAULT,
  size: ButtonSize.LARGE,
  onClick: () => {},
  className: "",
  disabled: false,
};

export default Button;
