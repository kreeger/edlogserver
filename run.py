"""Main execution procedures."""

# from server import Server
# from config import Config
from parser import JSONParser
from loader import Loader
from store import Store
from models import SupercruiseExit

if __name__ == '__main__':
    # config = Config('./config.json')
    # Server.start(config)
    store = Store(Loader('./_journals', JSONParser))
    loaded = store.import_data()
    [print(l.body_type) for l in loaded if isinstance(l, SupercruiseExit)]
