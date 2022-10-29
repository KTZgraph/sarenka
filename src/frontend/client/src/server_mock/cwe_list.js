// class CWE(models.Model):
//     code = models.CharField(max_length=20, unique=True)
//     #pole name z xmla to  krókie opisy jak  z https://nvd.nist.gov/vuln/categories
//     name = models.TextField(null=False)
//     abstraction = models.CharField(max_length=100)
//     structure = models.CharField(max_length=100)
//     status = models.CharField(max_length=100)
//     description = models.TextField(null=False)
//     extended_description = models.TextField(null=True)

export const cweList = [
  {
    // code: "CVE-2021-34563",
    id: 1,
    code: "CWE-1004",
    name: "Sensitive Cookie Without 'HttpOnly' Flag",
    abstraction: "Variant",
    structure: "Simple",
    status: "Incomplete",
    description:
      "The software uses a cookie to store sensitive information, but the cookie is not marked with the HttpOnly flag.",
    extended_description:
      "The HttpOnly flag directs compatible browsers to prevent client-side script from accessing cookies. Including the HttpOnly flag in the Set-Cookie HTTP response header helps mitigate the risk associated with Cross-Site Scripting (XSS) where an attacker's script code might attempt to read the contents of a cookie and exfiltrate information obtained. When set, browsers that support the flag will not reveal the contents of the cookie to a third party via client-side script executed via XSS.",
  },
  {
    // code: "CVE-2021-34564",

    id: 439,
    code: "CWE-315",
    name: "Cleartext Storage of Sensitive Information in a Cookie",
    abstraction: "Variant",
    structure: "Simple",
    status: "Draft",
    description:
      "The application stores sensitive information in cleartext in a cookie.",
    extended_description:
      "Attackers can use widely-available tools to view the cookie and read the sensitive information. Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.",
  },
  {
    // "code": "CVE-2021-37177",
    //  "code": "CVE-2021-37193",
    //   "code": "CVE-2021-42701",
    // "code": "CVE-2020-26237",
    // "code": "CVE-2018-3728",
    id: 589,
    code: "CWE-471",
    name: "Modification of Assumed-Immutable Data (MAID)",
    abstraction: "Base",
    structure: "Simple",
    status: "Draft",
    description:
      "The software does not properly protect an assumed-immutable element from being modified by an attacker.",
    extended_description:
      "This occurs when a particular input is critical enough to the functioning of the application that it should not be modifiable at all, but it is. Certain resources are often assumed to be immutable when they are not, such as hidden form fields in web applications, cookies, and reverse DNS lookups.",
  },
  {
    //  code: "CVE-2021-21423",
    id: 642,
    code: "CWE-527",
    name: "Exposure of Version-Control Repository to an Unauthorized Control Sphere",
    abstraction: "Variant",
    structure: "Simple",
    status: "Incomplete",
    description:
      "The product stores a CVS, git, or other repository in a directory, archive, or other resource that is stored, transferred, or otherwise made accessible to unauthorized actors.",
    extended_description:
      'Version control repositories such as CVS or git store version-specific metadata and other details within subdirectories. If these subdirectories are stored on a web server or added to an archive, then these could be used by an attacker. This information may include usernames, filenames, path root, IP addresses, and detailed "diff" data about how files have been changed - which could reveal source code snippets that were never intended to be made public.',
  },
  {
    // code: "CVE-2020-7591",
    id: 723,
    code: "CWE-603",
    name: "Use of Client-Side Authentication",
    abstraction: "Base",
    structure: "Simple",
    status: "Draft",
    description:
      "A client/server product performs authentication within client code but not in server code, allowing server-side authentication to be bypassed via a modified client that omits the authentication check.",
    extended_description:
      "Client-side authentication is extremely weak and may be breached easily. Any attacker may read the source code and reverse-engineer the authentication mechanism to access parts of the application which would otherwise be protected.",
  },
  {
    //  "code": "CVE-2020-11080",
    // "code": "CVE-2019-10052",
    // "code": "CVE-2018-3918",
    id: 816,
    code: "CWE-707",
    name: "Improper Neutralization",
    abstraction: "Pillar",
    structure: "Simple",
    status: "Incomplete",
    description:
      "The product does not ensure or incorrectly ensures that structured messages or data are well-formed and that certain security properties are met before being read from an upstream component or sent to a downstream component.",
    extended_description:
      "If a message is malformed, it may cause the message to be incorrectly interpreted.",
  },
];
