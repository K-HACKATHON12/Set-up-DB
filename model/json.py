import os
import glob
import json

class GetJsonData:
    def __init__(self):
        json_files = glob.glob('./json/seoul/*.json')
        self.all_json_files = [os.path.basename(file) for file in json_files]

    def table_name_parser(self, tablename):
        if tablename == 'commercial_change_indicator':
            return '상권변화지표'
        if tablename == 'commercial_expenditure':
            return '소득소비'
        if tablename == 'commercial_sales_info':
            return '추정매출'
        if tablename == 'commercial_facility_info':
            return '집객시설'
        if tablename == 'commercial_business_info':
            return '점포'
        if tablename == 'loc_apartment_info':
            return '아파트'
        if tablename == 'loc_administrative_district':
            return '영역'
        if tablename == 'population_street':
            return '길단위인구'
        if tablename == 'population_resident':
            return '상주인구'
        if tablename == 'population_workplace':
            return '직장인구'

    def search_json_file(self, name):
        return [file for file in self.all_json_files if name in file][0]

    def parse_json_file(self, json_file_name):
        with open(f'./json/seoul/{json_file_name}', 'r', encoding='utf-8') as file:
            return json.load(file)


