import json


class Settings:
    def __init__(self, info):
        self.connectionString = info["connectionString"]
        self.amountCommission = info["amountCommission"]
        self.baseCommission = info["amountCommission"]
        self.additionalCommission = info["additionalCommission"]

