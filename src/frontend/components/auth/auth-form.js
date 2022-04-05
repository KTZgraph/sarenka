import { useState, useRef, useContext } from "react";
// import { signIn } from "next-auth/client"; // do logowania
import { useRouter } from "next/router"; //do przekierownia

import classes from "./auth-form.module.css";
// import { createUser } from "../../lib/auth-utils";
import NotificationContext from "../../store/notification-context";

function AuthForm() {
  // do notyfikacji
  const notificationCtx = useContext(NotificationContext);

  const [isLogin, setIsLogin] = useState(false);
  const router = useRouter(); //do przekierowania

  // na początku ma się pokazać rejestracja
  const [isExistingUser, setIsExistingUser] = useState(false);

  const emailInputRef = useRef();
  const passwordInputRef = useRef();
  const passwordConfirmationInputRef = useRef();

  // przełączanie HTMLa zaloguj / zarejestruj
  function switchAuthModeHandler() {
    setIsExistingUser((prevState) => !prevState);
  }

  async function submitHandler(event) {
    event.preventDefault();

    const enteredEmail = emailInputRef.current.value;
    const enteredPassword = passwordInputRef.current.value;

    // waldiacja na froncie - pomaga użźytkownikowi, ale to ta na backendzie realnie gwarantuje bezpieczenstwo

    //logowanie
    if (isExistingUser) {
      // signIn( Provider - mbo moze być kilka, ObjectKonfiguracji)
      notificationCtx.showNotification({
        title: "Login",
        message: "trying to log user",
        status: "pendind",
      });

    //   const result = await signIn("credentials", {
    //     redirect: false, //zeby nie przekierowywał usera na error page w razie bledu, tylko pokazac jak na tej samej stronie
    //     email: enteredEmail,
    //     password: enteredPassword,
    //   });

      if (result.error) {
        // błąd logowania
        notificationCtx.showNotification({
          title: "Error",
          message: result.error || "Couldn't log user",
          status: "error",
        });
      }
      console.log(result);
      if (!result.error) {
        // jak nie ma błedu to atrybut error jest nullem,
        // ustawić status, żeby zalogowany user widział wiecej podstron - ale trzeba ustawić token
        // przekierować jak jest user prawidłowo zalogowany
        notificationCtx.showNotification({
          title: "Success",
          message: "User logged succesfully",
          status: "success",
        });
        router.replace("/credentials");
      }
    }

    // rejestracja
    else {
      try {
        // potwierdzenie hasła do rejestracji
        const enteredPassConfirm = passwordConfirmationInputRef.current.value;
        if (enteredPassword !== enteredPassConfirm) {
          throw new Error("Passwords don't match");
        }
        notificationCtx.showNotification({
          title: "Creating new user",
          message: "Saving user to database",
          status: "pendind",
        });
        // const result = await createUser(enteredEmail, enteredPassword);
        // dobrze dac stworzenie użytkownika do notyfikacji
        // wiem, że użytkownik został stworozny
        console.log(result);
        notificationCtx.showNotification({
          title: "Success",
          message: "User created",
          status: "success",
        });
      } catch (error) {
        // dobrze dac błąd do notyfikacji
        console.log(error);
        notificationCtx.showNotification({
          title: "Error",
          message: error.message || "User not created!",
          status: "error",
        });
      }
    }

    //jeśli jest już zalogowany to przekierować na credentiale
  }

  return (
    <section className={classes.auth}>
      <h1>Sign up</h1>
      <form onSubmit={submitHandler}>
        <div className={classes.control}>
          <label htmlFor="email">Your Email</label>
          <input type="email" id="email" required ref={emailInputRef} />
        </div>
        <div className={classes.control}>
          <label htmlFor="password">Your Password</label>
          <input
            type="password"
            id="password"
            required
            ref={passwordInputRef}
          />
        </div>
        {/* potwierdzenie hasła tylko przy rejestracji */}
        {!isExistingUser && (
          <div className={classes.control}>
            <label htmlFor="passwordConfirmation">Confirm Your Password</label>
            <input
              type="password"
              id="passwordConfirmation"
              required
              ref={passwordConfirmationInputRef}
            />
          </div>
        )}

        <div className={classes.actions}>
          {/* jeśłi uzytkonik istnieje to pokazaż przycisk logowania */}
          <button>{isExistingUser ? "Login" : "Create account"}</button>

          {/* przycisk zmiany formularzy */}
          {/* jeśli użytkownik nie istnieje to pokaż formularz rejestracji */}
          <button
            type="button"
            className={classes.toggle}
            onClick={switchAuthModeHandler}
          >
            {isExistingUser
              ? "Create new account"
              : "Login with existing account"}
          </button>
        </div>
      </form>
    </section>
  );
}

export default AuthForm;
