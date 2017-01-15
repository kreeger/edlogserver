#!/usr/bin/env python

import json


class Config:
    def __init__(self, path):
        self.data = self._parse(path)

    def _parse(self, path):
        json_data = open(path).read()
        data = json.loads(json_data)
        for (key, value) in data.items():
            self.__dict__[key] = value
        return data
