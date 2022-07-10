missed_cve_list = [
    {
        "id": "CWE-17",
        "name": "DEPRECATED: Code",
        "abstraction": "",
        "structure": "",
        "status": "DEPRECATED",
        "description": "",
        "extended_description": "This entry has been deprecated. It was originally used for organizing the Development View (CWE-699) and some other views, but it introduced unnecessary complexity and depth to the resulting tree."
    },
    {
        "id": "NVD-CWE-noinfo",
        "name": "Insufficient Information",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "There is insufficient information about the issue to classify it; details are unkown or unspecified.",
        "extended_description": ""
    },
    {
        "id": "NVD-CWE-Other",
        "name": "Other",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "",
        "extended_description": "NVD is only using a subset of CWE for mapping instead of the entire CWE, and the weakness type is not covered by that subset."
    },
    {
        "id": "CWE-399",
        "name": "Resource Management Errors",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "",
        "extended_description": "Weaknesses in this category are related to improper management of system resources."
    },
    {
        "id": "CWE-840",
        "name": "Business Logic Errors",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Weaknesses in this category identify some of the underlying problems that commonly allow attackers to manipulate the business logic of an application. Errors in business logic can be devastating to an entire application.",
        "extended_description": "They can be difficult to find automatically, since they typically involve legitimate use of the application's functionality. However, many business logic errors can exhibit patterns that are similar to well-understood implementation and design weaknesses."
    },
    {
        "id": "CWE-310",
        "name": "Cryptographic Issues",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Weaknesses in this category are related to the design and implementation of data confidentiality and integrity.",
        "extended_description": "Frequently these deal with the use of encoding techniques, encryption libraries, and hashing algorithms. The weaknesses in this category could lead to a degradation of the quality data if they are not addressed."
    },
    {
        "id": "CWE-254",
        "name": "7PK - Security Features",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Software security is not security software.",
        "extended_description": "Here we're concerned with topics like authentication, access control, confidentiality, cryptography, and privilege management."
    },
    {
        "id": "CWE-361",
        "name": "7PK - Time and State",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "This category represents one of the phyla in the Seven Pernicious Kingdoms vulnerability classification.",
        "extended_description": " It includes weaknesses related to the improper management of time and state in an environment that supports simultaneous or near-simultaneous computation by multiple systems, processes, or threads."
    },
    {
        "id": "CWE-388",
        "name": "7PK - Errors",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "This category represents one of the phyla in the Seven Pernicious Kingdoms vulnerability classification. It includes weaknesses that occur when an application does not properly handle errors that occur during processing.",
        "extended_description": "According to the authors of the Seven Pernicious Kingdoms, \"Errors and error handling represent a class of API. Errors related to error handling are so common that they deserve a special kingdom of their own. As with 'API Abuse,' there are two ways to introduce an error-related security vulnerability: the most common one is handling errors poorly (or not at all). The second is producing errors that either give out too much information (to possible attackers) or are difficult to handle.\""
    },
    {
        "id": "CWE-189",
        "name": "Numeric Errors",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Weaknesses in this category are related to improper calculation or conversion of numbers.",
        "extended_description": ""
    },
    {
        "id": "CWE-417",
        "name": "Communication Channel Errors",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Weaknesses in this category are related to improper handling of communication channels and access paths.",
        "extended_description": "These weaknesses include problems in creating, managing, or removing alternate channels and alternate paths. Some of these can overlap virtual file problems and are commonly used in \"bypass\" attacks, such as those that exploit authentication errors."
    },
    {
        "id": "CWE-264",
        "name": "Permissions, Privileges, and Access Controls",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Weaknesses in this category are related to the management of permissions, privileges, and other security features that are used to perform access control.",
        "extended_description": ""
    },
    {
        "id": "CWE-21",
        "name": "DEPRECATED: Pathname Traversal and Equivalence Errors",
        "abstraction": "",
        "structure": "",
        "status": "DEPRECATED",
        "description": "This category has been deprecated. It was originally used for organizing weaknesses involving file names, which enabled access to files outside of a restricted directory (path traversal) or to perform operations on files that would otherwise be restricted (path equivalence).",
        "extended_description": "Consider using either the File Handling Issues category (CWE-1219) or the class Use of Incorrectly-Resolved Name or Reference (CWE-706)."
    },
    {
        "id": "CWE-275",
        "name": "Permission Issues",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Weaknesses in this category are related to improper assignment or handling of permissions.",
        "extended_description": ""
    },
    {
        "id": "CWE-199",
        "name": "Information Management Errors",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Weaknesses in this category are related to improper handling of sensitive information.",
        "extended_description": ""
    },
    {
        "id": "CWE-320",
        "name": "Key Management Errors",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Weaknesses in this category are related to errors in the management of cryptographic keys.",
        "extended_description": ""
    },
    {
        "id": "CWE-19",
        "name": "Data Processing Errors",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Weaknesses in this category are typically found in functionality that processes data. Data processing is the manipulation of input to retrieve or save information.",
        "extended_description": ""
    },
    {
        "id": "CWE-895",
        "name": "SFP Primary Cluster: Information Leak",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "This category identifies Software Fault Patterns (SFPs) within the Information Leak cluster (SFP23).",
        "extended_description": ""
    },
    {
        "id": "CWE-16",
        "name": "Configuration",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Weaknesses in this category are typically introduced during the configuration of the software.",
        "extended_description": ""
    },
    {
        "id": "CWE-18",
        "name": "DEPRECATED: Source Code",
        "abstraction": "",
        "structure": "",
        "status": "DEPRECATED",
        "description": "This entry has been deprecated. It was originally used for organizing the Development View (CWE-699) and some other views, but it introduced unnecessary complexity and depth to the resulting tree.",
        "extended_description": ""
    },
    {
        "id": "CWE-255",
        "name": "Credentials Management Errors",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Weaknesses in this category are related to the management of credentials.",
        "extended_description": ""
    },
    {
        "id": "CWE-1",
        "name": "DEPRECATED: Location",
        "abstraction": "",
        "structure": "",
        "status": "DEPRECATED",
        "description": "This category has been deprecated. It was originally used for organizing the Development View (CWE-699), but it introduced unnecessary complexity and depth to the resulting tree.",
        "extended_description": ""
    },
    {
        "id": "CWE-371",
        "name": "State Issues",
        "abstraction": "",
        "structure": "",
        "status": "",
        "description": "Weaknesses in this category are related to improper management of system state.",
        "extended_description": ""
    }
]