from models.base_model import BaseModel
from sqlalchemy import  Column, Integer, String, DateTime


class DbTripItemVersion(BaseModel):
    __tablename__ = "DbTripItemVersions"

    Id = Column(Integer, primary_key=True, index=True)
    TripItemId = Column(Integer)
    ProviderName = Column(String)
    ServiceType = Column(String)
    Status = Column(Integer)
    CheckinDate = Column(DateTime)
    CheckoutDate = Column(DateTime)
    City = Column(String)
    Description = Column(String)
    EventDate = Column(DateTime)
    JsonData = Column(String)
    CompanyId = Column(Integer)
    ServiceSourceType = Column(String)
    ProjectId = Column(Integer)
    Reason = Column(String)
    CreatedBy = Column(String)
    DepartmentId = Column(Integer)
