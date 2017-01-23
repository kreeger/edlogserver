"""Describes classes needed to read and parse configuration data."""

import json


class Config:
    """Used to read and parse configuration data."""

    def __init__(self, path):
        """
        Initialize and return an instance of this object.

        Takes a filepath from which to load JSON configuration data.
        """
        self.data = self._parse(path)

    def _parse(self, path):
        json_data = open(path).read()
        data = json.loads(json_data)
        for (key, value) in data.items():
            self.__dict__[key] = value
        return data
