# sarenka
https://sarenka.readthedocs.io/en/latest/
Everything I like in one place for passive reconnaissance.
Logo was generated with https://www.renderforest.com/
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


# doc
https://app.gitbook.com/@pawlaczyk/s/sarenka/

# Config
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
        "base_url": "https://who.is/"
    },
    "yandex": {
        "base_url": "https://yandex.com/"
    },
    "zoomeye": {
        "base_url": "https://www.zoomeye.org/",
        "user": "<my_user>",
        "api_key": "<my_api_key>"
    }
}
```

# Used libraries
  - https://github.com/achillean/shodan-python (Raw Data in future)

# Thir part services
  - https://censys.io/ (https://censys.io/account/api) (raw data)
  - https://www.shodan.io/
  - https://www.binaryedge.io/
  - https://censys.io/
  - https://fofa.so/
  - https://publicwww.com/
  - https://urlscan.io/
  - https://who.is/
  - https://yandex.com/
  - https://www.zoomeye.org/

  - https://greynoise.io/ (maybe?)
  - https://www.ebay.com/ (helpful when I totally don't know what it is)
  - https://www.amazon.com/ (helpful when I totally don't know what it is)
  - https://allegro.pl/ (helpful when I totally don't know what it is)
  - https://aliexpress.com/ (helpful when I totally don't know what it is)

# Tools
  - https://nmap.org/ 
  - https://github.com/scipag/vulscan
  - nslookup (maybe)
  - netcat (maybe)
  - https://github.com/ElevenPaths/FOCA (maybe)
  - https://github.com/wireshark/wireshark (maybe)
  - https://github.com/VowpalWabbit (maybe)
  - Docker
  - Virtualbox

# Chorme extension
    Open question: Can I get data from them?
  - https://www.wappalyzer.com/
  - https://retirejs.github.io/retire.js/
  - https://github.com/scipag/vulscan
  - https://github.com/scipag/vulscan
  - https://builtwith.com/

# Installation software for testing
  - Docker to temporary installation software on local machine (analyze)

# UI
  - web app with nice interface in Vue.js
  - from command line

