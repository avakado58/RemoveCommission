import json
from config.settings import Settings


class ConfigReader:
    @staticmethod
    def read():
        with open("./.config/config.json", encoding="utf-8") as file:
            return Settings(json.loads(file.read()))
