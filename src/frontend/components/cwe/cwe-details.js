import useTranslation from "next-translate/useTranslation";

import classes from "./cwe-details.module.css";
import Button from "../../components/ui/button";

function CWEDetails(props) {
  let { t } = useTranslation();

  return (
    <div className={classes.content}>
      <h2>{props.id}</h2>
      <p>
        <span>{t("common:name")}:</span>
        {props.name}
      </p>
      <p>
        <span>{t("common:abstraction")}:</span>
        {props.abstraction}
      </p>
      <p>
        <span>{t("common:structure")}:</span>
        {props.structure}
      </p>
      <p>
        <span>{t("common:status")}:</span>
        {props.status}
      </p>
      <p>
        <span>{t("common:description")}:</span>
        {props.description}
      </p>
      <p>
        <span>{t("common:extendedDescription")}:</span>
        {props.extended_description}
      </p>

      <ul className={classes.actions}>
        {props.cveList.map((cveId) => (
          <li key={cveId}>
            <Button link={`/cve/${cveId}`}>{cveId}</Button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CWEDetails;
