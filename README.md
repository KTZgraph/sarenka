<p align="center">
    <img alt="sarenka-logo" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/logo.png">
</p>

[![Release release](https://img.shields.io/badge/release-planned-red.svg)](https://github.com/pawlaczyk/sarenka/releases/latest) [![CircleCi release](https://img.shields.io/badge/coverage-None-green.svg)](https://github.com/pawlaczyk/sarenka/releases/latest) [![CircleCi release](https://img.shields.io/badge/CircleCi-passed-lime.svg)](https://github.com/pawlaczyk/sarenka/releases/latest) ![Platform release](https://img.shields.io/badge/platform-Windows-blue.svg) [![Platform release](https://img.shields.io/badge/platform-Linux-purple.svg)](https://github.com/pawlaczyk/sarenka/releases/latest) ![CWE feed](https://img.shields.io/badge/CWE-12/20/2020-darkgreen.svg) ![CVE feed](https://img.shields.io/badge/CVE-12/19/2020-green.svg) [![license](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/pawlaczyk/sarenka/blob/master/LICENSE) 



**♥ Free Software, requires only free accounts to third part services ♥**

> Lack of knowledge ... that is the problem.
>
>
>[William Edwards Deming]


**SARENKA** is an Open Source Intelligence (**OSINT**) tool which helps you obtaining and understanding **Attack Surface**.

The main goal is to gathering infromation from search engines for Internet-connected devices (**https://censys.io/**, **https://www.shodan.io/**).
It scraps data about Common Vulnerabilities and Exposures (**CVE**), Common Weakness Enumeration (**CWE**) and also has database where CVEs are mapped to CWE.

It returns data about local machine - local installed softwares (from Windows Registry), local network information (python libraries, popular cmd commads).

For now application has also simple tools like hash calcualtor, shannon entropy calculator and very simple port scanner. 
More cryptography-math tools and reconnaissance scripts are planned.

# Screenshots
<img alt="sarenka-logo" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/readmeStatic/Screenshot 2021-01-07 234911.png">

<img alt="sarenka-logo" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/readmeStatic/Screenshot 2021-01-07 235528.png">

<img alt="sarenka-logo" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/readmeStatic/Screenshot 2021-01-07 235615.png">

#### Look
- https://www.facebook.com/ncybersec/posts/1671427243027993
- https://www.instagram.com/p/CI8tXMNg3yI/
- https://securityonline.info/sarenka-obtaining-and-understanding-attack-surface/
- https://haxf4rall.com/2020/12/30/sarenka-obtaining-and-understanding-attack-surface/
- http://hackdig.com/12/hack-245463.htm
- http://www.findglocal.com/BR/Ananindeua/1436460569931544/Computer-Network-%26-Technology
- https://www.facebook.com/DDHS.TW/
- https://laptrinhx.com/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place-3347349303/
- https://www.kitploit.com/2021/01/sarenka-osint-tool-data-from-services.html
- https://attackware.com/index.php/2021/01/07/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/security-world-news/admin/
- https://www.hacking.land/2021/01/sarenka-osint-tool-data-from-services.html
- https://cyberfishnews.com/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place-19097.html
- https://modernnetsec.io/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/
- https://spywarenews.com/index.php/2021/01/07/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/security-world-news/admin/
- https://cert.europa.eu/cert/alertedition/en/VulnerabilitiesDBMS.html
- http://dfir.pro/index.php?link_id=109300&utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+dfirpro+%28IT+%26+Security+NewsFeed+%29
- https://iransec.net/forums/topic/550-sarenka/?tab=comments#comment-605
- https://hacker-gadgets.com/blog/2021/01/07/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/
- https://vulners.com/kitploit/KITPLOIT:491559930238488010
- https://www.redpacketsecurity.com/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/
- https://kali-linuxtr.net/sarenka-open-source-intelligence-osint-tool


# Installation
Description in progress.

# Getting started 
Description in progress.

#### Config POST
```json
{
    "censys.api_id": "<censys_API_ID>",
    "censys.secret" : "<censys_Secret>",
    "shodan.user": "<shodan_user>",
    "shodan.api_key": "<shodan_api_key>"
}
```


# Features
  - gets data from **https://censys.io/** by ip
  - get data from **https://www.shodan.io/** by ip
  - get **DNS** data
  - get **WHOIS** data
  - **banner** grabbing
  - find **CVEs** by **CWE** 
  - generatre pdf report

You can also:
  - calculate **hashes** based on user string
  - calculate **shannon entropy** based on user string
  - check is **port** open|closed (instead always use nmap if you can - it's slow)

#### Suggestions are welcome
[1.1]: http://i.imgur.com/tXSoThF.png (twitter icon with padding)
[2.1]: http://i.imgur.com/P3YfQoD.png (facebook icon with padding)

[1]: https://twitter.com/OsintSarenka
[2]: https://www.facebook.com/sarenka.osint.5

- Want some feature, other tool, library functionality?
- Have any idea or question?  [![alt text][1.1]][1]
- Don't hesitate to contact  [![Author](https://img.shields.io/badge/pawlaczyk-black.svg)](https://github.com/pawlaczyk/) .

#### Databases
Details in documentation.

## Tech
* [Renderforest](https://www.renderforest.com/)
* [gawk](http://gnuwin32.sourceforge.net/packages/gawk.htm) 
* [chocolatey](https://chocolatey.org/)
* [PyCharm](https://www.jetbrains.com/pycharm/)



And of course SARENKA itself is open source with a [public repository][sarenka]
 on GitHub.

#### Planned features

 - Rewrite documentation in English (end of 2021)
 - trello/ github instead of Jira
 - Cover 100% code by tests
 - typing backend
 - document all functions and class
 - Docker
 - online demo
 - Jenkins
 - GraphQL
 - Selenium Scrapers
 - More pentesting tools
 - Google Dorks
 - Abstract Algebra calculator
 - Number Theory calculator
 - Server certificate validator
 - tests on Linux
 - NLP
 - d3js visualizations
 - alterntive pure version in command lineS

##### CI/CD Tools
- https://circleci.com/
- https://github.com/snyk-bot

#### Tests
- Tested on Windows 10
- Tested on Kali Linux kali-rolling 2020.2

### Documentation
Till end of March, 2021 documentation will be available only in Polish!
The documentation is availabe [here](https://pawlaczyk.github.io/sarenka/).

# Authors
[![Author](https://img.shields.io/badge/Dominika-Pawlaczyk-red.svg)](https://github.com/pawlaczyk/)  [![Author](https://img.shields.io/badge/Michał-Pawlaczyk-red.svg)](https://github.com/michalpawlaczyk) [![Author](https://img.shields.io/badge/Karolina-Słonka-red.svg)](https://github.com/k-slonka)


##### Contact
[![Author](https://img.shields.io/badge/pawlaczyk-black.svg)](https://github.com/pawlaczyk/)

# License
SARENKA is **licensed** under the **[MIT License]**.

[MIT License]: https://github.com/pawlaczyk/sarenka/blob/master/LICENSE
[GitHub]: https://github.com/pawlaczyk/sarenka
[documentation]: https://pawlaczyk.github.io/sarenka/
[public repository]: https://github.com/pawlaczyk/sarenka


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [sarenka]: <https://github.com/pawlaczyk/sarenka>
   [git-repo-url]: <https://github.com/pawlaczyk/sarenka>
   [William Edwards Deming]: <https://deming.org/deming-the-man/>


