import classes from './cwe-content.module.css';

function CWEContent(props) {
  return (
    <section className={classes.content}>
      {props.children}
    </section>
  );
}

export default CWEContent;
