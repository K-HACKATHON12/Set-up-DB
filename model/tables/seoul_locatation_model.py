from sqlalchemy import *
from metadata import metadata

# 아파트
loc_apartment_info = Table(
    'loc_apartment_info', metadata,

    # 상권 관련 정보
    Column('TRDAR_CD', String, nullable=False, comment="상권_코드"),
    Column('TRDAR_CD_NM', String, nullable=False, comment="상권_코드_명"),
    Column('TRDAR_SE_CD', String, nullable=False, comment="상권_구분_코드"),
    Column('TRDAR_SE_CD_NM', String, nullable=False, comment="상권_구분_코드_명"),
    Column('STDR_YYQU_CD', String, nullable=False, comment="기준_년분기_코드"),

    # 아파트 관련 정보
    Column('APT_HSMP_CO', Integer, nullable=False, comment="아파트_단지_수"),
    Column('AVRG_AE', Integer, nullable=False, comment="아파트_평균_면적"),
    Column('AVRG_MKTC', BigInteger, nullable=False, comment="아파트_평균_시가"),

    # 아파트 가격대별 세대 수
    Column('PC_1_HDMIL_BELO_HSHLD_CO', Integer, nullable=False, comment="아파트_가격_1_억_미만_세대_수"),
    Column('PC_1_HDMIL_HSHLD_CO', Integer, nullable=False, comment="아파트_가격_1_억_세대_수"),
    Column('PC_2_HDMIL_HSHLD_CO', Integer, nullable=False, comment="아파트_가격_2_억_세대_수"),
    Column('PC_3_HDMIL_HSHLD_CO', Integer, nullable=False, comment="아파트_가격_3_억_세대_수"),
    Column('PC_4_HDMIL_HSHLD_CO', Integer, nullable=False, comment="아파트_가격_4_억_세대_수"),
    Column('PC_5_HDMIL_HSHLD_CO', Integer, nullable=False, comment="아파트_가격_5_억_세대_수"),
    Column('PC_6_HDMIL_ABOVE_HSHLD_CO', Integer, nullable=False, comment="아파트_가격_6_억_이상_세대_수"),

    # 아파트 면적별 세대 수
    Column('AE_66_SQMT_BELO_HSHLD_CO', Integer, nullable=False, comment="아파트_면적_66_제곱미터_미만_세대_수"),
    Column('AE_66_SQMT_HSHLD_CO', Integer, nullable=False, comment="아파트_면적_66_제곱미터_세대_수"),
    Column('AE_99_SQMT_HSHLD_CO', Integer, nullable=False, comment="아파트_면적_99_제곱미터_세대_수"),
    Column('AE_132_SQMT_HSHLD_CO', Integer, nullable=False, comment="아파트_면적_132_제곱미터_세대_수"),
    Column('AE_165_SQMT_HSHLD_CO', Integer, nullable=False, comment="아파트_면적_165_제곱미터_세대_수"),
)

# 상권 영역
loc_administrative_district = Table(
    'loc_administrative_district', metadata,

    # 상권 관련 정보
    Column('TRDAR_CD', String, nullable=False, comment="상권_코드"),
    Column('TRDAR_CD_NM', String, nullable=False, comment="상권_코드_명"),
    Column('TRDAR_SE_CD', String, nullable=False, comment="상권_구분_코드"),
    Column('TRDAR_SE_CD_NM', String, nullable=False, comment="상권_구분_코드_명"),

    # 행정동 관련 정보
    Column('ADSTRD_CD', String, nullable=False, comment="행정동_코드"),
    Column('ADSTRD_CD_NM', String, nullable=False, comment="행정동_코드_명"),

    # 자치구 관련 정보
    Column('SIGNGU_CD', String, nullable=False, comment="자치구_코드"),
    Column('SIGNGU_CD_NM', String, nullable=False, comment="자치구_코드_명"),

    # 좌표 값
    Column('XCNTS_VALUE', Integer, nullable=False, comment="엑스좌표_값"),
    Column('YDNTS_VALUE', Integer, nullable=False, comment="와이좌표_값"),

    Column('RELM_AR', Integer, nullable=False, comment="영역_면적"),
)