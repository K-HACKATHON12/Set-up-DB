from sqlalchemy import Table, Column, Integer, String, BigInteger, Float

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


# 상권 소득 소비 데이터 모델
class CommercialExpenditureModel:
    def __init__(self, metadata):
        self.expenditure = Table(
            'commercial_expenditure', metadata,

            # 상권 관련 정보
            Column('TRDAR_CD', String, nullable=False, comment="상권_코드"),
            Column('TRDAR_CD_NM', String, nullable=False, comment="상권_코드_명"),
            Column('TRDAR_SE_CD', String, nullable=False, comment="상권_구분_코드"),
            Column('TRDAR_SE_CD_NM', String, nullable=False, comment="상권_구분_코드_명"),
            Column('STDR_YYQU_CD', String, nullable=False, comment="기준_년분기_코드"),

            # 지출 항목별 총 금액
            Column('LSR_EXPNDTR_TOTAMT', BigInteger, nullable=False, comment="여가_지출_총금액"),
            Column('MCP_EXPNDTR_TOTAMT', BigInteger, nullable=False, comment="의료비_지출_총금액"),
            Column('PLESR_EXPNDTR_TOTAMT', BigInteger, nullable=False, comment="유흥_지출_총금액"),
            Column('EDC_EXPNDTR_TOTAMT', BigInteger, nullable=False, comment="교육_지출_총금액"),
            Column('CLTUR_EXPNDTR_TOTAMT', BigInteger, nullable=False, comment="문화_지출_총금액"),
            Column('EXPNDTR_TOTAMT', BigInteger, nullable=False, comment="지출_총금액"),
            Column('FDSTFFS_EXPNDTR_TOTAMT', BigInteger, nullable=False, comment="식료품_지출_총금액"),
            Column('CLTHS_FTWR_EXPNDTR_TOTAMT', BigInteger, nullable=False, comment="의류_신발_지출_총금액"),
            Column('LVSPL_EXPNDTR_TOTAMT', BigInteger, nullable=False, comment="생활용품_지출_총금액"),
            Column('TRNSPORT_EXPNDTR_TOTAMT', BigInteger, nullable=False, comment="교통_지출_총금액"),

            # 소득 관련 정보
            Column('INCOME_SCTN_CD', String, nullable=False, comment="소득_구간_코드"),
            Column('MT_AVRG_INCOME_AMT', BigInteger, nullable=False, comment="월_평균_소득_금액"),
        )

# 상권 추정 매출 데이터 모델
class CommercialSalesInfoModel:
    def __init__(self, metadata):
        self.sales_info = Table(
            'commercial_sales_info', metadata,

            # 상권 관련 정보
            Column('TRDAR_CD', String, nullable=False, comment="상권_코드"),
            Column('TRDAR_CD_NM', String, nullable=False, comment="상권_코드_명"),
            Column('TRDAR_SE_CD', String, nullable=False, comment="상권_구분_코드"),
            Column('TRDAR_SE_CD_NM', String, nullable=False, comment="상권_구분_코드_명"),
            Column('STDR_YYQU_CD', String, nullable=False, comment="기준_년분기_코드"),

            # 연령대별 매출 금액 및 건수
            Column('AGRDE_10_SELNG_AMT', BigInteger, nullable=False, default=0, comment="연령대_10_매출_금액"),
            Column('AGRDE_10_SELNG_CO', Integer, nullable=False, default=0, comment="연령대_10_매출_건수"),
            Column('AGRDE_20_SELNG_AMT', BigInteger, nullable=False, default=0, comment="연령대_20_매출_금액"),
            Column('AGRDE_20_SELNG_CO', Integer, nullable=False, default=0, comment="연령대_20_매출_건수"),
            Column('AGRDE_30_SELNG_AMT', BigInteger, nullable=False, default=0, comment="연령대_30_매출_금액"),
            Column('AGRDE_30_SELNG_CO', Integer, nullable=False, default=0, comment="연령대_30_매출_건수"),
            Column('AGRDE_40_SELNG_AMT', BigInteger, nullable=False, default=0, comment="연령대_40_매출_금액"),
            Column('AGRDE_40_SELNG_CO', Integer, nullable=False, default=0, comment="연령대_40_매출_건수"),
            Column('AGRDE_50_SELNG_AMT', BigInteger, nullable=False, default=0, comment="연령대_50_매출_금액"),
            Column('AGRDE_50_SELNG_CO', Integer, nullable=False, default=0, comment="연령대_50_매출_건수"),
            Column('AGRDE_60_ABOVE_SELNG_AMT', BigInteger, nullable=False, default=0, comment="연령대_60_이상_매출_금액"),
            Column('AGRDE_60_ABOVE_SELNG_CO', Integer, nullable=False, default=0, comment="연령대_60_이상_매출_건수"),

            # 시간대별 매출 금액 및 건수
            Column('TMZON_00_06_SELNG_AMT', BigInteger, nullable=False, default=0, comment="시간대_00~06_매출_금액"),
            Column('TMZON_00_06_SELNG_CO', Integer, nullable=False, default=0, comment="시간대_00~06_매출_건수"),
            Column('TMZON_06_11_SELNG_AMT', BigInteger, nullable=False, default=0, comment="시간대_06~11_매출_금액"),
            Column('TMZON_06_11_SELNG_CO', Integer, nullable=False, default=0, comment="시간대_06~11_매출_건수"),
            Column('TMZON_11_14_SELNG_AMT', BigInteger, nullable=False, default=0, comment="시간대_11~14_매출_금액"),
            Column('TMZON_11_14_SELNG_CO', Integer, nullable=False, default=0, comment="시간대_11~14_매출_건수"),
            Column('TMZON_14_17_SELNG_AMT', BigInteger, nullable=False, default=0, comment="시간대_14~17_매출_금액"),
            Column('TMZON_14_17_SELNG_CO', Integer, nullable=False, default=0, comment="시간대_14~17_매출_건수"),
            Column('TMZON_17_21_SELNG_AMT', BigInteger, nullable=False, default=0, comment="시간대_17~21_매출_금액"),
            Column('TMZON_17_21_SELNG_CO', Integer, nullable=False, default=0, comment="시간대_17~21_매출_건수"),
            Column('TMZON_21_24_SELNG_AMT', BigInteger, nullable=False, default=0, comment="시간대_21~24_매출_금액"),
            Column('TMZON_21_24_SELNG_CO', Integer, nullable=False, default=0, comment="시간대_21~24_매출_건수"),

            # 요일별 매출 금액 및 건수
            Column('MON_SELNG_AMT', BigInteger, nullable=False, default=0, comment="월요일_매출_금액"),
            Column('MON_SELNG_CO', Integer, nullable=False, default=0, comment="월요일_매출_건수"),
            Column('TUES_SELNG_AMT', BigInteger, nullable=False, default=0, comment="화요일_매출_금액"),
            Column('TUES_SELNG_CO', Integer, nullable=False, default=0, comment="화요일_매출_건수"),
            Column('WED_SELNG_AMT', BigInteger, nullable=False, default=0, comment="수요일_매출_금액"),
            Column('WED_SELNG_CO', Integer, nullable=False, default=0, comment="수요일_매출_건수"),
            Column('THUR_SELNG_AMT', BigInteger, nullable=False, default=0, comment="목요일_매출_금액"),
            Column('THUR_SELNG_CO', Integer, nullable=False, default=0, comment="목요일_매출_건수"),
            Column('FRI_SELNG_AMT', BigInteger, nullable=False, default=0, comment="금요일_매출_금액"),
            Column('FRI_SELNG_CO', Integer, nullable=False, default=0, comment="금요일_매출_건수"),
            Column('SAT_SELNG_AMT', BigInteger, nullable=False, default=0, comment="토요일_매출_금액"),
            Column('SAT_SELNG_CO', Integer, nullable=False, default=0, comment="토요일_매출_건수"),
            Column('SUN_SELNG_AMT', BigInteger, nullable=False, default=0, comment="일요일_매출_금액"),
            Column('SUN_SELNG_CO', Integer, nullable=False, default=0, comment="일요일_매출_건수"),

            # 성별 매출 금액 및 건수
            Column('ML_SELNG_AMT', BigInteger, nullable=False, default=0, comment="남성_매출_금액"),
            Column('ML_SELNG_CO', Integer, nullable=False, default=0, comment="남성_매출_건수"),
            Column('FML_SELNG_AMT', BigInteger, nullable=False, default=0, comment="여성_매출_금액"),
            Column('FML_SELNG_CO', Integer, nullable=False, default=0, comment="여성_매출_건수"),

            # 주중 및 주말 매출 금액 및 건수
            Column('MDWK_SELNG_AMT', BigInteger, nullable=False, default=0, comment="주중_매출_금액"),
            Column('MDWK_SELNG_CO', Integer, nullable=False, default=0, comment="주중_매출_건수"),
            Column('WKEND_SELNG_AMT', BigInteger, nullable=False, default=0, comment="주말_매출_금액"),
            Column('WKEND_SELNG_CO', Integer, nullable=False, default=0, comment="주말_매출_건수"),

            # 당월 매출 금액 및 건수
            Column('THSMON_SELNG_AMT', BigInteger, nullable=False, default=0, comment="당월_매출_금액"),
            Column('THSMON_SELNG_CO', Integer, nullable=False, default=0, comment="당월_매출_건수"),

            # 서비스 업종 관련 정보
            Column('SVC_INDUTY_CD', String, nullable=False, comment="서비스_업종_코드"),
            Column('SVC_INDUTY_CD_NM', String, nullable=False, comment="서비스_업종_코드_명"),
        )

class CommercialBusinessInfoModel:
    def __init__(self, metadata):
        self.business_info = Table(
            'commercial_business_info', metadata,

            # 상권 관련 정보
            Column('TRDAR_CD', String, nullable=False, comment="상권_코드"),
            Column('TRDAR_CD_NM', String, nullable=False, comment="상권_코드_명"),
            Column('TRDAR_SE_CD', String, nullable=False, comment="상권_구분_코드"),
            Column('TRDAR_SE_CD_NM', String, nullable=False, comment="상권_구분_코드_명"),
            Column('STDR_YYQU_CD', String, nullable=False, comment="기준_년분기_코드"),

            # 점포 관련 정보
            Column('STOR_CO', Integer, nullable=False, comment="점포_수"),
            Column('OPBIZ_STOR_CO', Integer, nullable=False, comment="개업_점포_수"),
            Column('CLSBIZ_STOR_CO', Integer, nullable=False, comment="폐업_점포_수"),
            Column('FRC_STOR_CO', Integer, nullable=False, comment="프랜차이즈_점포_수"),
            Column('SIMILR_INDUTY_STOR_CO', Integer, nullable=False, comment="유사_업종_점포_수"),

            # 서비스 업종 관련 정보
            Column('SVC_INDUTY_CD', String, nullable=False, comment="서비스_업종_코드"),
            Column('SVC_INDUTY_CD_NM', String, nullable=False, comment="서비스_업종_코드_명"),

            # 비율 관련 정보
            Column('OPBIZ_RT', Float, nullable=False, comment="개업_율"),
            Column('CLSBIZ_RT', Float, nullable=False, comment="폐업_률"),
        )


# 집객시설
class CommercialFacilityInfoModel:
    def __init__(self, metadata):
        self.facility_info = Table(
            'commercial_facility_info', metadata,

            # 상권 관련 정보
            Column('TRDAR_CD', String, nullable=False, comment="상권_코드"),
            Column('TRDAR_CD_NM', String, nullable=False, comment="상권_코드_명"),
            Column('TRDAR_SE_CD', String, nullable=False, comment="상권_구분_코드"),
            Column('TRDAR_SE_CD_NM', String, nullable=False, comment="상권_구분_코드_명"),
            Column('STDR_YYQU_CD', String, nullable=False, comment="기준_년분기_코드"),


            # 시설 관련 정보
            Column('KNDRGR_CO', Integer, nullable=False, default=0, comment="유치원_수"),
            Column('BUS_STTN_CO', Integer, nullable=False, default=0, comment="버스_정거장_수"),
            Column('RLROAD_STATN_CO', Integer, nullable=False, default=0, comment="철도_역_수"),
            Column('DRTS_CO', Integer, nullable=False, default=0, comment="백화점_수"),
            Column('SUPMK_CO', Integer, nullable=False, default=0, comment="슈퍼마켓_수"),
            Column('HGSCHL_CO', Integer, nullable=False, default=0, comment="고등학교_수"),
            Column('UNIV_CO', Integer, nullable=False, default=0, comment="대학교_수"),
            Column('GEHSPT_CO', Integer, nullable=False, default=0, comment="종합병원_수"),
            Column('ELESCH_CO', Integer, nullable=False, default=0, comment="초등학교_수"),
            Column('PBLOFC_CO', Integer, nullable=False, default=0, comment="관공서_수"),
            Column('BANK_CO', Integer, nullable=False, default=0, comment="은행_수"),
            Column('THEAT_CO', Integer, nullable=False, default=0, comment="극장_수"),
            Column('ARPRT_CO', Integer, nullable=False, default=0, comment="공항_수"),
            Column('BUS_TRMINL_CO', Integer, nullable=False, default=0, comment="버스_터미널_수"),
            Column('VIATR_FCLTY_CO', Integer, nullable=False, default=0, comment="집객시설_수"),
            Column('STAYNG_FCLTY_CO', Integer, nullable=False, default=0, comment="숙박_시설_수"),
            Column('MSKUL_CO', Integer, nullable=False, default=0, comment="중학교_수"),
            Column('PARMACY_CO', Integer, nullable=False, default=0, comment="약국_수"),
            Column('GNRL_HSPTL_CO', Integer, nullable=False, default=0, comment="일반_병원_수"),
            Column('SUBWAY_STATN_CO', Integer, nullable=False, default=0, comment="지하철_역_수"),
        )