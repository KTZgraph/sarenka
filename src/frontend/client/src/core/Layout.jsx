import { Helmet } from "react-helmet";

const Layout = ({ title, content, children }) => {
  return (
    <>
      <Helmet>
        <title>{title}</title>
        <meat name="description" content={content} />
      </Helmet>
      {/* Navbar */}
    </>
  );
};

export default Layout;
