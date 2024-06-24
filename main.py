from urllib.parse import quote
from sqlalchemy import create_engine, text
from dotenv import dotenv_values

# take environment variables from .env
config = dotenv_values(".env")

# URL 인코딩을 통해 특수 문자 처리
username = config['USERNAME']
password = quote(config['PASSWORD'])  # 비밀번호 인코딩
host = config['HOST']
port = config['PORT']
database = config['DATABASE']

# 연결 문자열 생성
connection_string = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
print("Connection String:", connection_string)

# SQLAlchemy 엔진 생성
engine = create_engine(connection_string)

try:
    # 데이터베이스 연결 시도
    with engine.connect() as connection:
        # 간단한 쿼리 실행
        result = connection.execute(text("SELECT 1"))
        for row in result:
            print("DB 연결 성공:", row)
except Exception as e:
    print("DB 연결 실패:", e)