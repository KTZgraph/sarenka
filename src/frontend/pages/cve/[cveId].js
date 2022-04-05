import Head from "next/head";

import CVEDetails from "../../components/cve/cve-details";
import { getAllCVEs, getCVEById } from "../../lib/api-utils";
import Spinner from "../../components/ui/spinner";

function CVEDetailPage(props) {
  let cve;
  if (props.cve) {
    cve = JSON.parse(props.cve);
  }

  if (!cve) {
    return <Spinner />;
  }

  return (
    <>
      <Head>
        {/* komponent na metadane np title */}
        <title>Sarenka | {cve.id}</title>
        <meta name="keywords" content={cve.id} />
      </Head>
      <CVEDetails
        id={cve.id}
        description={cve.description}
        published={cve.published}
        updated={cve.updated}
        vector={cve.vector}
        baseScore={cve.baseScore}
        status={cve.status}
        hyperlink={cve.hyperlink}
        source={cve.source}
        cweId={cve.cweId}
      />
    </>
  );
}

export async function getStaticProps(context) {
  const cveId = context.params.cveId;
  const cve = await getCVEById(cveId);

  return {
    props: {
      // może zwrócić tylko jsona
      cve: JSON.stringify(cve),
    },
  };
}

export async function getStaticPaths() {
  const cves = await getAllCVEs(); // raczej się zmieniają i są ogladane tylko przyszłe wydarzenia

  // https://nextjs.org/docs/advanced-features/i18n-routing  trzeba tworzyć sciezki
  const pathsEN = cves.map((cve) => ({
    params: { cveId: cve.id },
    locale: "en",
  }));
  const pathsPL = cves.map((cve) => ({
    params: { cveId: cve.id },
    locale: "pl",
  }));
  const pathsAll = pathsEN.concat(pathsPL); //konkatencja list

  return {
    paths: pathsAll,
    fallback: true,
  };
}

export default CVEDetailPage;