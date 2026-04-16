from pathlib import Path
from textworld.data import DataManager, Database, Tile, World, Color

class TextworldGame():

    data_manager: DataManager
    dummy_database: Database

    def __init__(self):
        self.data_manager = DataManager()
        self.core_file_validation()
        with self.data_manager.fetch_database("textworld") as db:
            db.connect()

            # Select by tile, 'str' as param
            #query = db.fetch_tile(Tile.SELECT_WITH_COLORS_BY_TILE, '~')
            
            # Select by noise value, (max , min) Tuple as params
            query = db.fetch_tile(Tile.SELECT_WITH_COLORS_BY_NOISE, (0.35, 0.25))
            print(query)
    
    def core_file_validation(self):
        if not Path("data/core/textworld").exists(): 
            self.data_manager.database_intialization(["data/core/", "textworld"])
            with self.data_manager.fetch_database("textworld") as db:
                db.connect()
                db.intialize_database(Tile.INIT, Color.INIT, World.INIT, Tile.FILL, Color.FILL)
        else: 
            self.data_manager.add_database_to_manager(["data/core/", "textworld"])
