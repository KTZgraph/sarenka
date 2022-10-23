import Title from "../../../components/atoms/title/index";
import LoginForm from "../components/LoginForm";

import "./Login.scss";
const Login = () => {
  return (
    <div className="wrapper login">
      <Title className="login__title">Sarenka</Title>
      <LoginForm className="login__form" />
      <footer className="login__footer">
        <img
          className="login__logo"
          src={process.env.PUBLIC_URL + "/images/logo_cropped.png"}
          alt="app-logo.png"
        />
      </footer>
    </div>
  );
};

export default Login;
