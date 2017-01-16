#!/usr/bin/env python

import dateutil.parser


class Base(object):
    def __init__(self, data):
        if data.get("timestamp"):
            self.timestamp = dateutil.parser.parse(data.get("timestamp"))
        else:
            self.timestamp = None
        self.event = data.get("event")

    def __str__(self):
        return "%s %r" % (self.__class__.__name__, self.__dict__)


class FileHeader(Base):
    def __init__(self, data):
        super(FileHeader, self).__init__(data)

        self.part = data.get("part")
        self.language = data.get("language")
        self.game_version = data.get("gameversion")
        self.build = data.get("build")
