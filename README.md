<p align="center">
    <img alt="sarenka-logo" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/logo.png">
</p>

[![Release release](https://img.shields.io/badge/release-planned-red.svg)](https://github.com/pawlaczyk/sarenka/releases/latest) [![CircleCi release](https://img.shields.io/badge/coverage-None-green.svg)](https://github.com/pawlaczyk/sarenka/releases/latest) [![CircleCi release](https://img.shields.io/badge/CircleCi-passed-lime.svg)](https://github.com/pawlaczyk/sarenka/releases/latest) [![Platform release](https://img.shields.io/badge/platform-Windows-blue.svg)](https://github.com/pawlaczyk/sarenka/releases/latest)  [![license](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/pawlaczyk/sarenka/blob/master/LICENSE) 

**♥ Free Software, requires only free accounts to third part services ♥**

> Lack of knowledge ...
> that is the problem.
[William Edwards Deming]

**SARENKA** is Open Source Intelligence (**OSINT**) tool which helps you obtaining and understanding **Attack Surface**.

The main goal is to gathering infromation from search engines for Internet-connected devices (**https://censys.io/**, **https://www.shodan.io/**).
It scraps data about Common Vulnerabilities and Exposures (**CVE**), Common Weakness Enumeration (**CWE**) and also has database where CVEs are mapped to CWE.

It returns data about local machine - local installed softwares (from Windows Registry), local network information (python libraries, popular cmd commads).

For now application has also simple tools like hash calcualtor, shannon entropy calculator and very simple port scanner. 
More cryptography-math tools and reconnaissance scripts are planned.

# Installation
Description in progress

# Getting started 
Description in progress
Sarenka is local web application for Windows.

#### Config
example sarenka/backend/connectors/credentials.json

```json
{   
    "binaryedge": {
        "base_url": "https://www.binaryedge.io/",
        "user": "<my_user>",
        "api_key": "<my_api_key>"
    },
    "censys": {
        "base_url": "https://censys.io/",
        "API_ID": "<my_user>",
        "Secret": "<my_api_key>",
        "API_URL": "https://censys.io/api/v1"
    },
    "fofa": {
        "base_url": "https://fofa.so/",
        "user": "<my_user>",
        "api_key": "<my_api_key>"
    },
    "publicwww": {
        "base_url": "https://publicwww.com/",
        "user": "<my_user>",
        "api_key": "<my_api_key>"
    },
    "shodan": {
        "base_url": "https://www.shodan.io/",
        "user": "<my_user>",
        "api_key": "<my_api_key>"
    },
    "urlscan": {
        "base_url": "https://urlscan.io/"
    },
    "whois": {
        "base_url": "https://www.whoisxmlapi.com/"
    },
    "zoomeye": {
        "base_url": "https://www.zoomeye.org/",
        "user": "<my_user>",
        "api_key": "<my_api_key>"
    },
    "cve_search":{
        "base_url": "https://cve.circl.lu/api/",
        "cve": "https://cve.circl.lu/api/cve/",
        "vendor": "https://cve.circl.lu/api/browse/",
        "last": "https://cve.circl.lu/api/last",
        "db_info": "https://cve.circl.lu/api/dbInfo"
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
Whant some feature, other tool, library functionality?
Have any idea or question?  
Don't hesitate to contact  [![Author](https://img.shields.io/badge/pawlaczyk-black.svg)](https://github.com/pawlaczyk/)

#### Tech

SARENKA uses a number of open source projects to work properly on:
* [Renderforest](https://www.renderforest.com/) - logo generator
* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [Breakdance](https://breakdance.github.io/breakdance/) - HTML to Markdown converter
* [jQuery] - duh

And of course SARENKA itself is open source with a [public repository][sarenka]
 on GitHub.

#### Planned features

 - Rewrite documentation in English (end of 2021)
 - trello/ github insead Jira
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
