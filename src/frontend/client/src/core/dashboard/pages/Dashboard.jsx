import Sidebar from "../../../shared/sidebar/Sidebar";
import Navbar from "../../../shared/navbar/Navbar";
import Widget from "../components/Widget";
import Featured from "../components/Featured";
import Chart from "../components/Chart";
import Hometable from "../components/Hometable";

import { Navigate } from "react-router-dom";
// do danych usera
// https://youtu.be/GaKGYo2jQ2Y?t=211
import { useSelector } from "react-redux";

import "./Dashboard.scss";
import Spinner from "../../../UI/Spinner";
const Dashboard = () => {
  // sarenka\src\frontend\client\src\store.js do reducera odnoszę się przez słowo `user`
  const { user, loading, isAuthenticated } = useSelector((state) => state.user);
  console.log("dashboard user");
  console.log(user);

  if (!isAuthenticated && !loading && user === null) {
    return <Navigate to="/login" />;
  }

  if (loading) {
    return <Spinner />;
  }

  return (
    <>
      <Sidebar currentPage="home" />
      <main>
        <Navbar />
        <div className="main__container dashboard">
          {loading || user === null ? (
            <Spinner />
          ) : (
            <div className="dashboard__container">
              {/* user details */}
              <div className="dashboard__user">
                <h1>User details</h1>
                <ul>
                  <li>First name {user?.first_name || "brak"}</li>
                  <li>Last name {user?.last_name || "brak last name"}</li>
                  <li>Email {user?.email_name || "brak last name"}</li>
                  <li>Cały user {JSON.stringify(user)}</li>
                </ul>
              </div>

              <div className="dashboard__widgets">
                <Widget type="user" />
                <Widget type="order" />
                <Widget type="earnings" />
                <Widget type="balance" />
              </div>
              <div className="dashboard__charts">
                {/* wykresiki */}
                <Featured />
                <Chart
                  chartTitle="Last 6 Months (Revenue)"
                  chartAspect={2 / 1}
                />
              </div>
              <div className="chart__list-container">
                {/* FIXME zmienić na ostatnie CVEs */}
                <div className="chart__list-title">Latest Transactions</div>
                <Hometable />
              </div>
            </div>
          )}
        </div>
      </main>
    </>
  );
};

export default Dashboard;
