#!/usr/bin/env python

from server import Server
from config import Config
from parser import Parser

if __name__ == '__main__':
    # config = Config('./config.json')
    # Server.start(config)
    Parser('./_journals/Journal.160920134531.01.log')
