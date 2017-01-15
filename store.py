#!/usr/bin/env python

import models


class Store:
    def __init__(self, loader):
        self.loader = loader

    def import_data(self):
        self.models = [self._type_for(o)(o) for o in self.loader.load()]
        return self.models

    def _type_for(self, dict):
        switcher = {
            "fileheader": models.FileHeader,
        }
        return switcher.get(dict["event"].lower(), models.Base)
