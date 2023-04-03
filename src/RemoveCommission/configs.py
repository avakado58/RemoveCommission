import json


class ConfigReader:
    @staticmethod
    def read():
        with open("config.json", encoding="utf-8") as file:
            return Settings(json.loads(file.read()))


class Settings:
    def __init__(self, info):
        self.connectionStringSQLAlchemy = info["connectionStringSQLAlchemy"]
        self.connectionStringPyodbc = info["connectionStringPyodbc"]
        self.amountCommission = info["amountCommission"]
        self.commission = info["commission"]
        self.fee = info["fee"]
        self.companyId = info["companyId"]