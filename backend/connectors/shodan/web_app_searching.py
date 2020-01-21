import re

from web_app_searching_interface import WebAppSearchingInterface


class WebAppSearching(WebAppSearchingInterface):
    def __init__(self, host_wrapper):
        super.__init__(host_wrapper)
    
    def search_version(self):
        pattern = ".*".join([i for i in self.host.query])+"\d+" #TODO:
        result = re.search(pattern, self.host.html)
        print(result)
