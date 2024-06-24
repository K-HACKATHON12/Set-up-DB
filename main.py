from urllib.parse import quote
from sqlalchemy import create_engine, text, MetaData
from dotenv import dotenv_values
from model.seoul_commercial_model import CommercialChangeIndicatorModel, CommercialExpenditureModel, CommercialSalesInfoModel, CommercialBusinessInfoModel, CommercialFacilityInfoModel
from model.seoul_locatation_model import LocAdministrativeDistrictModel, LocApartmentInfoModel
from model.seoul_population_model import PopulationResidentModel, PopulationStreetModel, PopulationWorkplaceModel

# take environment variables from .env
config = dotenv_values("DB.env")

# URL 인코딩을 통해 특수 문자 처리
username = config['USERNAME']
password = quote(config['PASSWORD'])  # 비밀번호 인코딩
host = config['HOST']
port = config['PORT']
database = config['DATABASE']

# 연결 문자열 생성
connection_string = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"

# SQLAlchemy 엔진 생성
engine = create_engine(connection_string)

# 메타데이터 객체 생성
metadata = MetaData()

# Table 생성
commercial_change_indicator_table = CommercialChangeIndicatorModel(metadata)
commercial_expanditure_table = CommercialExpenditureModel(metadata)
commercial_sales_info_table = CommercialSalesInfoModel(metadata)
commercial_bussiness_info_table = CommercialBusinessInfoModel(metadata)
loc_apartment_info_table = LocApartmentInfoModel(metadata)
loc_administrative_district_table = LocAdministrativeDistrictModel(metadata)
loc_facility_info_table = CommercialFacilityInfoModel(metadata)
population_street_table = PopulationStreetModel(metadata)
population_resident_table = PopulationResidentModel(metadata)
population_workplace_table = PopulationWorkplaceModel(metadata)
metadata.create_all(engine)


# 각 테이블에 데이터 생성