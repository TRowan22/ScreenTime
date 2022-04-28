import json
import datetime


def find_current_path():
    current = datetime.date.today()
    current = current + datetime.timedelta(days=-current.weekday(), weeks=0)
    return convert_file(current)


def convert_file(current):
    file = str(current) + ".json"
    return rf"C:\Users\tsrow\PycharmProjects\ScreenTime\data\{file}"


def write(path, data):
    with open(path, 'w') as writefile:
        writefile.seek(0)
        json.dump(data, writefile, indent=4)


def read(path):
    with open(path, 'r') as outfile:
        outfile.seek(0)
        return json.load(outfile)