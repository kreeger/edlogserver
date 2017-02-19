"""Describes enumerations used for explaining criminal activities."""

from enum import Enum, auto


class Crime(Enum):
    """Used to describe the type of a committed crime."""

    ASSAULT = auto()
    MURDER = auto()
    PIRACY = auto()
    INTERDICTION = auto()
    ILLEGAL_CARGO = auto()
    DISOBEY_POLICE = auto()
    FIRE_IN_NO_FIRE_ZONE = auto()
    FIRE_IN_STATION = auto()
    DUMPING_DANGEROUS = auto()
    DUMPING_NEAR_STATION = auto()
    DOCKING_MINOR_BLOCKING_AIRLOCK = auto()
    DOCKING_MAJOR_BLOCKING_AIRLOCK = auto()
    DOCKING_MINOR_BLOCKING_LANDING_PAD = auto()
    DOCKING_MAJOR_BLOCKING_LANDING_PAD = auto()
    DOCKING_MINOR_TRESPASS = auto()
    DOCKING_MAJOR_TRESPASS = auto()
    COLLIDED_AT_SPEED_IN_NO_FIRE_ZONE = auto()
    COLLIDED_AT_SPEED_IN_NO_FIRE_ZONE_HULL_DAMAGE = auto()
