from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, Numeric


class DbOperationDetails(BaseModel):
    __tablename__ = "DbOperationDetails"

    Id = Column(Integer, primary_key=True, index=True)
    Amount = Column(Numeric)
    Description = Column(String)
    Type = Column(Integer)
    OperationId = Column(Integer)
    TripItemVersionId = Column(Integer)
