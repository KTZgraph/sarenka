import Sidebar from "../../organisms/sidebar/Sidebar";
import Navbar from "../../organisms/navbar/Navbar";
import Header from "../../organisms/header/Header";
import Subtitle from "../../atoms/subtitle/index";
import "./style.scss";

const DefaultSingle = ({
  children,
  subtitle,
  actionType,
  actionLink,
  label,
}) => {
  return (
    <div className="default">
      <Sidebar />
      <div className="defaultContainer">
        <Navbar />
        <Header actionType={actionType} actionLink={actionLink} label={label} />
        <div className="children">
          <Subtitle className="subtitle">{subtitle}</Subtitle>
          {children}
        </div>
      </div>
    </div>
  );
};

export default DefaultSingle;
