import Sidebar from "../../organisms/sidebar/Sidebar";
import Navbar from "../../organisms/navbar/Navbar";
import Spinner from "../../atoms/spinner/index";
import "./style.scss";

const Loading = () => {
  return (
    <div className="loading">
      <Sidebar />
      <div className="loadingContainer">
        <Navbar />
        <div className="spinnerContainer">
          <Spinner className="spinner" />
        </div>
      </div>
    </div>
  );
};

export default Loading;
