from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.db_trip_item_version import DbTripItemVersion


class Repository:
    def __init__(self, connection_string: str):
        self.__engine = create_engine(connection_string, echo=True)

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
