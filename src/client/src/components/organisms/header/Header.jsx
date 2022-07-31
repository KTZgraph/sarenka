import Navigation from "../../atoms/navigation";
import "./header.scss";

const Header = ({ actionType, actionLink }) => {
  return (
    <div className="header">
      <div className="headerContainer">
        <div className="items">
          <Navigation to={actionLink} className={`item ${actionType}`}>
            {actionType === "update"
              ? "Update"
              : actionType === "create"
              ? "Create"
              : actionType === "delete"
              ? "Delete"
              : ""}
          </Navigation>
        </div>
      </div>
    </div>
  );
};

export default Header;
