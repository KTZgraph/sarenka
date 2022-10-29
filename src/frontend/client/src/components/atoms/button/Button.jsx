// https://github.com/danilowoz/react-atomic-design/blob/master/src/components/atoms/button/index.js

// https://github.com/WebDevSimplified/storybook-react-crash-course/blob/main/src/components/Button.js
import PropTypes from "prop-types";

function Button({ label, backgroundColor = "red", size = "md", handleClick }) {
  let scale = 1;
  if (size === "sm") scale = 0.75;
  if (size === "lg") scale = 1.5;
  const style = {
    backgroundColor,
    padding: `${scale * 0.5}rem ${scale * 1}rem`,
    border: "none",
  };
  return (
    <button onClick={handleClick} style={style}>
      {label}
    </button>
  );
}

// stąd pochodzi dokuemntacja w
//localhost:6006/?path=/story/button--red
http: Button.propTypes = {
  label: PropTypes.string,
  backgroundColor: PropTypes.string,
  size: PropTypes.oneOf(["sm", "md", "lg"]),
  handleClick: PropTypes.func,
};

export default Button;
