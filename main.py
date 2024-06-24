from urllib.parse import quote
from sqlalchemy import create_engine, text, MetaData
from dotenv import dotenv_values
from model.seoul import StreetPopulationModel

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
street_population = StreetPopulationModel(metadata)
metadata.create_all(engine)

# 각 테이블에 데이터 생성