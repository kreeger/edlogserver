"""Describes travel models."""

from .base import Base


class Docked(Base):
    """Logged when landing at a space station, outpost, or settlement."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
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
    """Logged when the player cancels a docking request."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(DockingCancelled, self).__init__(data)

        self.station_name = data.get("StationName")


class DockingDenied(Base):
    """Logged when the station denies a docking request."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(DockingDenied, self).__init__(data)

        self.station_name = data.get("StationName")
        self.reason = data.get("Reason")
        # NoSpace, TooLarge, Hostile, Offences, Distance,
        #   ActiveFighter, NoReason


class DockingGranted(Base):
    """Logged when a docking request is granted."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(DockingGranted, self).__init__(data)

        self.station_name = data.get("StationName")
        self.landing_pad = data.get("LandingPad")


class DockingRequested(Base):
    """Logged when the player requests docking at a station."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(DockingRequested, self).__init__(data)

        self.station_name = data.get("StationName")


class DockingTimeout(Base):
    """Logged when a docking request has timed out."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(DockingTimeout, self).__init__(data)

        self.station_name = data.get("StationName")


class FSDJump(Base):
    """Logged when jumping from one star system to another."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(FSDJump, self).__init__(data)

        self.star_system = data.get("StarSystem")
        self.star_position = data.get("StarPos")
        self.body = data.get("Body")
        self.jump_distance = data.get("JumpDist")
        self.fuel_used = data.get("FuelUsed")
        self.fuel_level = data.get("FuelLevel")
        self.boost_used = data.get("BoostUsed")
        self.faction = data.get("Faction")
        self.faction_state = data.get("FactionState")
        self.allegiance = data.get("Allegiance")
        self.economy = data.get("Economy")
        self.government = data.get("Government")
        self.security = data.get("Security")

        # Powerplay values.
        self.powers = data.get("Powers")
        self.powerplay_state = data.get("PowerplayState")


class Liftoff(Base):
    """Logged when taking off from planet surface."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Liftoff, self).__init__(data)

        self.latitude = data.get("Latitude")
        self.longitude = data.get("Longitude")


class Location(Base):
    """Logged at startup, or when being resurrected at a station."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Location, self).__init__(data)

        self.star_system = data.get("StarSystem")
        self.star_position = data.get("StarPos")
        self.body = data.get("Body")
        self.body_type = data.get("BodyType")
        self.docked = data.get("Docked")
        self.station_name = data.get("StationName")
        self.station_type = data.get("StationType")
        self.faction = data.get("Faction")
        self.faction_state = data.get("FactionState")
        self.allegiance = data.get("Allegiance")
        self.economy = data.get("Economy")
        self.government = data.get("Government")
        self.security = data.get("Security")

        # Powerplay values.
        self.powers = data.get("Powers")
        self.powerplay_state = data.get("PowerplayState")


class SupercruiseEntry(Base):
    """Logged when entering supercruise from normal space."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(SupercruiseEntry, self).__init__(data)

        self.star_system = data.get("Starsystem")


class SupercruiseExit(Base):
    """Logged when leaving supercruise for normal space."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(SupercruiseExit, self).__init__(data)

        self.star_system = data.get("Starsystem")
        self.body = data.get("Body")
        self.body_type = data.get("BodyType")


class Touchdown(Base):
    """Logged when landing on a planet surface."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Touchdown, self).__init__(data)

        self.latitude = data.get("Latitude")
        self.longitude = data.get("Longitude")


class Undocked(Base):
    """Logged upon liftoff from a station, outpost or settlement."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Undocked, self).__init__(data)

        self.station_name = data.get("StationName")
