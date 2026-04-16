from pathlib import Path
from textworld.data import DataManager, Database, TileQuery, WorldQuery, ColorQuery
from textworld.generation import Generator
from textworld.models import Size, Coords

class TextworldGame():

    data_manager: DataManager

    def __init__(self):
        self.data_manager = DataManager()
        self.core_file_validation()

        with Generator(1) as gen:
            gen.generate_chunk(self.data_manager.fetch_database("textworld"), Size(500, 500), Coords(0, 0))
    
    # TODO Move to DataManager
    def core_file_validation(self):
        if not Path("data/core/textworld").exists(): 
            self.data_manager.database_intialization(["data/core/", "textworld"])
            with self.data_manager.fetch_database("textworld") as db:
                db.intialize_database(Tile.INIT, Color.INIT, World.INIT, Tile.FILL, Color.FILL)
        else: 
            self.data_manager.add_database_to_manager(["data/core/", "textworld"])
