#!/usr/bin/env python

from .base import Base


class ClearSavedGame(Base):
    def __init__(self, data):
        super(ClearSavedGame, self).__init__(data)

        self.commander_name = data.get("Name")


class NewCommander(Base):
    def __init__(self, data):
        super(NewCommander, self).__init__(data)

        self.commander_name = data.get("Name")
        self.package = data.get("Package")


class LoadGame(Base):
    def __init__(self, data):
        super(LoadGame, self).__init__(data)

        self.commander_name = data.get("Commander")
        self.ship = data.get("Ship")
        self.ship_id = data.get("ShipID")
        self.game_mode = data.get("GameMode")
        self.group = data.get("Group")
        self.credits = data.get("Credits")
        self.loan = data.get("Loan")
        self.start_landed = data.get("StartLanded")


class Progress(Base):
    def __init__(self, data):
        super(Progress, self).__init__(data)

        self.combat = data.get("Combat")
        self.trade = data.get("Trade")
        self.explore = data.get("Explore")
        self.empire = data.get("Empire")
        self.federation = data.get("Federation")
        self.cqc = data.get("CQC")


class Rank(Base):
    # TODO: Add true rank names
    def __init__(self, data):
        super(Rank, self).__init__(data)

        self.combat = data.get("Combat")
        self.trade = data.get("Trade")
        self.explore = data.get("Explore")
        self.empire = data.get("Empire")
        self.federation = data.get("Federation")
        self.cqc = data.get("CQC")
