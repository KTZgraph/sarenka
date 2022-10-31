/*
https://www.youtube.com/watch?v=tIdNeoHniEY
*/

import { useContext, useState, useEffect } from "react";
import { Navigate } from "react-router-dom";

import { AuthContext } from "../../../context/AuthContext";
import { signInWithEmailAndPassword } from "../../../lib/auth";

import FormInput from "../../../UI/FormInput";
import Subtitle from "../../../components/atoms/subtitle";
import Spinner from "../../../UI/Spinner";

// redux
import { useDispatch, useSelector } from "react-redux";
import { resetRegistered, login } from "../../../features/user";

import "./LoginForm.scss";

const LoginForm = ({ className }) => {
  // WARNING https://www.youtube.com/watch?v=cvu6a3P9S0M&t=1365s 48:30
  const userDispatch = useDispatch();
  // https://youtu.be/oa_YvzYDyR8?t=500
  // https://youtu.be/GaKGYo2jQ2Y?t=111 isAuthenticated
  // https://youtu.be/GaKGYo2jQ2Y?t=1434 registered
  const { loading, isAuthenticated, registered } = useSelector(
    (state) => state.user
  );

  const { dispatch } = useContext(AuthContext);

  const [error, setError] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const [values, setValues] = useState({
    email: "",
    password: "",
  });

  const { email, password } = values;

  const inputs = [
    {
      id: 1,
      name: "email",
      type: "email",
      placeholder: "Email",
      errorMessage: "It should be a valid email address!",
      label: "Email",
      required: true,
    },
    {
      id: 2,
      name: "password",
      type: "password",
      placeholder: "Password",
      label: "Password",
      required: true,
    },
  ];

  const handleSubmit = (e) => {
    e.preventDefault();

    // https://youtu.be/oa_YvzYDyR8?t=2325 pamietać żeby robić to jako obiekt
    userDispatch(login({ email, password }));
    // FIXME
    signInWithEmailAndPassword(values.email, values.password)
      .then((userCredentials) => {
        setError(false);
        setErrorMessage("");
        dispatch({ type: "LOGIN", payload: userCredentials.user });
        // navigate("/");
      })
      .catch((error) => {
        setErrorMessage(error.message);
        setError(true);
      });
  };

  const handleChange = (e) => {
    setValues({ ...values, [e.target.name]: e.target.value });
  };

  useEffect(() => {
    if (registered) userDispatch(resetRegistered);
  }, [registered]);

  // BUG https://github.com/linkedweb/auth-site/blob/main/frontend/client/src/containers/LoginPage.js
  // BUG jak używa się zwykłego navigate to nie moze wyrenderować komponentów
  if (isAuthenticated) return <Navigate to="/" />;

  return (
    <form className={`login-form ${className}`} onSubmit={handleSubmit}>
      <Subtitle className="login-form__subtitle">Log in</Subtitle>
      {inputs.map((input) => (
        <FormInput
          className="login-form__input"
          key={input.id}
          {...input}
          value={values[input.name]}
          onChange={handleChange}
          nameFocus="password"
        />
      ))}
      {loading ? (
        <Spinner />
      ) : (
        <button className="login-form__button" type="submit">
          Login
        </button>
      )}

      {error && (
        <span className="login-form__error-messsage">{errorMessage}</span>
      )}
    </form>
  );
};

export default LoginForm;
