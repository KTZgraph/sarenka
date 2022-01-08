BACKEND_API = 'http://127.0.0.1:8000/api/'


export async function getAllCWEs() { //zwraca promisa
    /**
     * Zwraca listę wszystkich obiektów cwe
     */
    const response = await fetch( //zwraca promisa
      `${BACKEND_API}/vulns/cwe-list/`
    );
    const data = await response.json();  
    return data;
}


export async function getCWEById(id){
    /**
     * Pobiera pojedyncze CWE po id
     * np.: http://127.0.0.1:8000/api/vulns/cwe/1004/
     * @param {int} id - id cwe ale sama liczba
     */

    const response = await fetch(`${BACKEND_API}/vulns/cwe/${id}`)
    const data = await response.json();  
    return data;
}