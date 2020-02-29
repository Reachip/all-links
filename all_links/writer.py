import json


class FileWriter:
    def __init__(self, filename):
        self._file = open(filename, "w+")

    def write_architecture_to_json(self, website_arch):
        self._file.write(website_arch.to_json())

    def write_architecture_to_xml(self, website_arch):
        self._file.write(website_arch.to_xml())
