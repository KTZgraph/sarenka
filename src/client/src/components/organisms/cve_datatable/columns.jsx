export const datatableColumns = [
  { field: "code", headerName: "ID", width: 120 },
  { field: "cwe_code", headerName: "CWE", width: 100 },
  {
    field: "cvss_v3",
    headerName: "CVSSV3",
    width: 100,
    renderCell: (params) => {
      let severity = params.row.base_metric_v3.cvss_v3.base_severity;
      severity ? (severity = severity.toLowerCase()) : (severity = "");

      return (
        <div
          className={
            severity === "critical"
              ? "cellWithStatus critical"
              : severity === "high"
              ? "cellWithStatus high"
              : severity === "medium"
              ? "cellWithStatus high"
              : severity === "low"
              ? "cellWithStatus low"
              : "cellWithStatus"
          }
        >
          {params.row.base_metric_v3.cvss_v3.base_score || ""}
        </div>
      );
    },
  },
  {
    //bgc zależnie od wartości
    field: "cvss_v2",
    headerName: "CVSSV2",
    width: 100,
    renderCell: (params) => {
      let severity = params.row.base_metric_v2.severity;
      severity ? (severity = severity.toLowerCase()) : (severity = "");

      return (
        <div
          className={
            severity === "critical"
              ? `cellWithStatus critical`
              : severity === "high"
              ? `cellWithStatus high`
              : severity === "medium"
              ? `cellWithStatus high`
              : severity === "low"
              ? `cellWithStatus low`
              : `cellWithStatus`
          }
        >
          {params.row.base_metric_v2.cvss_v2.base_score || ""}
        </div>
      );
    },
  },
  {
    //bgc zależnie od wartości
    field: "exploitability_score",
    headerName: "Exploitability",
    width: 100,
    renderCell: (params) => {
      return <p>{params.row.base_metric_v3.exploitability_score || ""}</p>;
    },
  },

  {
    field: "vector",
    headerName: "Vector",
    width: 400,
    renderCell: (params) => {
      let severity = params.row.base_metric_v2.severity;
      severity ? (severity = severity.toLowerCase()) : (severity = "");

      return (
        <div
          className={
            severity === "critical"
              ? `cellWithStatus vectorCritical`
              : severity === "high"
              ? `cellWithStatus verctorHigh`
              : severity === "medium"
              ? `cellWithStatus vectorMedium`
              : severity === "low"
              ? `cellWithStatus vectorLow`
              : `cellWithStatus`
          }
        >
          {params.row.base_metric_v3.cvss_v3.vector || ""}
        </div>
      );
    },
  },

  { field: "published", headerName: "Published", width: 150 },
  { field: "modified", headerName: "Modified", width: 150 },
  // { field: "version", headerName: "Version", width: 150 },
];
