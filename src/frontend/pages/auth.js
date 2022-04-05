import { useRouter } from "next/router"; //przekierowanie
// import { getSession } from "next-auth/client";
import { useEffect, useState } from "react"; //żeby dobrac się do getSession

import AuthForm from "../components/auth/auth-form";
import Spinner from "../components/ui/spinner";

function AuthPage() {
  const [isLoading, setIsLoading] = useState(true); //pilnuje czy dane się już pobrały
  const router = useRouter();

//   useEffect(() => {
//     getSession().then((session) => {
//       if (session) {
//         //  jak user zalogowany to żeby nie widział/ nie mógł sie dostać do stroyn logowania
//         router.replace("/");
//       } else {
//         setIsLoading(false);
//       }
//     });
//   }, [router]);


//   if (isLoading) {
//     return <Spinner />;
//   }

  return <AuthForm />;
}

export default AuthPage;