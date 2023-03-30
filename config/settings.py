class Settings:
    def __init__(self, info):
        self.connectionStringSQLAlchemy = info["connectionStringSQLAlchemy"]
        self.connectionStringPyodbc = info["connectionStringPyodbc"]
        self.amountCommission = info["amountCommission"]
        self.baseCommission = info["amountCommission"]
        self.additionalCommission = info["additionalCommission"]
        self.companyId = info["companyId"]

