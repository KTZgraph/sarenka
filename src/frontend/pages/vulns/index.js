import Link from 'next/link';
import Head from "next/head";
import styles from '../../styles/Vulns.module.css'; 

export const getStaticProps = async () => {
    const rest = await fetch('https://jsonplaceholder.typicode.com/users');
    const data = await rest.json();

    return {
        props: {cveList: data, cweList: data} 
    }
}

const Vulns = ({cveList, cweList}) => {
    return ( 
        <>
            <Head>
                {/* komponent na metadane np title */}
                <title>Sarenka | Vulnerabilities</title>
                <meta name='keywords' content='ninjas'/>
            </Head>
            <div>
                <h1>Vulns</h1>
                <section>
                  <h2>CVE list</h2>
                  {cveList.map( cve => (
                      <Link href={'/vulns/cve/' + cve.id} key={cve.id}>
                          <a>
                              <h3>{cve.name}</h3>
                          </a>
                      </Link>
                  ))}
                </section>
                {/* -------------------- CWE -------------------- */}
                <section>
                  <h2>CWE list</h2>
                  {cweList.map( cwe => (
                      <Link href={'/vulns/cwe/' + cwe.id} key={cwe.id}>
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
 
export default Vulns;
