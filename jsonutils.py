import json
import datetime
import os


class JsonUtils:
    @staticmethod
    def find_current_path():
        """
        :return: The string representation of the current weekly data path
        """
        current = datetime.date.today()
        current = current + datetime.timedelta(days=-current.weekday(), weeks=0)
        return JsonUtils.convert_file(current)

    @staticmethod
    def convert_file(current):
        """
        :param current: a given Monday (the start of the week)
        :return: the string representation of the data path
        """
        file = str(current) + ".json"
        path = os.path.dirname(os.path.realpath(__file__))
        return rf"{path}\data\{file}"

    @staticmethod
    def write(path, data):
        """
        Writes data to the json file on the given path
        :param path: self-explanatory
        :param data: self-explanatory
        """
        with open(path, 'w+') as writefile:
            writefile.seek(0)
            json.dump(data, writefile, indent=4)

    @staticmethod
    def read(path):
        """
        Reads data from the given json file path
        :param path: self-explanatory
        """
        with open(path, 'r+') as outfile:
            outfile.seek(0)
            return json.load(outfile)