from model.json import GetJsonData
from sqlalchemy.sql import insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

class Model(GetJsonData):
    def __init__(self, table):
        super().__init__()
        self.table = table

    def get_table_name(self):
        return self.table.name

    def create_table(self, metadata, engine):
        metadata.create_all(engine)

    def delete_all_table(self, engine):
        # 세션 생성
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            # 테이블 이름 가져오기
            table_name = self.get_table_name()
            # 원시 SQL 쿼리 실행하여 테이블 삭제
            session.execute(text(f"DROP TABLE IF EXISTS {table_name}"))
            # 변경 사항 커밋
            session.commit()
        except Exception as e:
            # 오류 발생 시 롤백
            session.rollback()
            print(f"Error occurred: {e}")
        finally:
            # 세션 종료
            session.close()

    def create_data_all(self, metadata, engine):
        # 테이블 이름과 JSON 파일 이름 얻기
        table_name = self.get_table_name()
        table_name_parsed = self.table_name_parser(table_name)
        json_file_name = self.search_json_file(table_name_parsed)
        data_from_json = self.parse_json_file(json_file_name)

        check = 0

        # 메타데이터 반영 및 세션 생성
        metadata.reflect(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            # 테이블 객체 가져오기
            table = metadata.tables[table_name]

            # 테이블 컬럼 이름 가져오기
            table_columns = set(table.columns.keys())

            # 데이터 삽입
            for data in data_from_json['DATA']:
                cleaned_data = {}
                for key, value in data.items():
                    # 소문자 키를 대문자로 변환하여 테이블에 존재하는 컬럼만 삽입
                    upper_key = key.upper()
                    if upper_key in table_columns:
                        cleaned_data[upper_key] = 0 if value is None else value

                if cleaned_data:
                    stmt = insert(table).values(cleaned_data)
                    check += 1
                    if check % 10000 == 0:
                        print(f"{check}개 삽입")
                    session.execute(stmt)

            # 커밋
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            # 세션 닫기
            session.close()



