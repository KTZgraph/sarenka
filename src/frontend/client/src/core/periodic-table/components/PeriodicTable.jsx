/*
https://www.youtube.com/watch?v=c9nw5rWtMeQ
https://github.com/muratkemaldar/periodic-table-css
*/

import data from "./PeriodicTableJSON.json";
import "./PeriodicTable.scss";

const PeriodicTable = () => {
  return (
    <div className="periodic-table">
      {data.elements.map((element) => (
        <div
          key={element.name}
          style={{ gridColumn: element.xpos, gridRow: element.ypos }}
        >
          {element.symbol}
        </div>
      ))}
    </div>
  );
};

export default PeriodicTable;
