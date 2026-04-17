from pathlib import Path
from textworld.data._database import Database
from textworld.data._queries import TileQuery, ColorQuery, WorldQuery

# TODO Add magic methods to remove need for explicit fetch function

class DataManager():
    """
    Used to manage and inteface with local Databases
    """

    __databases: dict

    def __init__(self):
        self.__databases = {}
        self.__core_file_validation()
    
    def __database_intialization(self, *databases):
        """
        Used to intialize a database and add it to the manager for later use

        *databases
        -> Any number of iterables in the order of [path, name]. These will
        be iterated through to ensure file paths exist and databases are created 
        """
        for db in databases:
            self.__create_missing_directory_tree(db[0])
            self.__databases.update({db[1]:Database(db[1], db[0])})

    def __add_database_to_manager(self, database):
        """
        Internally used to add an existing database to the manager

        database
        -> A single iterable in the order of [path, name] to add and existing
        database to the manager
        """
        self.__databases.update({database[1]: Database(database[1], database[0])})
    

    def __create_missing_directory_tree(self, location):
        """
        Internally used to create missing file paths

        location
        -> The full path to create 
        """
        Path(location).mkdir(parents=True, exist_ok=True)

    # TODO Further validation steps, hashing?
    def __core_file_validation(self):
        """
        Internally used to ensure the core textworld database exists
        """
        if not Path("data/core/textworld").exists(): 
            self.__database_intialization(["data/core/", "textworld"])
            with self.fetch_database("textworld") as db:
                db.intialize_database(TileQuery.INIT, ColorQuery.INIT, WorldQuery.INIT, TileQuery.FILL, ColorQuery.FILL)
        else: 
            self.__add_database_to_manager(["data/core/", "textworld"])

    def fetch_database(self, database_name):
        """
        Used to request a database from the manager for use

        database_name
        -> The name of the database to fetch from the manager
        """
        return self.__databases[database_name]