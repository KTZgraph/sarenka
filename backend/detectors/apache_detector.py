import yaml
import pprint



from base_detector import BaseDetector

class ApacheDetector(BaseDetector):
    def __init__(self, filename):
        self.name = "apache"
        


        with open(self.plugin_path) as f:
            data_map = yaml.safe_load(f)

        pprint.pprint(data_map)
    
    def process(self):
        print("apache process")


if __name__ == "__main__":
    apache_detector = ApacheDetector("apache.yaml")
    # C:\Users\dp\Desktop\sarenka\backend\detectors\apache_detector.py