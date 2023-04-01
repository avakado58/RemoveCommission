import json
import jsonpickle
from typing import List
from src.RemoveCommission.configs import Settings
from src.RemoveCommission.json_models import Voucher, PriceDetails, OperationInfo, Details
from src.RemoveCommission.models import DbTripItemVersion, DbPaymentInvoice
from src.RemoveCommission.repository import Repository
from src.RemoveCommission.sql import PureSql


class CommissionService:
    def __init__(self, repository: Repository, pure_sql: PureSql, settings: Settings):
        self.__pure_sql = pure_sql
        self.__repository = repository
        self.__settings = settings

    def remove_ticket_commission(self, ticket_number: List[int], company_id: int):
        ids = self.__pure_sql.get_version_id(ticket_number, company_id)
        payment_operation_ids = self.__pure_sql.get_payment_operation_id(ids)
        details_id, operation_ids = self.__repository.update_operation_details(ids)
        self.__repository.update_detail_price(details_id)

        payments = self.__repository.get_payment(payment_operation_ids)
        version = self.__repository.get_versions(ids)
        self.__versions_process(version)
        self.__payments_process(payments)
        self.__repository.update_version(version)
        self.__repository.update_payments(payments)
        return

    def __versions_process(self, versions: List[DbTripItemVersion]):
        for version in versions:
            version.JsonData = self.__voucher_process(version.JsonData)

        return

    def __payments_process(self, payments: List[DbPaymentInvoice]):
        for payment in payments:
            payment.Amount -= self.__settings.amountCommission
            payment.OperationInfo = self.__operation_info_process(payment.OperationInfo)

        return

    def __voucher_process(self, json_data):
        voucher = Voucher(json_data)
        voucher.PriceDetails = PriceDetails(json.dumps(voucher.PriceDetails))

        if voucher.PriceDetails.Fee > 0:
            voucher.PriceDetails.Fee -= self.__settings.fee
            voucher.PriceDetails.Commission -= self.__settings.commission
        elif voucher.PriceDetails.Commission < 0:
            voucher.PriceDetails.Fee += self.__settings.fee
            voucher.PriceDetails.Commission += self.__settings.commission

        voucher.PriceDetails = voucher.PriceDetails.__dict__
        return json.dumps(voucher.__dict__, ensure_ascii=False)

    def __operation_info_process(self, operation_info):
        info = OperationInfo(operation_info)
        info.Details = list(map(lambda x: Details(json.dumps(x)), info.Details))

        info.Details = self.__select_not_commission(info.Details)

        info.Details = list(map(lambda x: x.__dict__, info.Details))
        return json.dumps(info.__dict__, ensure_ascii=False)

    @staticmethod
    def __select_not_commission(details: List[Details]):
        new_detail = []

        for detail in details:
            if "сбор за выписку" not in detail.Name:
                new_detail.append(detail)

        return new_detail
