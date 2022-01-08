import { Fragment } from "react";
import { getCWEById, getAllCWEs } from "../../../helpers/api-utils";

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
      <h1>CWE</h1>
      <p>{cwe.name}</p>
      <p>{cwe.description}</p>
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
  const cweList = await getAllCWEs(); // raczej się zmieniają i są ogladane tylko przyszłe wydarzenia
  //to tez w konsekwnecji sprawia, ze niektóe wydarzenia nie będę prerenderowane

  const paths = cweList.map((cwe) => ({ params: { cweId: cwe.id } }));

  return {
    paths: paths,
    // będzie starała się dynamcicnzie renderowac strony
    fallback: "blocking", // jest wiecej stron niż te które się wyrenderowany
    //block nextjs niż nie srerwuje dopóki nie wyrenederujemy strony; trochę dłuzej to trwa ale zwraca już całą stronę
  };
}

export default CWEDetailPage;
