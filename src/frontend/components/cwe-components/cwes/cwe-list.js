// react component
// notacja event-list zamiast EventList jak w czystym Reacie żeby rozpoznbnać które to komponenty Reacta a które Nexta
// indywidualnie mozna taki tak nazywać
import CWEItem from "./cwe-item";
import classes from './cwe-list.module.css';

function CWEList(props) {
  // props - eventy są z zewnątrz poprzekazane dane
  const { cwes } = props;

  return (
    <ul className={classes.list}>
      {cwes.map((cwe) => (
        //   pamieać o key,które jest wymagane przez REact!
        <CWEItem
          key={cwe.id}
          id={cwe.id}
          name={cwe.name}
          abstraction={cwe.abstraction}
          structure={cwe.structure}
          status={cwe.status}
          description={cwe.description}
          extendedDescription={cwe.extended_description}
        />
      ))}
    </ul>
  );

}


export default CWEList;
