/*
https://youtu.be/DGmX1FDdLZE?t=1004
*/

import { useState } from "react";
import { Navigate } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";

// action creator import z sarenka\src\frontend\client\src\features\user.js
import { register } from "../../../features/user";

import Spinner from "../../../UI/Spinner";
const Register = () => {
  const dispatch = useDispatch();

  // sarenka\src\frontend\client\src\store.js chodzi o user linia 16
  const { registered, loading } = useSelector((state) => state.user);

  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  });

  // destrukturyzacja danych ze state, żeby używać ich bezpośrednio
  const { first_name, last_name, email, password } = formData;

  const onChange = (e) => {
    // zmieniam tylko jeden atryubut ze stanu - rreszta pozostahe bez zmian
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const onSubmit = (e) => {
    e.preventDefault();

    // teraz będą actioncreator - trzeba przez dispatch to zrobić
    dispatch(
      register({
        // mozna przekazac caly obiekt formData ale tka jest czytelniej
        first_name,
        last_name,
        email,
        password,
      })
    );
  };

  if (registered) return <Navigate to="/login" />;

  return (
    <div>
      <h1>Register for an account</h1>
      <form onSubmit={onSubmit}>
        <div>
          {/* first name */}
          <div className="register__form-group">
            <label className="register__label" htmlFor="first_name">
              First Name
            </label>
            <input
              type="text"
              // ważne żeby nazwa była jak w sarenka\src\frontend\routes\auth\register.js
              name="first_name"
              onChange={onChange}
              // mogę bezpośrednio bo zdestruktyruzowałam state
              value={first_name}
              required
            />
          </div>

          {/* last name */}
          <div className="register__form-group">
            <label className="register__label" htmlFor="last_name">
              Last Name
            </label>
            <input
              type="text"
              // ważne żeby nazwa była jak w sarenka\src\frontend\routes\auth\register.js
              name="last_name"
              onChange={onChange}
              // mogę bezpośrednio bo zdestruktyruzowałam state
              value={last_name}
              required
            />
          </div>
          {/* email */}
          <div className="register__form-group">
            <label className="register__label" htmlFor="email">
              Email
            </label>
            <input
              type="text"
              // ważne żeby nazwa była jak w sarenka\src\frontend\routes\auth\register.js
              name="email"
              onChange={onChange}
              // mogę bezpośrednio bo zdestruktyruzowałam state
              value={email}
              required
            />
          </div>
          <div className="register__form-group">
            <label className="register__label" htmlFor="password">
              Password
            </label>
            <input
              // WARNING inputy type password
              type="password"
              // ważne żeby nazwa była jak w sarenka\src\frontend\routes\auth\register.js
              name="password"
              onChange={onChange}
              // mogę bezpośrednio bo zdestruktyruzowałam state
              value={password}
              required
            />
          </div>
        </div>
        {loading ? (
          <Spinner />
        ) : (
          <button className="register__button">Register</button>
        )}
      </form>
    </div>
  );
};

export default Register;
