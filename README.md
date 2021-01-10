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

#### SARENKA was mentioned here:
* [ncybersec](https://www.facebook.com/ncybersec/posts/1671427243027993)
* [llllap3xllll](https://www.instagram.com/p/CI8tXMNg3yI/)
* [securityonline.info](https://securityonline.info/sarenka-obtaining-and-understanding-attack-surface//)
* [haxf4rall.com](https://haxf4rall.com/2020/12/30/sarenka-obtaining-and-understanding-attack-surface/)
* [hackdig.com](http://hackdig.com/12/hack-245463.htm)
* [findglocal.com](http://www.findglocal.com/BR/Ananindeua/1436460569931544/Computer-Network-%26-Technology)
* [台灣數位國土安全部 - DDHS](https://www.facebook.com/DDHS.TW/)
* [laptrinhx.com](https://laptrinhx.com/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place-3347349303/)
* [kitploit.com](https://www.kitploit.com/2021/01/sarenka-osint-tool-data-from-services.html)
* [attackware.com](https://attackware.com/index.php/2021/01/07/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/security-world-news/admin/)
* [hacking.land](https://www.hacking.land/2021/01/sarenka-osint-tool-data-from-services.html)
* [cyberfishnews.com](https://cyberfishnews.com/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place-19097.html)
* [modernnetsec.io](https://modernnetsec.io/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/)
* [spywarenews.com](https://spywarenews.com/index.php/2021/01/07/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/security-world-news/admin/)
* [cert.europa.eu](https://cert.europa.eu/cert/alertedition/en/VulnerabilitiesDBMS.html)
* [dfir.pro](http://dfir.pro/index.php?link_id=109300&utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+dfirpro+%28IT+%26+Security+NewsFeed+%29)
* [iransec.net](https://iransec.net/forums/topic/550-sarenka/?tab=comments#comment-605)
* [hacker-gadgets.com](https://hacker-gadgets.com/blog/2021/01/07/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/)
* [vulners.com](https://vulners.com/kitploit/KITPLOIT:491559930238488010)
* [redpacketsecurity.com](https://www.redpacketsecurity.com/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/)
* [kali-linuxtr.net](https://kali-linuxtr.net/sarenka-open-source-intelligence-osint-tool)
* [anonymousmedia.org](https://anonymousmedia.org/2021/01/07/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/)
* [pentesttools.net](https://pentesttools.net/sarenka-osint-tool-data-from-services-like-shodan-censys-etc/)
* [wangshit.xyz](https://wangshit.xyz/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/)
* [geekychild.com](https://geekychild.com/hack-penetration-tool/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/)
* [hacker.observer](https://hacker.observer/sarenka-osint-tool-data-from-services-like-shodan-censys-etc-in-one-place/)
* [nuomiphp.com](https://www.nuomiphp.com/github/zh/5ff88c65e4570e7ee973117d.html)
* [danielonsecurity.com](https://danielonsecurity.com/links/)



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
  - check is **port** open|closed (instead always use nmap if you can - it is slow)


# Installation

## Installation from sources
- Application has been tested manually in Kali Linux kali-rolling 2020.2; Python 3.8.2; Node
- Application has been tested manually in Windows 10; Python 3.8.5; Node v12.13.0


##### Clone repository
```
$ git clone https://github.com/pawlaczyk/sarenka.git
```
##### Go to source appliction directory
```
$ cd sarenka/sarenka
```

###Create and activate virtualenv - depends on OS!
#### Linux

```
# python virtualenv manually; you can change "sarenka_env"

$ pip3 install virtualenv
$ virtualenv sarenka_env
$ virtualenv sarenka_env
$ source sarenka_env/bin/activate
```

#### Windows
```
> python -m venv sarenka_env
> sarenka_env\Scripts\activate
```

#### With sarenka.py script
```
# script checks OS and creates proper 'sarenka_env' 
python sarenka.py --env
```
##### activate sarenka_env in Linux
```
# script creates "sarenka_env" now this name is required
$ source sarenka_env/bin/activate
```
##### activate sarenka_env in Windows
```
# script creates "sarenka_env" now this name is required
$ sarenka_env\Scripts\activate
```

##### Build application with sarenka.py script
```
$ python sarenka.py --build
```
##### Run backend application - Django
```
$ python backend/manage.py runserver
```
##### Run frontent application - React


# Getting started 

####Please create accounts on this services:
- https://account.shodan.io/register
- https://censys.io/register

#### Next go to 'Settings' tab and add user credentials:
<img alt="sarenka-settigs" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/readmeStatic/Screenshot 2021-01-08 213602.png">


###### Or if you are using only backend send this POST request to <server_addres>/api/user_credentials endpoint
```json
{
    "censys.api_id": "<censys_API_ID>",
    "censys.secret" : "<censys_Secret>",
    "shodan.user": "<shodan_user>",
    "shodan.api_key": "<shodan_api_key>"
}
```




# Screenshots
<img alt="sarenka-main-harwdare" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/readmeStatic/Screenshot 2021-01-07 234911.png">

<img alt="sarenka-cve" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/readmeStatic/Screenshot 2021-01-07 235528.png">

<img alt="sarenka-windows-registry" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/readmeStatic/Screenshot 2021-01-07 235615.png">

<img alt="sarenka-censys" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/readmeStatic/Screenshot 2021-01-08 213333.png">

<img alt="sarenka-cwe" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/readmeStatic/Screenshot 2021-01-08 213519.png">

<img alt="sarenka-swagger" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/readmeStatic/swagger.png">






#### Suggestions are welcome
[1.1]: http://i.imgur.com/tXSoThF.png (twitter icon with padding)
[2.1]: http://i.imgur.com/P3YfQoD.png (facebook icon with padding)

[1]: https://twitter.com/OsintSarenka
[2]: https://www.facebook.com/sarenka.osint.5

- Want some feature, other tool, library functionality?
- Have any idea or question?  [![alt text][1.1]][1]
- Don't hesitate to contact  [![Author](https://img.shields.io/badge/pawlaczyk-black.svg)](https://github.com/pawlaczyk/) .


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


