#!/usr/bin/env python

import dateutil.parser


class Base:
    def __init__(self, data):
        for (key, value) in data.items():
            setattr(self, "%s" % key, value)

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = dateutil.parser.parse(value)

    def event(self):
        return self._event

    def __str__(self):
        return "%s %r" % (self.__class__.__name__, self.__dict__)
