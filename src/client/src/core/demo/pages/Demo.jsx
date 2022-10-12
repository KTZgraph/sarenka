import { useEffect, useState, useRef } from "react";

import Navbar from "../../../shared/navbar/Navbar";
import Sidebar from "../../../shared/sidebar/Sidebar";

import DashboardTop from "../components/dashboard-top/DashboardTop";
import VulnerabilitiesGeneral from "../components/vulnerabilities-general/VulnerabilitiesGeneral";

import "./Demo.scss";

const Demo = () => {
  return (
    <>
      <Sidebar currentPage="demo" />
      <main>
        <Navbar />
        <div className="main__container demo">
          <DashboardTop />
          <VulnerabilitiesGeneral />
        </div>
      </main>
    </>
  );
};

export default Demo;
