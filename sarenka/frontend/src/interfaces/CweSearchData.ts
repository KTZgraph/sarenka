interface CweSearchData {
  ID_CWE: string;
  title: string;
  description: string;
  likehood: string;
  technical_impact: string[];
  caused_by: {
    field: string;
    process: string;
    description: string;
  };
  cve_examples: {
    id_CVE: string;
    description: string;
    mitre_url: string;
    sarenka_url: string;
  }[];
}

export default CweSearchData;
