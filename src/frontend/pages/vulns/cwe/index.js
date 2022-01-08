import { Fragment } from "react";
import Link from "next/link";

import { getAllCWEs } from "../../../helpers/api-utils";
import CWEList from "../../../components/cwe-components/cwes/cwe-list";
import Spinner from "../../../components/ui/spinner";

function AllCWEPage(props) {
  const cwes = props.cwes;

  if (!cwes) {
    //walidacja danych
    return <Spinner />;
  }

  return (
    <div>
      <CWEList cwes={cwes} />
    </div>
  );
}

export async function getStaticProps() {
  const cwes = await getAllCWEs();

  return {
    props: {
      cwes: cwes,
    },
    revalidate: 86400, // co 24h
  };
}

export default AllCWEPage;
