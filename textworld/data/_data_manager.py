from pathlib import Path
from textworld.data._database import Database

class DataManager():

    _databases: dict

    def __init__(self):
        self._databases = {}
    
    def database_intialization(self, *databases):
        for db in databases:
            #print(db[0])
            self.create_missing_directory_tree(db[0])
            self._databases.update({db[1]:Database(db[1], db[0])})
    
    def fetch_database(self, database_name):
        return self._databases[database_name]

    def create_missing_directory_tree(self, location):
        Path(location).mkdir(parents=True, exist_ok=True)