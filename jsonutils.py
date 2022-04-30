import json
import datetime
import os


class JsonUtils:
    @staticmethod
    def find_current_path():
        current = datetime.date.today()
        current = current + datetime.timedelta(days=-current.weekday(), weeks=0)
        return JsonUtils.convert_file(current)

    @staticmethod
    def convert_file(current):
        file = str(current) + ".json"
        path = os.path.dirname(os.path.realpath(__file__))
        return rf"{path}\data\{file}"

    @staticmethod
    def write(path, data):
        with open(path, 'w') as writefile:
            writefile.seek(0)
            json.dump(data, writefile, indent=4)

    @staticmethod
    def read(path):
        with open(path, 'r') as outfile:
            outfile.seek(0)
            return json.load(outfile)