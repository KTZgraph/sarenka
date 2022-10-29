import Sidebar from "../sidebar/Sidebar";
import Navbar from "../navbar/Navbar";
import Spinner from "../../UI/Spinner";

import "./Loading.scss";

const Loading = ({ currentPage }) => {
  return (
    <>
      <Sidebar currentPage={currentPage} />
      <main>
        <Navbar />
        <div className="main__container loading-container">
          <Spinner />
        </div>
      </main>
    </>
  );
};

export default Loading;
