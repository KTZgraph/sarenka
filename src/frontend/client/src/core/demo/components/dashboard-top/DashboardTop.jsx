import InsertDriveFileIcon from "@mui/icons-material/InsertDriveFile";
import GppMaybeIcon from "@mui/icons-material/GppMaybe";

import Widget from "./Widget";
import styles from "./DashboardTop.module.scss";

const widgetsData = [
  {
    title: "Vulnerabilities",
    count: 1111111111,
    linkName: "See all vulnerabilities",
    linkUrl: "/vulnerabilities",
    icon: <GppMaybeIcon className={styles.icon} />,
    percentage: 11,
  },

  {
    title: "plugins regular",
    count: 22222,
    linkName: "See all plugins",
    linkUrl: "/plugins",
    icon: <InsertDriveFileIcon className={styles.icon} />,
    percentage: 22,
  },
  {
    title: "Plugins Alligator",
    count: 33333,
    linkName: "Alligator interface",
    linkUrl: "/alligator-interface",
    icon: <InsertDriveFileIcon className={styles.icon} />,
    percentage: -33,
  },
  {
    title: "detectors",
    count: 44444,
    linkName: "Detectors",
    linkUrl: "/detectors",
    icon: <InsertDriveFileIcon className={styles.icon} />,
    percentage: -44,
  },
];

const DashboardTop = () => {
  return (
    <section className={styles.dashboardTop}>
      {widgetsData.map((data) => (
        <Widget
          key={data.title}
          data={data}
          className={styles.dashboardTop__widget}
        />
      ))}
    </section>
  );
};

export default DashboardTop;
