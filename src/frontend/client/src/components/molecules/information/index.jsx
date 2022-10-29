import styles from "./style.scss";
import classnames from "classnames";

export const InformationType = {
  INFO: "info",
  ALERT: "alert",
  ERROR: "error",
};

export const InformationTheme = {
  DEFAULT: "default",
  ROUNDED: "rounded",
};

export const InformationSize = {
  SMALL: "small",
  MEDIUM: "medium",
  LARGE: "large",
};

const Information = (props) => {
  const { type, name, info, theme, size, className } = props;

  const classProps = classnames(
    // styles.button,
    styles[theme],
    styles[size],

    className
  );

  return (
    <div type={type} className={classProps}>
      <span className="name">{name}:</span>
      <p className="info">{info}</p>
    </div>
  );
};

// typy przycisków
Information.defaultProps = {
  type: InformationType.INFO,
  theme: InformationTheme.DEFAULT,
  size: InformationSize.LARGE,
  className: "",
};

export default Information;
