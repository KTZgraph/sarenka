/*
https://www.youtube.com/watch?v=eT-yDDnFbyU
*/

import Navbar from "../../../shared/navbar/Navbar";
import Sidebar from "../../../shared/sidebar/Sidebar";
import Calendar from "../components/Calendar";

const CalendarPage = () => {
  return (
    <>
      <Sidebar currentPage="calendar-page" />
      <main>
        <Navbar />
        <div className="main__container">
          <Calendar />
        </div>
      </main>
    </>
  );
};

export default CalendarPage;
