import json

class Common:
    
    @staticmethod
    def save_dict_to_file(filename, data_dict):
        data = json.dumps(data_dict)
        with open(filename, "w") as f:
            f.write(data)

    @staticmethod
    def save_list_to_file(fielname, data_list, separator="\n"):
        data = separator.join(data_list)
        with open(fielname, "w") as f:
            f.write(data)
    
    @staticmethod
    def file_to_dict(filename):
        if isinstance(filename, dict):
            return filename
        
        with open(filename) as f:
            output = f.read()

        return json.loads(output)

    @staticmethod
    def list_flattening(l):
        return sum(l, [])

    @staticmethod
    def parse_to_list(data):
        """
        Parsuje plik do listy
        """
        if isinstance(data, list):
            output = data

        if isinstance(data, str):
            with open(data, "r") as f:
                output = f.readlines()
            output = [i.rstrip() for i in output]

        return output


    @staticmethod
    def dict_to_string(json_dict):
        result = ""
        for item in json_dict.items():
            result += str(item[0]) + ": " + str(item[1]) + "\n"

        return result
    
