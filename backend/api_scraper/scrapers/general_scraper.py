from typing import Dict, Optional, Union
import requests
from requests.exceptions import InvalidSchema, MissingSchema, ConnectionError
from urllib3.exceptions import NewConnectionError
from bs4 import BeautifulSoup
import traceback
from django.conf import settings
import logging.config

print(settings.BASE_DIR)

logging.config.fileConfig('C:\\Users\\dp\\Desktop\\sarenka\\backend\\logging.conf')

logger = logging.getLogger(__name__)
logger.debug("this is a debug message")


class GeneralScraperError(Exception):
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class GeneralScraper:
    """
    Gets general data from website, like keywords, title, image etc.
    """

    def __init__(self, url:str):
        try:
            page = requests.get(url)
        except (InvalidSchema, MissingSchema, ) as err:
            # logging.error(err, exc_info=True)
            logging.error(err)
            raise GeneralScraperError(f'Invalid url "{url}"')
        except (ConnectionError, NewConnectionError) as err:
            # logging.error(err, exc_info=True)
            logging.error(err)
            raise GeneralScraperError(f'Connection error for url "{url}"')
        except:
            logging.error("The error is %s", traceback.format_exc())

        self.soup = BeautifulSoup(page.text, 'html.parser')

    def get_all(self) -> Dict[str, Union[str, Dict[str, str]]]:
        """
        Returns all founded data
        """
        return {
            "title": self.get_title(),
            "description": self.get_description(),
            "keywords": self.get_keywords(),
            "image": self.get_image()
        }

    def get_title(self) -> Optional[str]:
        return self.soup.head.find('title').text if self.soup.head.find('title') else None

    def get_description(self) -> Optional[Dict[str, str]]:
        description = self.soup.head.find('meta', attrs={'name': 'description'})
        meta_description = description.get('content') if description else None

        description = self.soup.find("meta", property="og:description")
        og_description = description.get('content') if description else None

        response = None
        if meta_description or og_description:
            response = {
                "meta_description": meta_description,
                "og_description": og_description
            }

        return response

    def get_keywords(self) -> Optional[str]:
        meta_keywords = self.soup.head.find('meta', attrs={'name': 'keywords'})
        return meta_keywords.get('content') if meta_keywords else None

    def get_image(self):
        og_image = self.soup.find("meta", property="og:image")
        return og_image.get('content') if og_image else None


if __name__ == "__main__":
    try:
        GeneralScraper("https://www.yaheeeeeeeeeeeeeeeeeeeeeeoo.com")
    except:
        print("obsluzone elo")