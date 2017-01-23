"""Handles all data storage needs for importing JSON models."""

import models


class Store:
    """Handles all data storage needs for importing JSON models"""

    def __init__(self, loader):
        self.loader = loader
        self.models = []

    def import_data(self):
        """Imports all model data using the loader."""

        self.models = [self.type_for(o)(o) for o in self.loader.load()]
        return self.models

    @staticmethod
    def type_for(data):
        """Returns the class type to be used for a given event name."""

        switcher = {
            "fileheader": models.FileHeader,
            "clearsavedgame": models.ClearSavedGame,
            "newcommander": models.NewCommander,
            "loadgame": models.LoadGame,
            "progress": models.Progress,
            "rank": models.Rank,
            "docked": models.Docked,
            "dockingcancelled": models.DockingCancelled,
            "dockingdenied": models.DockingDenied,
            "dockinggranted": models.DockingGranted,
            "dockingrequested": models.DockingRequested,
            "dockingtimeout": models.DockingTimeout,
            "fsdjump": models.FSDJump,
            "liftoff": models.Liftoff,
            "location": models.Location,
            "supercruiseentry": models.SupercruiseEntry,
            "supercruiseexit": models.SupercruiseExit,
            "touchdown": models.Touchdown,
            "undocked": models.Undocked,
        }
        return switcher.get(data["event"].lower(), models.Base)
