import classnames from "classnames";
import styles from "./style.scss";

const Title = (props) => (
  <h1 className={classnames(styles.title, props.className)}>
    {props.children}
  </h1>
);

Title.defaultProps = {
  className: "",
  children: "",
};

export default Title;
