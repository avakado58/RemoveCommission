from config.config_reader import ConfigReader
from database.repository import Repository
from commission_service import CommissionService
from database.sql import PureSql


def run():
    settings = ConfigReader.read()
    print(settings.connectionStringSQLAlchemy)
    pure_sql = PureSql(settings.connectionStringPyodbc)
    repository = Repository(settings.connectionStringSQLAlchemy)
    commission_service = CommissionService(repository, pure_sql)
    commission_service.remove_ticket_commission([71186818061714, 71236820630305], settings.companyId)


if __name__ == '__main__':
    run()
