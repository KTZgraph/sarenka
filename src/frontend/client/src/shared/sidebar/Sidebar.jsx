import { useContext } from "react";
import { DarkModeContext } from "../../context/darkModeContext";
import { Link } from "react-router-dom";

import { sidebarItems } from "./sidebar-items";
import "./Sidebar.scss";

const SidebarList = ({ currentPage, sidebarItems }) => {
  return (
    <ul>
      {sidebarItems.map((group, idx) => (
        <div className="sidebar__group" key={idx}>
          {group.title && (
            <p key={group.id} className="sidebar__title">
              {group.title}
            </p>
          )}

          {group.elements.map((el) => (
            <Link to={el.to} key={el.id}>
              <li
                className={`sidebar__item ${
                  currentPage === `${el.activePage}`
                    ? "sidebar__item--active"
                    : ""
                }`}
              >
                {el.icon}
                <span className="sidebar__subtitle">{el.label}</span>
              </li>
            </Link>
          ))}
        </div>
      ))}
    </ul>
  );
};

const Sidebar = ({ currentPage }) => {
  const { dispatch } = useContext(DarkModeContext);

  return (
    <div className="sidebar">
      <div className="sidebar__top">
        <Link to="/">
          <span className="sidebar__logo-name">SARENKA</span>
        </Link>
      </div>
      <hr className="sidebar__separator" />
      <div className="sidebar__center">
        {/* elementy sidebara */}
        <SidebarList currentPage={currentPage} sidebarItems={sidebarItems} />
      </div>
      <div className="sidebar__bottom">
        <div
          className="sidebar__color-option sidebar__color-option--light"
          onClick={() => dispatch({ type: "LIGHT" })}
        ></div>
        <div
          className="sidebar__color-option sidebar__color-option--dark"
          onClick={() => dispatch({ type: "DARK" })}
        ></div>
      </div>
      <div className="sidebar__logo">
        <img
          className="sidebar__img"
          src={process.env.PUBLIC_URL + "/images/logo_cropped.png"}
          alt="sarenka-logo"
        />
      </div>
    </div>
  );
};

export default Sidebar;
