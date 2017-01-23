"""Main execution procedures."""

# from server import Server
# from config import Config
from parser import JSONParser
from loader import Loader
from store import Store

if __name__ == '__main__':
    # config = Config('./config.json')
    # Server.start(config)
    store = Store(Loader('./_journals', JSONParser))
    loaded = store.import_data()
    obj = [l for l in loaded if l.event == "FSDJump"][0]
    print(obj)
