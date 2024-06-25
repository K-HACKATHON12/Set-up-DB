from model.json import GetJsonData

class Model(GetJsonData):
    def __init__(self, table):
        super().__init__()
        self.table = table

    def get_table_name(self):
        return self.table.name

    def create_table(self, metadata, engine):
        metadata.create_all(engine)

    def delete_all_data(self, metadata, engine):
        pass

    def create_data_all(self):
        table_name = self.get_table_name()
        table_name_parsed = self.table_name_parser(table_name)
        json_file_name = self.search_json_file(table_name_parsed)
        data = self.parse_json_file(json_file_name)
        print(data)
