import { useState } from "react";
import StackedAreaChart from "./StackedAreaChart";
import StackedBarChartCopy from "./StackedBarChartCopy";

const allKeys = ["🥑", "🍌", "🍆"];

// obiekt kolorów potrzebny do kolorowania sekwencji słupków
const colors = {
  "🥑": "green",
  "🍌": "orange",
  "🍆": "purple",
};

const StackedAreaChartApp = () => {
  const [keys, setKeys] = useState(allKeys);
  const [data, setData] = useState([
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
  ]);

  return (
    <>
      <h2>Stacked Area Chart with D3 </h2>
      <StackedAreaChart data={data} keys={keys} colors={colors} />
      <StackedBarChartCopy data={data} keys={keys} colors={colors} />

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

      <button
        onClick={() =>
          setData([
            ...data,
            {
              year: Math.max(...data.map((d) => d.year)) + 10,
              "🥑": Math.round(Math.random() * 100),
              "🍌": Math.round(Math.random() * 125),
              "🍆": Math.round(Math.random() * 150),
            },
          ])
        }
      >
        Add data
      </button>
    </>
  );
};

export default StackedAreaChartApp;
