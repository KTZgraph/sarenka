<p align="center">
    <img alt="sarenka-logo" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/logo.png">
</p>

[![Release release](https://img.shields.io/badge/release-planned-red.svg)](https://github.com/pawlaczyk/sarenka/releases/latest) [![CircleCi release](https://img.shields.io/badge/coverage-None-green.svg)](https://github.com/pawlaczyk/sarenka/releases/latest) [![CircleCi release](https://img.shields.io/badge/CircleCi-passed-lime.svg)](https://github.com/pawlaczyk/sarenka/releases/latest) [![Platform release](https://img.shields.io/badge/platform-Windows-blue.svg)](https://github.com/pawlaczyk/sarenka/releases/latest) ![CWE feed](https://img.shields.io/badge/CWE-12/20/2020-darkgreen.svg) [![license](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/pawlaczyk/sarenka/blob/master/LICENSE) 


**♥ Free Software, requires only free accounts to third part services ♥**

> Lack of knowledge ... that is the problem.
>
>
>[William Edwards Deming]


**SARENKA** is Open Source Intelligence (**OSINT**) tool which helps you obtaining and understanding **Attack Surface**.

The main goal is to gathering infromation from search engines for Internet-connected devices (**https://censys.io/**, **https://www.shodan.io/**).
It scraps data about Common Vulnerabilities and Exposures (**CVE**), Common Weakness Enumeration (**CWE**) and also has database where CVEs are mapped to CWE.

It returns data about local machine - local installed softwares (from Windows Registry), local network information (python libraries, popular cmd commads).

For now application has also simple tools like hash calcualtor, shannon entropy calculator and very simple port scanner. 
More cryptography-math tools and reconnaissance scripts are planned.

#### Look
https://www.facebook.com/ncybersec/posts/1671427243027993

# Realtion beetwen CWE and CVE - sarenka data feeder
Generating this file takes a long time e.g: 702.5641514
#### all CWE Ids with description
https://raw.githubusercontent.com/pawlaczyk/sarenka_tools/master/cwe_all.json

#### all CVE Ids with description
In progress

#### get all CVE Ids by CWE Id
In progress

# Installation
Description in progress

# Getting started 
Description in progress
Sarenka is local web application for Windows.

#### Config
Rirst release gathers data from two search engines.
example sarenka/backend/connectors/credentials.json  

```json
{   
    "censys": {
        "base_url": "https://censys.io/",
        "API_ID": "<my_user>",
        "Secret": "<my_api_key>",
        "API_URL": "https://censys.io/api/v1"
    },
    "shodan": {
        "base_url": "https://www.shodan.io/",
        "user": "<my_user>",
        "api_key": "<my_api_key>"
    }
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

- Whant some feature, other tool, library functionality?
- Have any idea or question?  [![alt text][1.1]][1]
- Don't hesitate to contact  [![Author](https://img.shields.io/badge/pawlaczyk-black.svg)](https://github.com/pawlaczyk/) .

# Database
This is tricki part, because we have 863 sqlite3 database files: default, CWE-NONE (some CVE hasn't cwe_id eg.: CVE-2013-3621) and 861 individual for CWEs 

## Tech
Description in progress.

SARENKA uses a number of open source projects to work properly on:
* [Renderforest](https://www.renderforest.com/) - logo generator
* [gawk](http://gnuwin32.sourceforge.net/packages/gawk.htm) - python manage.py migrate --database CWE_ID 
* [chocolatey](https://chocolatey.org/)
* [PyCharm](https://www.jetbrains.com/pycharm/) - Community Edition
* [Technology](url_address) - description
* [Technology](url_address) - description
* [Technology](url_address) - description
* [Technology](url_address) - description
* [Technology](url_address) - description
* [Technology](url_address) - description
* [Technology](url_address) - description
* [Technology](url_address) - description
* [Technology](url_address) - description
* [Technology](url_address) - description



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
[Mirrors]: http://mirrors.jenkins-ci.org
[GitHub]: https://github.com/pawlaczyk/sarenka
[documentation]: https://pawlaczyk.github.io/sarenka/
[public repository]: https://github.com/pawlaczyk/sarenka


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [sarenka]: <https://github.com/pawlaczyk/sarenka>
   [git-repo-url]: <https://github.com/pawlaczyk/sarenka>
   [William Edwards Deming]: <https://deming.org/deming-the-man/>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
