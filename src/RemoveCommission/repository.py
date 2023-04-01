from typing import List, Tuple
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.RemoveCommission.configs import Settings
from src.RemoveCommission.models import DbTripItemVersion, DbPaymentInvoice, \
    DbOperationDetails, DbOperationDetailsPrices


class Repository:
    def __init__(self, settings: Settings):
        self.__engine = create_engine(settings.connectionStringSQLAlchemy, echo=True)
        self.__settings = settings

    def get_versions(self, version_ids: List[int]) -> List[DbTripItemVersion]:
        with Session(autoflush=False, bind=self.__engine) as db:
            versions = db.query(DbTripItemVersion).filter(DbTripItemVersion.Id.in_(version_ids)).all()
            print(f"{len(versions)} версий по билетам")

        return versions

    def update_version(self, versions: List[DbTripItemVersion]) -> int:
        with Session(autoflush=False, bind=self.__engine) as db:
            ids = list(map(lambda x: x.Id, versions))
            db_versions = db.query(DbTripItemVersion).filter(DbTripItemVersion.Id.in_(ids)).all()

            i = 0
            while i < len(db_versions):
                new_json = next(v for v in versions if v.Id == db_versions[i].Id).JsonData
                setattr(db_versions[i], 'JsonData', new_json)
                i += 1

            db.commit()

            print(f"{i} версий обнавленно")

        return i

    def update_operation_details(self, version_ids: List[int]) -> Tuple[List[int], List[int]]:
        with Session(autoflush=False, bind=self.__engine) as db:
            operation_details = db.query(DbOperationDetails) \
                .filter(DbOperationDetails.TripItemVersionId.in_(version_ids)).all()
            detail_ids = []
            operation_ids = []

            i = 0
            while i < len(operation_details):
                amount = operation_details[i].Amount
                detail_ids.append(operation_details[i].Id)
                operation_ids.append(operation_details[i].OperationId)
                '''
                if amount < 0:
                    operation_details[i].Amount += self.__settings.amountCommission
                elif amount > 0:
                    operation_details[i].Amount -= self.__settings.amountCommission
                '''
                i += 1

            operation_ids = list(set(operation_ids))
            db.commit()
        return detail_ids, operation_ids

    def update_detail_price(self, detail_ids: List[int]):
        with Session(autoflush=False, bind=self.__engine) as db:
            details_prise = db.query(DbOperationDetailsPrices) \
                .filter(DbOperationDetailsPrices.OperationDetailsId.in_(detail_ids)).all()

            for price in details_prise:
                if price.Commission < 0:
                    price.Fee += self.__settings.fee
                    price.Commission += self.__settings.commission
                elif price.Commission > 0:
                    price.Fee -= self.__settings.fee
                    price.Commission -= self.__settings.commission

            db.commit()

    def get_payment(self, operation_id: List[int]):
        with Session(autoflush=False, bind=self.__engine) as db:
            payments = db.query(DbPaymentInvoice) \
                .filter(DbPaymentInvoice.OperationId.in_(operation_id)).all()

        print(f"{len(payments)} счетов по билетам")

        return payments

    def update_payments(self, payments: List[DbPaymentInvoice]):
        return
