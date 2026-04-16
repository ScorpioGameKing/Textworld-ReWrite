from pathlib import Path
from textworld.data._database import Database

class DataManager():

    _databases: dict

    def __init__(self):
        self._databases = {}
    
    def database_intialization(self, *databases):
        for db in databases:
            self.create_missing_directory_tree(db[0])
            self._databases.update({db[1]:Database(db[1], db[0])})

    def add_database_to_manager(self, database):
        self._databases.update({database[1]: Database(database[1], database[0])})
    
    def fetch_database(self, database_name):
        return self._databases[database_name]

    def create_missing_directory_tree(self, location):
        Path(location).mkdir(parents=True, exist_ok=True)