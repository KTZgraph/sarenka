import classes from "./spinner.module.css";

function Spinner() {
  return (
    <div className={classes.spinner}>
      <p>Loading ...</p>
    </div>
  );
}

export default Spinner;