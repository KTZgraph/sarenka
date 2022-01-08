import Button from "../../ui/button";
import ArrowRightIcon from "../../icons/arrow-right-icon";
import classes from "./cwe-item.module.css";

function CWEItem(props) {
  const {
    id,
    name,
    abstraction,
    structure,
    status,
    description,
    extendedDescription,
  } = props;

  // konstrukcja linku do konkretnego cwe po id
  const exploreCWE = `/vulns/cwe/${id}`;

  // dla konkrentych danych
  return (
    <li className={classes.item}>
      <div className={classes.content}>
        <div className={classes.summary}>
          <h2>{id}</h2>
          <h3>{name}</h3>
          <p>{description}</p>
        </div>
        
        
        <div className={classes.actions}>
          {/* technicznie to dalej <Link ale będzie wygladac jak przycisk */}
          <Button link={exploreCWE}>
            <span>Explore Event</span>
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
