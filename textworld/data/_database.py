import sqlite3

class Database():

    _database_connection: sqlite3.Connection = None
    _database_cursor: sqlite3.Cursor = None
    _database_location: str
    _database_name: str

    def __init__(self, database_name:str=None, location:str=None):
        if location == None: location = 'data/dummy_data/'
        if database_name == None: database_name = 'dummy.db'
        self._database_location = location
        self._database_name = database_name
        
    def connect(self):
        self._database_connection = sqlite3.connect(f"{self._database_location}{self._database_name}")
        self._database_cursor = self._database_connection.cursor()

    def intialize_database(self, *initalization_queries):
        for q in initalization_queries:
            self._database_cursor.execute(q, ())
            self._database_connection.commit()

    def __enter__(self):
        return self

    def __exit__(self, *misc):
        pass

    def __str__(self):
        return f"Database Object: {self._database_name} Located at: {self._database_location}"