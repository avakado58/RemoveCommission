from src.RemoveCommission.configs import ConfigReader
from src.RemoveCommission.repository import Repository
from src.RemoveCommission.services import CommissionService
from src.RemoveCommission.sql import PureSql


def run():
    settings = ConfigReader.read()
    print(settings.connectionStringSQLAlchemy)
    pure_sql = PureSql(settings.connectionStringPyodbc)
    repository = Repository(settings)
    commission_service = CommissionService(repository, pure_sql, settings)
    commission_service.remove_ticket_commission([71536827273854], settings.companyId)


if __name__ == '__main__':
    run()
