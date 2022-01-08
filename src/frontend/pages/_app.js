import Head from 'next/head';
import Layout from '../components/layouts/layout'
import '../styles/globals.css'

function MyApp({ Component, pageProps }) {
  return (
    <Layout>
      <Head>
        <title>SARENKA</title>
        <meta name="description" content=""/>
        <meta name="viewport" content="initial-scale=1.0, width=device-width"/>
      </Head>
      <div className="container">
      <Component {...pageProps} /> 
      </div>
    </Layout>
  )
}

export default MyApp
