/*
https://www.youtube.com/watch?v=bPNkdoEqfVY&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=16
*/

import { useState } from "react";
import FilteringVisually from "./FilteringVisually";
import FilteringVisuallyChild from "./FilteringVisuallyChild";

const FilteringVisuallyApp = () => {
  //   const [data, setData] = useState([10, 25, 30, 40, 25, 60]);
  const [data, setData] = useState(
    Array.from({ length: 30 }).map(() => Math.round(Math.random() * 100))
  );

  const onAddDataClick = () => {
    setData([...data, Math.round(Math.random() * 100)]);
  };

  return (
    <div style={{ minHeight: "90vh" }}>
      <h2>Sub-selections with d3-brush</h2>

      <FilteringVisually data={data}>
        {/* {(selection) => (
          // dziecko komponentu
          <FilteringVisuallyChild data={data} selection={selection} />
        )} */}
        {/* WARNING - funckja jako dizecko - komponet funcktujny żeby przekazać wartości do dizeckza */}
        {/* argument z  FilteringVisually przekazany do dziecka jest dostępny w callbacku*/}
        {(selection) => (
          <FilteringVisuallyChild data={data} selection={selection} />
        )}
      </FilteringVisually>
      <button onClick={onAddDataClick}>Add data</button>
    </div>
  );
};

export default FilteringVisuallyApp;
