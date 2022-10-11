/**
 * https://www.youtube.com/watch?v=bXN9anQN_kQ&list=PLDZ4p-ENjbiPo4WH7KdHjh_EMI7Ic8b2B&index=16
 */

import { useState } from "react";

import StackedBarChart from "./StackedBarChart";

const data = [
  {
    year: 1980,
    "🥑": 10,
    "🍌": 20,
    "🍆": 30,
  },
  {
    year: 1990,
    "🥑": 20,
    "🍌": 40,
    "🍆": 60,
  },
  {
    year: 2000,
    "🥑": 30,
    "🍌": 45,
    "🍆": 80,
  },
  {
    year: 2010,
    "🥑": 40,
    "🍌": 60,
    "🍆": 100,
  },
  {
    year: 2020,
    "🥑": 50,
    "🍌": 80,
    "🍆": 120,
  },
];

const allKeys = ["🥑", "🍌", "🍆"];

const colors = {
  "🥑": "green",
  "🍌": "orange",
  "🍆": "purple",
};

const StackedBarChartApp = () => {
  const [keys, setKeys] = useState(allKeys);
  return (
    <>
      <h2>Stacked Bar Chart with D3 </h2>
      <StackedBarChart data={data} keys={keys} colors={colors} />

      <div className="fields">
        {allKeys.map((key) => (
          <div key={key} className="field">
            <input
              id={key}
              type="checkbox"
              checked={keys.includes(key)}
              onChange={(e) => {
                if (e.target.checked) {
                  setKeys(Array.from(new Set([...keys, key])));
                } else {
                  setKeys(keys.filter((_key) => _key !== key));
                }
              }}
            />
            <label htmlFor={key} style={{ color: colors[key] }}>
              {key}
            </label>
          </div>
        ))}
      </div>
    </>
  );
};

export default StackedBarChartApp;
