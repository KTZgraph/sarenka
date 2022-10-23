export const datatableColumns = [
  { field: "code", headerName: "ID", width: 120 },
  {
    field: "cvss",
    headerName: "CVSS",
    width: 100,
    renderCell: (params) => {
      // CVSSV3
      const baseScoreV3 = params.row.base_metric_v3.cvss_v3.base_score || "";
      let severityV3 = params.row.base_metric_v3.cvss_v3.base_severity;
      severityV3 ? (severityV3 = severityV3.toLowerCase()) : (severityV3 = "");
      // CVSSV2

      const baseScoreV2 = params.row.base_metric_v2.cvss_v2.base_score || "";
      let severityV2 = params.row.base_metric_v2.severity;
      severityV2 ? (severityV2 = severityV2.toLowerCase()) : (severityV2 = "");

      return (
        <div className="cellMultiple">
          <div
            className={
              severityV3 === "critical"
                ? "cellWithStatus critical"
                : severityV3 === "high"
                ? "cellWithStatus high"
                : severityV3 === "medium"
                ? "cellWithStatus high"
                : severityV3 === "low"
                ? "cellWithStatus low"
                : "cellWithStatus"
            }
          >
            {baseScoreV3}
          </div>
          <div
            className={
              severityV2 === "critical"
                ? "cellWithStatus critical"
                : severityV2 === "high"
                ? "cellWithStatus high"
                : severityV2 === "medium"
                ? "cellWithStatus high"
                : severityV2 === "low"
                ? "cellWithStatus low"
                : "cellWithStatus"
            }
          >
            {baseScoreV2}
          </div>
        </div>
      );
    },
  },
  { field: "cwe_code", headerName: "CWE", width: 100 },
  { field: "description", headerName: "Description", flex: 1 },
];
