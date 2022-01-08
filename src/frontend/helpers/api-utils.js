BACKEND_API = "http://127.0.0.1:8000/api/";

export async function getAllCWEs() {
  //zwraca promisa
  /**
   * Zwraca listę wszystkich obiektów cwe
   * @return {Promise} lista wszystkich CWE z bazy
   */
  const response = await fetch(
    //zwraca promisa
    `${BACKEND_API}/vulns/cwe-list/`
  );
  const data = await response.json();
  return data;
}

export async function getCWEById(id) {
  /**
     * Pobiera pojedyncze CWE po id i zwraca Obiekt
     * np.: http://127.0.0.1:8000/api/vulns/cwe/1004/
     * @param {int} id - id cwe ale sama liczba
     * @return {Promise} będący popjedycnzycm obiektem cwe
     * {
        "id": "1004",
        "name": "Sensitive Cookie Without 'HttpOnly' Flag",
        "abstraction": "Variant",
        "structure": "Simple",
        "status": "Incomplete",
        "description": "The software uses a cookie to store sensitive information, but the cookie is not marked with the HttpOnly flag.",
        "extended_description": "The HttpOnly flag directs compatible browsers to prevent client-side script from accessing cookies. Including the HttpOnly flag in the Set-Cookie HTTP response header helps mitigate the risk associated with Cross-Site Scripting (XSS) where an attacker's script code might attempt to read the contents of a cookie and exfiltrate information obtained. When set, browsers that support the flag will not reveal the contents of the cookie to a third party via client-side script executed via XSS."
        }
     */

  const response = await fetch(`${BACKEND_API}/vulns/cwe/${id}`);
  const data = await response.json();
  return data;
}
