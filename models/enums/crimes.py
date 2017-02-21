"""Describes enumerations used for explaining criminal activities."""

from enum import Enum


class Crime(Enum):
    """Used to describe the type of a committed crime."""

    ASSAULT = "assault"
    MURDER = "murder"
    PIRACY = "piracy"
    INTERDICTION = "interdiction"
    ILLEGAL_CARGO = "illegalCargo"
    DISOBEY_POLICE = "disobeyPolice"
    FIRE_IN_NO_FIRE_ZONE = "fireInNoFireZone"
    FIRE_IN_STATION = "fireInStation"
    DUMPING_DANGEROUS = "dumpingDangerous"
    DUMPING_NEAR_STATION = "dumpingNearStation"
    DOCKING_MINOR_BLOCKING_AIRLOCK = "dockingMinorBlockingAirlock"
    DOCKING_MAJOR_BLOCKING_AIRLOCK = "dockingMajorBlockingAirlock"
    DOCKING_MINOR_BLOCKING_LANDING_PAD = "dockingMinorBlockingLandingPad"
    DOCKING_MAJOR_BLOCKING_LANDING_PAD = "dockingMajorBlockingLandingPad"
    DOCKING_MINOR_TRESPASS = "dockingMinorTresspass"
    DOCKING_MAJOR_TRESPASS = "dockingMajorTresspass"
    RECKLESS_FLYING = "collidedAtSpeedInNoFireZone"
    RECKLESS_FLYING_HULL_DAMAGE = "collidedAtSpeedInNoFireZone_HullDamage"
