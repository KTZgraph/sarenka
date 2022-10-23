/*
https://www.youtube.com/watch?v=c9nw5rWtMeQ
*/

// www.youtube.com/watch?v=c9nw5rWtMeQ
//github.com/Bowserinator/Periodic-Table-JSON/blob/master/PeriodicTableJSON.json
import Navbar from "../../../shared/navbar/Navbar";
import Sidebar from "../../../shared/sidebar/Sidebar";
import PeriodicTable from "../components/PeriodicTable";

const PeriodicTablePage = () => {
  return (
    <>
      <Sidebar currentPage="periodicTable" />
      <main>
        <Navbar />
        <div className="periodic-table-page" style={{ marginLeft: "18rem" }}>
          <h1>Periodic Table of Elements</h1>
          <small> with React + CSS Grid</small>
          <PeriodicTable />
        </div>
      </main>
    </>
  );
};

export default PeriodicTablePage;
