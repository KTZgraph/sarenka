import Footer from "./footer";
import Navbar from "./navbar";

const Layout = ({children}) => {
    return (
       <div className="container change">
           <Navbar/>
           {children}
           <Footer/>
       </div>
    );
}
 
export default Layout;