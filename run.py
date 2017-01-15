#!/usr/bin/env python

from server import Server
from config import Config
from parser import Parser
from loader import Loader
from store import Store

if __name__ == '__main__':
    # config = Config('./config.json')
    # Server.start(config)
    store = Store(Loader('./_journals', Parser))
    loaded = store.import_data()
    header = loaded[0]
    print(header)
