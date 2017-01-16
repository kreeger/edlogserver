#!/usr/bin/env python

from .base import Base


class Docked(Base):
    def __init__(self, data):
        super(Docked, self).__init__(data)

        self.station_name = data.get("StationName")
        self.station_type = data.get("StationType")
        self.star_system = data.get("StarSystem")
        self.faction = data.get("Faction")
        self.faction_state = data.get("FactionState")
        self.allegiance = data.get("Allegiance")
        self.economy = data.get("Economy")
        self.government = data.get("Government")
        self.security = data.get("Security")

class DockingCancelled(Base):
    def __init__(self, data):
        super(DockingCancelled, self).__init__(data)


class DockingDenied(Base):
    def __init__(self, data):
        super(DockingDenied, self).__init__(data)


class DockingGranted(Base):
    def __init__(self, data):
        super(DockingGranted, self).__init__(data)


class DockingRequested(Base):
    def __init__(self, data):
        super(DockingRequested, self).__init__(data)


class DockingTimeout(Base):
    def __init__(self, data):
        super(DockingTimeout, self).__init__(data)


class FSDJump(Base):
    def __init__(self, data):
        super(FSDJump, self).__init__(data)


class Liftoff(Base):
    def __init__(self, data):
        super(Liftoff, self).__init__(data)


class Location(Base):
    def __init__(self, data):
        super(Location, self).__init__(data)


class SupercruiseEntry(Base):
    def __init__(self, data):
        super(SupercruiseEntry, self).__init__(data)


class SupercruiseExit(Base):
    def __init__(self, data):
        super(SupercruiseExit, self).__init__(data)


class Touchdown(Base):
    def __init__(self, data):
        super(Touchdown, self).__init__(data)


class Undocked(Base):
    def __init__(self, data):
        super(Undocked, self).__init__(data)
