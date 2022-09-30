import HomeRoundedIcon from "@mui/icons-material/HomeRounded";

// import SettingsInputHdmiRoundedIcon from "@mui/icons-material/SettingsInputHdmiRounded";

import InsertDriveFileIcon from "@mui/icons-material/InsertDriveFile";
import NoteAddRoundedIcon from "@mui/icons-material/NoteAddRounded";
import PlagiarismIcon from "@mui/icons-material/Plagiarism";
import DescriptionIcon from "@mui/icons-material/Description";
import GppMaybeIcon from "@mui/icons-material/GppMaybe";
import AddModeratorRoundedIcon from "@mui/icons-material/AddModeratorRounded";
import PolicyRoundedIcon from "@mui/icons-material/PolicyRounded";
import SecurityIcon from "@mui/icons-material/Security";
import FilePresentRoundedIcon from "@mui/icons-material/FilePresentRounded";
import StorageRoundedIcon from "@mui/icons-material/StorageRounded";
import PersonOutlineIcon from "@mui/icons-material/PersonOutline";
import ManageAccountsIcon from "@mui/icons-material/ManageAccounts";

export const sidebarItems = [
  {
    // home pierwszy
    id: "sidebar-title-home",
    title: "",
    elements: [
      {
        id: "sidebar-element-home-1",
        activePage: "home",
        label: "home",
        to: "/",
        icon: <HomeRoundedIcon className="sidebar__icon" />,
      },
    ],
  },
  // notes
  {
    id: "sidebar-title-notes",
    title: "notes",
    elements: [
      {
        id: "sidebar-element-notes-1",
        activePage: "notes",
        label: "notes",
        to: "/notes",
        icon: <InsertDriveFileIcon className="sidebar__icon" />,
      },
      {
        id: "sidebar-element-notes-2",
        activePage: "addNote",
        label: "add note",
        to: "/notes/new",
        icon: <NoteAddRoundedIcon className="sidebar__icon" />,
      },
      {
        id: "sidebar-element-notes-3",
        activePage: "searchNotes",
        label: "search notes",
        to: "/notes/search",
        icon: <PlagiarismIcon className="sidebar__icon" />,
      },
      {
        id: "sidebar-element-notes-4",
        activePage: "noteTemplates",
        label: "note templates",
        to: "/notes/templates",
        icon: <DescriptionIcon className="sidebar__icon" />,
      },
      {
        id: "sidebar-element-notes-5",
        activePage: "advisoryTemplate",
        label: "advisory template",
        to: "/advisory-templates",
        icon: <FilePresentRoundedIcon className="sidebar__icon" />,
      },
    ],
  },
  // vulnerabilities
  {
    id: "sidebar-title-vulnerabilities",
    title: "vulnerabilities",
    elements: [
      {
        id: "sidebar-element-vulnerabilities-1",
        activePage: "vulnerabilities",
        label: "vulnerabilities",
        to: "/vulnerabilities",
        icon: <GppMaybeIcon className="sidebar__icon" />,
      },
      {
        id: "sidebar-element-vulnerabilities-2",
        activePage: "addVulnerability",
        label: "add vulnerability",
        to: "/vulnerabilities/new",
        icon: <AddModeratorRoundedIcon className="sidebar__icon" />,
      },
      {
        id: "sidebar-element-vulnerabilities-3",
        activePage: "searchVulnerabilities",
        label: "search vulnerabilities",
        to: "/vulnerabilities/search",
        icon: <PolicyRoundedIcon className="sidebar__icon" />,
      },
      {
        id: "sidebar-element-vulnerabilities-4",
        activePage: "unsuportedSoftware",
        label: "unsuported software",
        to: "/unsuported-software",
        icon: <SecurityIcon className="sidebar__icon" />,
      },
    ],
  },

  //statistics
  {
    id: "sidebar-title-statistics",
    title: "statistics",
    elements: [
      {
        id: "sidebar-element-statistics-1",
        activePage: "statistics",
        label: "statistics",
        to: "/statistics",
        icon: <StorageRoundedIcon className="sidebar__icon" />,
      },
    ],
  },

  //settings
  {
    id: "sidebar-title-settings",
    title: "settings",
    elements: [
      {
        id: "sidebar-element-settings-1",
        activePage: "profileSettings",
        label: "Profile",
        to: "/profile-settings",
        icon: <PersonOutlineIcon className="sidebar__icon" />,
      },
      {
        id: "sidebar-element-settings-2",
        activePage: "adminSettings",
        label: "Admin",
        to: "/admin-settings",
        icon: <ManageAccountsIcon className="sidebar__icon" />,
      },
    ],
  },

  //kociamber
  {
    id: "sidebar-title-kociamber",
    title: "kociamber",
    elements: [
      {
        id: "sidebar-element-kociamber-1",
        activePage: "kociamberInterface",
        label: "kociamber",
        to: "/kociamber-interface",
        icon: (
          <img
            className="sidebar__icon-svg"
            src={process.env.PUBLIC_URL + "/kociamber.svg"}
            alt="crocodile_v5_blue.svg"
          />
        ),
      },
    ],
  },
];
