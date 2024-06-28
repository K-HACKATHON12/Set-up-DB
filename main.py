from urllib.parse import quote
from sqlalchemy import create_engine, MetaData
from dotenv import dotenv_values
from model.tables.seoul_commercial_model import *
from model.tables.seoul_locatation_model import *
from model.tables.seoul_population_model import *
from model.model import Model

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

models = [
    Model(commercial_change_indicator),
    Model(commercial_expenditure),
    Model(commercial_business_info),
    Model(commercial_sales_info),
    Model(commercial_facility_info),

    Model(loc_apartment_info),
    Model(loc_administrative_district),

    Model(population_street),
    Model(population_resident),
    Model(population_workplace)
]

print("데이터 초기화 시작")

for model in models:
    model.delete_all_table(engine)

print("데이터 초기화 완료")

print("테이블 생성 시작")

from metadata import metadata
for model in models:
    model.create_table(metadata, engine)

print("테이블 생성 완료")

print("데이터 삽입 시작, 주의: 1시간 이상 소요될 수 있습니다.")
from metadata import metadata

for model in models:
    model.create_data_all(metadata, engine)

print("데이터 삽입 완료")
