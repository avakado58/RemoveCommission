from typing import List
from src.RemoveCommission.configs import Settings
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

        payments = self.__repository.get_payment(operation_ids)
        version = self.__repository.get_versions(ids)
        self.__versions_process(version)
        self.__payments_process(payments)
        self.__repository.update_version(version)
        self.__repository.update_payments(payments)
        return

    def __versions_process(self, versions: List[DbTripItemVersion]):
        return

    def __payments_process(self, payments: List[DbPaymentInvoice]):
        return

    def __voucher_process(self, voucher):
        return

    def __operation_info_process(self, operation_info):
        return
