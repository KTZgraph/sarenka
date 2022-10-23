/*
https://www.youtube.com/watch?v=tIdNeoHniEY
*/

import { useContext, useState } from "react";
import { useNavigate } from "react-router-dom";

import { AuthContext } from "../../../context/AuthContext";
import { signInWithEmailAndPassword } from "../../../lib/auth";

import FormInput from "../../../UI/FormInput";
import Subtitle from "../../../components/atoms/subtitle";
import "./LoginForm.scss";

const LoginForm = ({ className }) => {
  const { dispatch } = useContext(AuthContext);
  const navigate = useNavigate();

  const [error, setError] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const [values, setValues] = useState({
    email: "",
    password: "",
  });

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
    signInWithEmailAndPassword(values.email, values.password)
      .then((userCredentials) => {
        setError(false);
        setErrorMessage("");
        dispatch({ type: "LOGIN", payload: userCredentials.user });
        navigate("/");
      })
      .catch((error) => {
        setErrorMessage(error.message);
        setError(true);
      });
  };

  const handleChange = (e) => {
    setValues({ ...values, [e.target.name]: e.target.value });
  };

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
      <button className="login-form__button" type="submit">
        Login
      </button>
      {error && (
        <span className="login-form__error-messsage">{errorMessage}</span>
      )}
    </form>
  );
};

export default LoginForm;
