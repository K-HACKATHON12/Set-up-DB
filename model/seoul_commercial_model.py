from sqlalchemy import Table, Column, Integer, String, MetaData

# 상권 변화 지표 데이터 모델
class CommercialChangeIndicatorModel:
    def __init__(self, metadata):
        self.trade_area = Table(
            'commercial_change_indicator', metadata,

            # 상권 코드
            Column('TRDAR_CD', String, nullable=False, comment="상권_코드"),
            Column('TRDAR_CD_NM', String, nullable=False, comment="상권_코드_명"),

            # 기준 년분기 코드
            Column('STDR_YYQU_CD', String, nullable=False, comment="기준_년분기_코드"),

            # 상권 구분 코드
            Column('TRDAR_SE_CD', String, nullable=False, comment="상권_구분_코드"),
            Column('TRDAR_SE_CD_NM', String, nullable=False, comment="상권_구분_코드_명"),

            # 서울 운영 영업 개월 평균
            Column('SU_OPR_SALE_MT_AVRG', Integer, nullable=False, comment="서울_운영_영업_개월_평균"),

            # 운영 영업 개월 평균
            Column('OPR_SALE_MT_AVRG', Integer, nullable=False, comment="운영_영업_개월_평균"),

            # 상권 변화 지표
            Column('TRDAR_CHNGE_IX', String, nullable=False, comment="상권_변화_지표"),
            Column('TRDAR_CHNGE_IX_NM', String, nullable=False, comment="상권_변화_지표_명"),

            # 서울 폐업 영업 개월 평균
            Column('SU_CLS_SALE_MT_AVRG', Integer, nullable=False, comment="서울_폐업_영업_개월_평균"),

            # 폐업 영업 개월 평균
            Column('CLS_SALE_MT_AVRG', Integer, nullable=False, comment="폐업_영업_개월_평균"),
        )