/*
https://youtu.be/DGmX1FDdLZE?t=1004
*/

import { useState } from "react";
import { Navigate } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";

const Register = () => {
  // sarenka\src\frontend\client\src\store.js chodzi o user linia 16
  const { registered } = useSelector((state) => state.user);

  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  });

  // destrukturyzacja danych ze state, żeby używać ich bezpośrednio
  const { first_name, last_name, email, password } = formData;

  const onChange = (e) =>
    // zmieniam tylko jeden atryubut ze stanu - rreszta pozostahe bez zmian
    setFormData({ ...formData, [e.target.name]: e.target.value });

  if (registered) return <Navigate to="/login" />;

  return (
    <div>
      <h1>Register for an acount</h1>
      <form>
        <div>
          <label htmlFor="first_name">First Name</label>
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
      </form>
    </div>
  );
};

export default Register;
