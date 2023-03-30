from typing import List
from database.repository import Repository
from database.sql import PureSql
from models.db_trip_item_version import DbTripItemVersion


class CommissionService:
    def __init__(self, repository: Repository, pure_sql: PureSql):
        self.__pure_sql = pure_sql
        self.__repository = repository

    def remove_ticket_commission(self, ticket_number: List[int], company_id: int):
        ids = self.__pure_sql.get_version_id(ticket_number, company_id)
        version = self.__repository.get_versions(ids)
        self.__repository.update_version(version)
        return

    def __remove_voucher_commission(self, version: DbTripItemVersion):
        return

