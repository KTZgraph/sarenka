import classes from './cwe-summary.module.css';

function CWESummary(props) {
  const { title } = props;

  return (
    <section className={classes.summary}>
      <h1>{title}</h1>
    </section>
  );
}

export default CWESummary;