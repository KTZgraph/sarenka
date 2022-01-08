import Layout from '../components/layouts/layout'
import '../styles/globals.css'

function MyApp({ Component, pageProps }) {
  return (
    <Layout>
      <div className="container">
      <Component {...pageProps} /> 
      </div>
    </Layout>
  )
}

export default MyApp
