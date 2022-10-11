import React from "react";

import "./Calendar.scss";

const Calendar = () => {
  return (
    <div className="calendar__container">
      <div className="calendar">
        <div className="celendar-header">
          <span className="month-picker" id="month-picker">
            May
          </span>
          <div className="year-picker" id="year-picker">
            <span className="year-change" id="pre-year">
              <pre>{`<`}</pre>
            </span>
            <span id="year">2020</span>
            <span className="year-change" id="next-year">
              {/* WARNING ma problem ze strzłeczkami w html */}
              {/* WARNING HTML pre tag https://www.w3schools.com/tags/tag_pre.asp */}
              <pre>{`>`}</pre>
            </span>
          </div>
        </div>
        {/* calendar body */}
        <div className="calendar-body">
          <div className="calendar-week-days">
            <div>Sun</div>
            <div>Mon</div>
            <div>Tue</div>
            <div>Wed</div>
            <div>Thu</div>
            <div>Fri</div>
            <div>Sat</div>
          </div>
          {/* celndar days */}
          <div className="calendar-days"></div>
          {/*  footer*/}
          <div className="calendar-footer"></div>
          <div className="date-time-formate">
            <div className="day-text-formate">TODAY</div>
            <div className="date-time-value">
              <div className="time-formate">02:51:20</div>
              <div className="date-formate">23 - july - 2022</div>
            </div>
          </div>
        </div>
        {/* miesiąc */}
        <div className="month-list"></div>
      </div>
    </div>
  );
};

export default Calendar;
