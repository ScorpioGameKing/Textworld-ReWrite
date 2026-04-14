from pathlib import Path
from textworld.data import DataManager, Database, Tile, World, Color

class TextworldGame():

    data_manager: DataManager
    dummy_database: Database

    def __init__(self):
        self.data_manager = DataManager()
        self.core_file_validation()
    
    def core_file_validation(self):
        if not Path("data/core/textworld").exists(): 
            self.data_manager.database_intialization(["data/core/", "textworld"])
            with self.data_manager.fetch_database("textworld") as db:
                db.connect()
                db.intialize_database(Tile.INIT, Color.INIT, World.INIT, Tile.FILL, Color.FILL)
