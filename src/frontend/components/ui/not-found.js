import Button from "./button";
import classes from "./not-found.module.css";

function NotFound() {
  return (
    <section className={classes.section}>
      <h1>404</h1>
      <p>This page could not be found.</p>
      <Button link={"/"}>Home</Button>
    </section>
  );
}

export default NotFound;