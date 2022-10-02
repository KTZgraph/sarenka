import { useState } from "react";
import { Link } from "react-router-dom";
import ArrowForwardIosIcon from "@mui/icons-material/ArrowForwardIos";
import ArrowBackIosIcon from "@mui/icons-material/ArrowBackIos";

import { rowsPerPageOptions } from "./vulnerability-options";
import Dropdown from "../../../UI/Dropdown";
import "./VulnerabilitiesTable.scss";

const CVSS = ({ score }) => {
  if (score === 0 || !score) return;

  let statusClassName = "";

  if (score >= 9.0) {
    statusClassName = "cvss--critical";
  } else if (score < 9.0 && score >= 7.0) {
    statusClassName = "cvss--high";
  } else if (score < 7.0 && score >= 4.0) {
    statusClassName = "cvss--medium";
  } else if (score < 4.0) {
    statusClassName = "cvss--low";
  } else {
    statusClassName = "";
  }

  return (
    <div className={`cvss ${statusClassName}`}>
      <p>{score}</p>
    </div>
  );
};

const VulnerabilityRow = ({ vuln }) => {
  return (
    <tr className="vulnerability-table__tbody-tr">
      <td className="vulnerability-table__td">
        <input
          type="checkbox"
          // onChange={(e) => handleChange(e, vuln.id, vuln.code)}
          id={vuln.id}
          name={vuln.id}
        />
      </td>
      <td className="vulnerability-table__td vulnerability-table__score-item">
        <CVSS score={vuln.base_metric_v2.cvss_v2.base_score} />
        <CVSS score={vuln.base_metric_v3.cvss_v3.base_score} />
        <CVSS score={vuln.base_metric_v4?.cvss_v4?.base_score} />
      </td>
      <td className="vulnerability-table__td vulnerability-table__cwe-item vulnerability-table__cwe-item-key">
        <Link to={`/vulnerabilities/cwes/${vuln.cwe_code}`}>
          {vuln.cwe_code}
        </Link>
      </td>
      <td className="vulnerability-table__td vulnerability-table__cve-item">
        <Link to={`/vulnerabilities/${vuln.id}`}>
          <span className="vulnerability-table__cve-key">{vuln.code}</span>
        </Link>
      </td>
      <td className="vulnerability-table__td">{vuln.description}</td>
    </tr>
  );
};

const VulnerabilitiesTable = ({
  vulnerabilities,
  pageNumber,
  setPageNumber,
}) => {
  const [rowsPerPage, setRowsPerPage] = useState(100);

  return (
    <table className="vulnerability-table">
      {/* nagłówek tabelki */}
      <thead className="vulnerability-table__thead">
        <tr className="vulnerability-table__thead-tr">
          <th className="vulnerability-table__th">
            <input
              type="checkbox"
              onClick={() => console.log("checkbox click")}
            />
          </th>
          <th className="vulnerability-table__th vulnerability-table__score">
            CVSS Score
          </th>
          <th className="vulnerability-table__th vulnerability-table__cwe-item">
            CWE
          </th>
          <th className="vulnerability-table__th vulnerability-table__cve">
            CVE
          </th>
          <th className="vulnerability-table__th">Description</th>
        </tr>
      </thead>

      {/* ciało tabelki */}
      <tbody className="vulnerability-table__tbody">
        {vulnerabilities &&
          vulnerabilities.map((vuln) => (
            <VulnerabilityRow key={vuln.id} vuln={vuln} />
          ))}
      </tbody>

      {/* paginacja */}
      <tr className="vulnerability-table__pagination">
        {/* checkbox */}
        <td className="vulnerability-table__td">
          <input type="checkbox" />
        </td>

        {/* ilosc elemntów tabelce */}
        <td colSpan="2">
          <Dropdown
            className="vulnerability-table__rows-number"
            label="Rows per page"
            options={rowsPerPageOptions}
            value={rowsPerPage}
            onChange={(e) => setRowsPerPage(e.target.value)}
          />
        </td>

        <td colSpan="2">
          <div className="vulnerability-table__actions">
            {/* przejscie do strony o numerze, strzałeczki */}

            <Dropdown
              className="vulnerability-table__rows-number"
              label="Go to page"
              options={rowsPerPageOptions}
              value={rowsPerPage}
              onChange={(e) => setRowsPerPage(e.target.value)}
            />
            {/* strzałeczki */}

            <div className="vulnerability-table__arrows">
              <ArrowBackIosIcon
                className="plugins-table__arrow"
                onClick={() => {
                  setPageNumber(pageNumber - 1);
                  console.log(pageNumber);
                }}
              />
              <ArrowForwardIosIcon
                className="plugins-table__arrow"
                onClick={() => {
                  setPageNumber(pageNumber + 1);
                  console.log(pageNumber);
                }}
              />
            </div>
          </div>
        </td>
      </tr>
    </table>
  );
};

export default VulnerabilitiesTable;
