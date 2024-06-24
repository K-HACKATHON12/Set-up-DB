from sqlalchemy import Table, Column, Integer, String, MetaData

# 길단위인구 데이터 모델
class PopulationStreetModel:
    def __init__(self, metadata):
        self.street_population = Table(
            'population_street', metadata,
            # 상권 코드
            Column('TRDAR_CD', String, nullable=False, comment="상권_코드"),
            Column('TRDAR_CD_NM', String, nullable=False, comment="상권_코드_명"),
            Column('TRDAR_SE_CD', String, nullable=False, comment="상권_구분_코드"),
            Column('TRDAR_SE_CD_NM', String, nullable=False, comment="상권_구분_코드_명"),
            Column('STDR_YYQU_CD', String, nullable=False, comment="기준_년분기_코드"),

            # 남성 유동인구 수
            Column('ML_FLPOP_CO', Integer, nullable=False, comment="남성_유동인구_수"),

            # 여성 유동인구 수
            Column('FML_FLPOP_CO', Integer, nullable=False, comment="여성_유동인구_수"),

            # 요일별 유동인구 수
            Column('SUN_FLPOP_CO', Integer, nullable=False, comment="일요일_유동인구_수"),
            Column('MON_FLPOP_CO', Integer, nullable=False, comment="월요일_유동인구_수"),
            Column('TUES_FLPOP_CO', Integer, nullable=False, comment="화요일_유동인구_수"),
            Column('WED_FLPOP_CO', Integer, nullable=False, comment="수요일_유동인구_수"),
            Column('THUR_FLPOP_CO', Integer, nullable=False, comment="목요일_유동인구_수"),
            Column('FRI_FLPOP_CO', Integer, nullable=False, comment="금요일_유동인구_수"),
            Column('SAT_FLPOP_CO', Integer, nullable=False, comment="토요일_유동인구_수"),

            # 연령별 유동인구 수
            Column('AGRDE_10_FLPOP_CO', Integer, nullable=False, comment="연령대_10_유동인구_수"),
            Column('AGRDE_20_FLPOP_CO', Integer, nullable=False, comment="연령대_20_유동인구_수"),
            Column('AGRDE_30_FLPOP_CO', Integer, nullable=False, comment="연령대_30_유동인구_수"),
            Column('AGRDE_40_FLPOP_CO', Integer, nullable=False, comment="연령대_40_유동인구_수"),
            Column('AGRDE_50_FLPOP_CO', Integer, nullable=False, comment="연령대_50_유동인구_수"),
            Column('AGRDE_60_ABOVE_FLPOP_CO', Integer, nullable=False, comment="연령대_60_이상_유동인구_수"),

            # 시간대
            Column('TOT_FLPOP_CO', Integer, nullable=False, comment="총_유동인구_수"),
            Column('TMZON_00_06_FLPOP_CO', Integer, nullable=False, comment="시간대_00_06_유동인구_수"),
            Column('TMZON_06_11_FLPOP_CO', Integer, nullable=False, comment="시간대_06_11_유동인구_수"),
            Column('TMZON_11_14_FLPOP_CO', Integer, nullable=False, comment="시간대_11_14_유동인구_수"),
            Column('TMZON_14_17_FLPOP_CO', Integer, nullable=False, comment="시간대_14_17_유동인구_수"),
            Column('TMZON_17_21_FLPOP_CO', Integer, nullable=False, comment="시간대_17_21_유동인구_수"),
            Column('TMZON_21_24_FLPOP_CO', Integer, nullable=False, comment="시간대_21_24_유동인구_수"),
        )

# 상주인구
class PopulationResidentModel:
    def __init__(self, metadata):
        self.resident_population = Table(
            'population_resident', metadata,

            # 상권 코드
            Column('TRDAR_CD', String, nullable=False, comment="상권_코드"),
            Column('TRDAR_CD_NM', String, nullable=False, comment="상권_코드_명"),
            Column('TRDAR_SE_CD', String, nullable=False, comment="상권_구분_코드"),
            Column('TRDAR_SE_CD_NM', String, nullable=False, comment="상권_구분_코드_명"),
            Column('STDR_YYQU_CD', String, nullable=False, comment="기준_년분기_코드"),

            Column('TOT_REPOP_CO', Integer, nullable=False, comment="총_상주인구_수"),
            # 남성 연령대별 상주인구 수
            Column('MAG_10_REPOP_CO', Integer, nullable=False, comment="남성연령대_10_상주인구_수"),
            Column('MAG_20_REPOP_CO', Integer, nullable=False, comment="남성연령대_20_상주인구_수"),
            Column('MAG_30_REPOP_CO', Integer, nullable=False, comment="남성연령대_30_상주인구_수"),
            Column('MAG_40_REPOP_CO', Integer, nullable=False, comment="남성연령대_40_상주인구_수"),
            Column('MAG_50_REPOP_CO', Integer, nullable=False, comment="남성연령대_50_상주인구_수"),
            Column('MAG_60_ABOVE_REPOP_CO', Integer, nullable=False, comment="남성연령대_60_이상_상주인구_수"),

            # 여성 연령대별 상주인구 수
            Column('FAG_10_REPOP_CO', Integer, nullable=False, comment="여성연령대_10_상주인구_수"),
            Column('FAG_20_REPOP_CO', Integer, nullable=False, comment="여성연령대_20_상주인구_수"),
            Column('FAG_30_REPOP_CO', Integer, nullable=False, comment="여성연령대_30_상주인구_수"),
            Column('FAG_40_REPOP_CO', Integer, nullable=False, comment="여성연령대_40_상주인구_수"),
            Column('FAG_50_REPOP_CO', Integer, nullable=False, comment="여성연령대_50_상주인구_수"),
            Column('FAG_60_ABOVE_REPOP_CO', Integer, nullable=False, comment="여성연령대_60_이상_상주인구_수"),

            # 연령대별 상주인구 수
            Column('AGRDE_10_REPOP_CO', Integer, nullable=False, comment="연령대_10_상주인구_수"),
            Column('AGRDE_20_REPOP_CO', Integer, nullable=False, comment="연령대_20_상주인구_수"),
            Column('AGRDE_30_REPOP_CO', Integer, nullable=False, comment="연령대_30_상주인구_수"),
            Column('AGRDE_40_REPOP_CO', Integer, nullable=False, comment="연령대_40_상주인구_수"),
            Column('AGRDE_50_REPOP_CO', Integer, nullable=False, comment="연령대_50_상주인구_수"),
            Column('AGRDE_60_ABOVE_REPOP_CO', Integer, nullable=False, comment="연령대_60_이상_상주인구_수"),

            # 성별 상주인구 수
            Column('ML_REPOP_CO', Integer, nullable=False, comment="남성_상주인구_수"),
            Column('FML_REPOP_CO', Integer, nullable=False, comment="여성_상주인구_수"),

            # 가구수
            Column('APT_HSHLD_CO', Integer, nullable=False, comment="아파트_가구_수"),
            Column('NON_APT_HSHLD_CO', Integer, nullable=False, comment="비_아파트_가구_수"),
            Column('TOT_HSHLD_CO', Integer, nullable=False, comment="총_가구_수"),
        )

# 직장 인구
class PopulationWorkplaceModel:
    def __init__(self, metadata):
        self.workplace_population = Table(
            'population_workplace', metadata,

            # 상권 관련 정보
            Column('TRDAR_CD', String, nullable=False, comment="상권_코드"),
            Column('TRDAR_CD_NM', String, nullable=False, comment="상권_코드_명"),
            Column('TRDAR_SE_CD', String, nullable=False, comment="상권_구분_코드"),
            Column('TRDAR_SE_CD_NM', String, nullable=False, comment="상권_구분_코드_명"),
            Column('STDR_YYQU_CD', String, nullable=False, comment="기준_년분기_코드"),

            Column('TOT_WRC_POPLTN_CO', Integer, nullable=False, comment="총_직장_인구_수"),

            # 남성 연령대별 직장 인구 수
            Column('MAG_10_WRC_POPLTN_CO', Integer, nullable=False, comment="남성연령대_10_직장_인구_수"),
            Column('MAG_20_WRC_POPLTN_CO', Integer, nullable=False, comment="남성연령대_20_직장_인구_수"),
            Column('MAG_30_WRC_POPLTN_CO', Integer, nullable=False, comment="남성연령대_30_직장_인구_수"),
            Column('MAG_40_WRC_POPLTN_CO', Integer, nullable=False, comment="남성연령대_40_직장_인구_수"),
            Column('MAG_50_WRC_POPLTN_CO', Integer, nullable=False, comment="남성연령대_50_직장_인구_수"),
            Column('MAG_60_ABOVE_WRC_POPLTN_CO', Integer, nullable=False, comment="남성연령대_60_이상_직장_인구_수"),

            # 여성 연령대별 직장 인구 수
            Column('FAG_10_WRC_POPLTN_CO', Integer, nullable=False, comment="여성연령대_10_직장_인구_수"),
            Column('FAG_20_WRC_POPLTN_CO', Integer, nullable=False, comment="여성연령대_20_직장_인구_수"),
            Column('FAG_30_WRC_POPLTN_CO', Integer, nullable=False, comment="여성연령대_30_직장_인구_수"),
            Column('FAG_40_WRC_POPLTN_CO', Integer, nullable=False, comment="여성연령대_40_직장_인구_수"),
            Column('FAG_50_WRC_POPLTN_CO', Integer, nullable=False, comment="여성연령대_50_직장_인구_수"),
            Column('FAG_60_ABOVE_WRC_POPLTN_CO', Integer, nullable=False, comment="여성연령대_60_이상_직장_인구_수"),

            # 연령대별 직장 인구 수
            Column('AGRDE_10_WRC_POPLTN_CO', Integer, nullable=False, comment="연령대_10_직장_인구_수"),
            Column('AGRDE_20_WRC_POPLTN_CO', Integer, nullable=False, comment="연령대_20_직장_인구_수"),
            Column('AGRDE_30_WRC_POPLTN_CO', Integer, nullable=False, comment="연령대_30_직장_인구_수"),
            Column('AGRDE_40_WRC_POPLTN_CO', Integer, nullable=False, comment="연령대_40_직장_인구_수"),
            Column('AGRDE_50_WRC_POPLTN_CO', Integer, nullable=False, comment="연령대_50_직장_인구_수"),
            Column('AGRDE_60_ABOVE_WRC_POPLTN_CO', Integer, nullable=False, comment="연령대_60_이상_직장_인구_수"),

            # 성별 직장 인구 수
            Column('ML_WRC_POPLTN_CO', Integer, nullable=False, comment="남성_직장_인구_수"),
            Column('FML_WRC_POPLTN_CO', Integer, nullable=False, comment="여성_직장_인구_수"),
        )