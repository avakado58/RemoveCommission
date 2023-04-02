from src.RemoveCommission.configs import ConfigReader
from src.RemoveCommission.repository import Repository
from src.RemoveCommission.services import CommissionService
from src.RemoveCommission.sql import PureSql
import unicodedata2 as unc


def get_tickets():
    with open("./tickets.cvs", encoding="utf-8") as file:
        return list(map(lambda x: int(x), ("".join(ch for ch in file.read() if unc.category(ch)[0] != "C")).split(",")))
    return


def run():
    settings = ConfigReader.read()
    tickets = get_tickets()
    print(settings.connectionStringSQLAlchemy)
    pure_sql = PureSql(settings.connectionStringPyodbc)
    repository = Repository(settings)
    commission_service = CommissionService(repository, pure_sql, settings)
    commission_service.remove_ticket_commission(tickets)


if __name__ == '__main__':
    run()
