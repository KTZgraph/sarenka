import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import styles from "./Chart.module.scss";

const dataOriginal = [
  {
    name: "Page A",
    uv: 4000,
    pv: 2400,
    amt: 2400,
  },
  {
    name: "Page B",
    uv: 3000,
    pv: 1398,
    amt: 2210,
  },
  {
    name: "Page C",
    uv: 2000,
    pv: 9800,
    amt: 2290,
  },
  {
    name: "Page D",
    uv: 2780,
    pv: 3908,
    amt: 2000,
  },
  {
    name: "Page E",
    uv: 1890,
    pv: 4800,
    amt: 2181,
  },
  {
    name: "Page F",
    uv: 2390,
    pv: 3800,
    amt: 2500,
  },
  {
    name: "Page G",
    uv: 3490,
    pv: 4300,
    amt: 2100,
  },
];

const data = [
  { name: "January", Total: 1200 },
  { name: "February", Total: 2100 },
  { name: "March", Total: 800 },
  { name: "April", Total: 1600 },
  { name: "May", Total: 900 },
  { name: "June", Total: 1700 },
];

const Chart = ({ chartAspect, chartTitle }) => {
  return (
    <div className={styles.chart}>
      <div className={styles.title}>{chartTitle}</div>
      {/* height="100%" sprawia, ze wykres leci w nieskończonosc w dół */}
      {/* <ResponsiveContainer width="100%" height="100%"> */}
      {/* <ResponsiveContainer width="100%" height={100}> */}
      {/* aspect={2 / 1} daje połowę 100vh  */}
      <ResponsiveContainer width="100%" aspect={chartAspect}>
        {/* FIXME zmienić na dane o CVE CWETop25 albo OWASP TOP10 */}
        <AreaChart
          width={730}
          height={250}
          // podmianka danych do wykresu
          // data={dataOriginal}
          data={data}
          margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
        >
          <defs>
            {/* <linearGradient id="colorUv" x1="0" y1="0" x2="0" y2="1"> */}
            <linearGradient id="total" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#8884d8" stopOpacity={0.8} />
              <stop offset="95%" stopColor="#8884d8" stopOpacity={0} />
            </linearGradient>
            <linearGradient id="colorPv" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#82ca9d" stopOpacity={0.8} />
              <stop offset="95%" stopColor="#82ca9d" stopOpacity={0} />
            </linearGradient>
          </defs>
          {/* <XAxis dataKey="name" /> stroke - zmiana koloru linii*/}
          <XAxis dataKey="name" stroke="lightgray" />
          {/* pionowa osi 0Y z danymi "Total" na skali */}
          <YAxis />
          {/* siatka na wykresie */}
          {/* <CartesianGrid strokeDasharray="3 3" /> */}
          <CartesianGrid strokeDasharray="3 3" className={styles.chartGrid} />
          <Tooltip />
          {/* Area jest ważnym miejsce - tutaj pokazujemy ten liniowy chart*/}
          <Area
            type="monotone"
            // dataKey="uv"
            dataKey="Total"
            stroke="#8884d8"
            fillOpacity={1}
            // fill="url(#colorUv)"
            fill="url(#total)"
          />
          {/* <Area
            type="monotone"
            dataKey="pv"
            stroke="#82ca9d"
            fillOpacity={1}
            fill="url(#colorPv)"
          /> */}
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
};

export default Chart;
