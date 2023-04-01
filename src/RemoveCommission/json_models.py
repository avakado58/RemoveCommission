import json


class JsonModel:
    def __init__(self, json_string):
        self.__dict__ = json.loads(json_string)


class Voucher(JsonModel):
    pass


class OperationInfo(JsonModel):
    pass


class PriceDetails(JsonModel):
    pass


class Details(JsonModel):
    pass
