class Model:
    def __init__(self, table):
        self.table = table

    def get_table_name(self):
        return self.table.name

    def create_table(self, metadata, engine):
        metadata.create_all(engine)

    def create_data_all(self):
        pass

    def all_auto(self):
        pass