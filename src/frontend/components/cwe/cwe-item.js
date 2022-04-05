import classes from "./cwe-item.module.css";
import Button from "../ui/button";
import ArrowRightIcon from "../icons/arrow-right-icon";

function CWEItem(props) {
  const { cwe } = props;

  // konstrukcja linku do konkretnego cwe po id
  const exploreCWE = `/cwe/${cwe.id}`;
  // dla konkrentych danych
  return (
    <li className={classes.item}>
      <div className={classes.content}>
        <div className={classes.summary}>
          <h2>{cwe.id}</h2>
          <h3>{cwe.name}</h3>
          <p>{cwe.description}</p>
        </div>

        <div className={classes.actions}>
          {/* technicznie to dalej <Link ale będzie wygladac jak przycisk */}
          <Button link={exploreCWE}>
            <span>Explore {cwe.id}</span>
            <span className={classes.icon}>
              <ArrowRightIcon />
            </span>
          </Button>
        </div>
      </div>
    </li>
  );
}

export default CWEItem;
