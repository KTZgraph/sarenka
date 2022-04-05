// zwraca listę podatności cve
import Head from "next/head";
import useTranslation from "next-translate/useTranslation";

// import { getAllCVEs } from "../../lib/api-utils";
import CVEList from "../../components/cve/cve-list";

function CVEPage(props) {
  let { t } = useTranslation();

  let { cveList } = props;
  // cveList = JSON.parse(cveList);

  return (
    <>
      <Head>
        {/* komponent na metadane np title */}
        <title>Sarenka | {t("common:cveList")}</title>
        <meta name="keywords" content={t("common:cveList")} />
      </Head>

      <CVEList cveList={cveList} />
    </>
  );
}

// export async function getStaticProps() {
//   // pozwala na statyczne prerenderowanie podczas npm run build - optymailizacja danych które rzadko sie zmieniają
//   const cveList = await getAllCVEs();

//   return {
//     props: {
//       // obiekt
//       cveList: JSON.stringify(cveList), //nie może obiektu zwrócić z getStaticProps
//     },
//     // odświeżanie co minutę, bo może przeciez nie być wszysktich w bazie
//     revalidate: 60,
//   };
// }

export default CVEPage;