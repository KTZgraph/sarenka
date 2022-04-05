// chroniony endpoint - tylko dla zalogowanych
import Head from "next/head";
// import { getSession } from "next-auth/client"; //działa też po stronie serwera
import useTranslation from "next-translate/useTranslation";

import Credentials from "../components/credentials/credentials";

function CredentialsPage() {
  let { t } = useTranslation();

  return (
    <>
      <Head>
        {/* komponent na metadane np title */}
        <title>Sarenka | {t("credentials:credentials")}</title>
      </Head>
      <Credentials />
    </>
  );
}

// usuwanie wkurzającego mrugania jak przekierowuje niezalogowanego usera z /credentials -> /auth
// bardziej elenckie rozwiazanie przekirowania

// export async function getServerSideProps(context) {
//   // nie getStaticProps bo ma działać dla kazdego requesta
//   const session = await getSession({ req: context.req }); //zwraca promisa, null jak not authenticated user

//   if (!session) {
//     // not-authenticated
//     // notFound: true, // ale jednak nie chcę pokazywać 404
//     return {
//       redirect: {
//         // przekierowanie niezalogowanego bez mrugania/flashing
//         destination: "/auth",
//         permament: false, //nie zawszer przekierowuje, tylko jeden raz jak niezalgowany
//       },
//     };
//   }

//   // zalogowany
//   return {
//     // obiekt poptrzebny do ustawiania obiektu sesji w pages/_app.js
//     // nie wszsytkie strony potrzebują sesji
//     props: { session }, //przekazuję obiket sesji przez props
//   };
// }

export default CredentialsPage;