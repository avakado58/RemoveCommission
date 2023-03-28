import json


class ConfigReader:
    @staticmethod
    def read():
        with open("./.config/config.json", encoding="utf-8") as file:
            return json.loads(file.read())
