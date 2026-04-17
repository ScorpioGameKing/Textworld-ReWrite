import sqlite3
from textworld.models import Tile

class Database():

    """
    An interfacing class for working with sqlite databases.
    """

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
        """
        Use this to establish a connection to the Database
        """
        self._database_connection = sqlite3.connect(f"{self._database_location}{self._database_name}")
        self._database_cursor = self._database_connection.cursor()

    def intialize_database(self, *initalization_queries):
        """
        Use this to supply a Database with the intialization and additonal
        queries as needed.
        """
        for q in initalization_queries:
            self._database_cursor.execute(q, ())
            self._database_connection.commit()
    
    def fetch_tile(self, query, param=None):
        """
        Use this to fetch a tile from the current Database. The parameter changes
        based on the Query being used

        # SELECT_WITH_COLOR_BY_TILE
        fetch_tile(Tiles.SELECT_WITH_COLOR_BY_TILE, str)
        For this query the parameter must be a single character string

        # SELECT_WITH_COLOR_BY_NOISE
        fetch_tile(Tiles.SELECT_WITH_COLOR_BY_NOISE, (max_noise, min_noise))
        For this query the parameter must be a tuple of floats with the max noise
        value first and the min value second
        """

        match param:
            # Matching for SELECT_WITH_COLOR_BY_TILE
            case str():
                self._database_cursor.execute(query, param)
                self._database_connection.commit()
            # Matching for SELECT_WITH_COLOR_BY_NOISE
            case tuple():
                self._database_cursor.execute(query, param)
                self._database_connection.commit()
        tile_data = self._database_cursor.fetchone()
        return Tile(tile_data[0], tile_data[1], tile_data[2])

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *misc):
        pass