import Link from 'next/link';
import Head from "next/head";

export const getStaticProps = async () => {
    const rest = await fetch('http://127.0.0.1:8000/api/vulns/cwe-top/');
    const data = await rest.json();

    return {
        props: {cweTopList: data} 
    }
}


const CWE = ({cweTopList}) => {
    return (
        <>
        <Head>
            {/* komponent na metadane np title */}
            <title>Sarenka | CWE TOP 25 </title>
            <meta name='keywords' content='sarenka'/>
        </Head>
        
        <div>
            <h1>TOP 25 CWE</h1>
            <section>
            {cweTopList.map(cwe => (
              <Link href={'/vulns/cwe/' + cwe.cwe_id} key={cwe.cwe_id}>
                  <a>
                      <h3>{cwe.name}</h3>
                  </a>
              </Link>
            ))}
            </section>
        </div>
        </>
    );
}
 
export default CWE;