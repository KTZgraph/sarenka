import { Fragment } from "react";

import { getCWEById, getAllCWEs } from "../../../helpers/api-utils";
import CWEContent from "../../../components/cwe-components/cwe-detail/cwe-content";
import CWESummary from "../../../components/cwe-components/cwe-detail/cwe-summary";

function CWEDetailPage(props) {
  const cwe = props.selectedCWE;

  // walidacja danych
  if (!cwe) {
    return (
      <div className="center">
        <p>Loading...</p>
      </div>
    );
  }

  return (
    <Fragment>
      <CWESummary title={cwe.title} />
      <h1>CWE</h1>
      <p>{cwe.name}</p>
      <p>{cwe.description}</p>
      
      <CWEContent>
        <p>{cwe.description}</p>
      </CWEContent>
    </Fragment>
  );
}

export async function getStaticProps(context) {
  const cweId = context.params.cweId;
  const cwe = await getCWEById(cweId);

  return {
    props: {
        selectedCWE: cwe,
    },
  };
}

export async function getStaticPaths() {
  // instancje dla których trzeba wyrenderować wczesniej strony
  const cwes = await getAllCWEs(); // raczej się zmieniają i są ogladane tylko przyszłe wydarzenia
  //to tez w konsekwnecji sprawia, ze niektóe wydarzenia nie będę prerenderowane

  const paths = cwes.map((cwe) => ({ params: { cweId: cwe.id } }));

  return {
    paths: paths,
    // będzie starała się dynamcicnzie renderowac strony
    fallback: "blocking", // jest wiecej stron niż te które się wyrenderowany
    //block nextjs niż nie srerwuje dopóki nie wyrenederujemy strony; trochę dłuzej to trwa ale zwraca już całą stronę
  };
}

export default CWEDetailPage;
