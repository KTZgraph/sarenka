// zwraca listę cwe
import Head from "next/head";
import useTranslation from "next-translate/useTranslation";

// import { getAllCWEs } from "../../lib/api-utils";
import CWEList from "../../components/cwe/cwe-list";

function CWEPage(props) {
  let {t} = useTranslation()

  let { cweList } = props;
  // cweList = JSON.parse(cweList);
  // przekazać osobno propsy nie obiekt - Warning: Only strings and numbers are supported as <option> children.
  //TODO
  return (
    <>
      <Head>
        {/* komponent na metadane np title */}
        <title>Sarenka | {t('common:cweList')}</title>
        <meta name="keywords" content={t('common:cweList')} />
      </Head>
      <CWEList cweList={cweList} />;
    </>
  );
}

// export async function getStaticProps() {
//   // pozwala na statyczne prerenderowanie podczas npm run build - optymailizacja danych które rzadko sie zmieniają
//   const cweList = await getAllCWEs(); //zwraca jsona

//   return {
//     props: {
//       // obiekt
//       cweList: JSON.stringify(cweList), //nie może obiektu musi JSON zwrócić z getStaticProps
//     },
//     // odświeżanie co 24h na produkcji
//     revalidate: 86400, // co 24h
//   };
// }

export default CWEPage;