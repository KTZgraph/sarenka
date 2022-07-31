import Sidebar from "../../organisms/sidebar/Sidebar";
import Navbar from "../../organisms/navbar/Navbar";
import Subtitle from "../../atoms/subtitle/index";
import "./style.scss";

const Default = ({ children, subtitle }) => {
  return (
    <div className="default">
      <Sidebar />
      <div className="defaultContainer">
        <Navbar />
        <div className="children">
          <Subtitle className="subtitle">{subtitle}</Subtitle>
          {children}
        </div>
      </div>
    </div>
  );
};

export default Default;
