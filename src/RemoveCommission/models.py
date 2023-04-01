from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Numeric, DateTime, Boolean


class BaseModel(DeclarativeBase):
    pass


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


class DbOperationDetails(BaseModel):
    __tablename__ = "DbOperationDetails"

    Id = Column(Integer, primary_key=True, index=True)
    Amount = Column(Numeric)
    Description = Column(String)
    Type = Column(Integer)
    OperationId = Column(Integer)
    TripItemVersionId = Column(Integer)


class DbOperationDetailsPrices(BaseModel):
    __tablename__ = "DbOperationDetailsPrices"

    OperationDetailsId = Column(Integer, primary_key=True)
    Base = Column(Numeric)
    Tax = Column(Numeric)
    Fee = Column(Numeric)
    VAT = Column(Numeric)
    Commission = Column(Numeric)
    HasVAT = Column(Boolean)
    Taxes = Column(Numeric)


class DbPaymentInvoice(BaseModel):
    __tablename__ = "DbPaymentInvoices"

    CompanyId = Column(Integer)
    CreatedDate = Column(DateTime)
    InvoiceNum = Column(String)
    OperationInfo = Column(String)
    Amount = Column(Numeric)
    TripId = Column(Integer)
    TripDate = Column(String)
    OperationId = Column(Integer, primary_key=True)
    SpendingFundType = Column(Integer)
