import { useEffect, useState, useRef } from "react";

import Navbar from "../../../shared/navbar/Navbar";
import Sidebar from "../../../shared/sidebar/Sidebar";

import DashboardTop from "../components/dashboard-top/DashboardTop";

import "./Demo.scss";

const Demo = () => {
  return (
    <>
      <Sidebar currentPage="demo" />
      <main>
        <Navbar />
        <div className="main__container demo">
          <DashboardTop />
        </div>
      </main>
    </>
  );
};

export default Demo;
