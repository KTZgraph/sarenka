/*
https://www.youtube.com/watch?v=bPNkdoEqfVY&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=16
*/

import { useState } from "react";
import FilteringVisually from "./FilteringVisually";

const FilteringVisuallyApp = () => {
  const [data, setData] = useState([10, 25, 30, 40, 25, 60]);

  const onAddDataClick = () => {
    setData([...data, Math.round(Math.random() * 100)]);
  };

  return (
    <>
      <h2>Sub-selections with d3-brush</h2>

      <FilteringVisually data={data} />
      <button onClick={onAddDataClick}>Add data</button>
    </>
  );
};

export default FilteringVisuallyApp;
