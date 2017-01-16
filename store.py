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
        return switcher.get(dict["event"].lower(), models.Base)
