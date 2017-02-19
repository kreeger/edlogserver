"""Describes enumerations used for explaining specific rank types."""

from enum import IntEnum


class CombatRank(IntEnum):
    """Used to describe a player's combat ranking."""

    HARMLESS = 0
    MOSTLY_HARMLESS = 1
    NOVICE = 2
    COMPETENT = 3
    EXPERT = 4
    MASTER = 5
    DANGEROUS = 6
    DEADLY = 7
    ELITE = 8


class TradeRank(IntEnum):
    """Used to describe a player's trade ranking."""

    PENNILESS = 0
    MOSTLY_PENNILESS = 1
    PEDDLER = 2
    DEALER = 3
    MERCHANT = 4
    BROKER = 5
    ENTREPRENEUR = 6
    TYCOON = 7
    ELITE = 8


class ExplorationRank(IntEnum):
    """Used to describe a player's exploration ranking."""

    AIMLESS = 0
    MOSTLY_AIMLESS = 1
    SCOUT = 2
    SURVEYOR = 3
    EXPLORER = 4
    PATHFINDER = 5
    RANGER = 6
    PIONEER = 7
    ELITE = 8


class FederationRank(IntEnum):
    """Used to describe a player's ranking in the Federation."""

    NONE = 0
    RECRUIT = 1
    CADET = 2
    MIDSHIPMAN = 3
    PETTY_OFFICER = 4
    CHIEF_PETTY_OFFICER = 5
    WARRANT_OFFICER = 6
    ENSIGN = 7
    LIEUTENANT = 8
    LIEUTENANT_COMMANDER = 9
    POST_COMMANDER = 10
    POST_CAPTAIN = 11
    REAR_ADMIRAL = 12
    VICE_ADMIRAL = 13
    ADMIRAL = 14


class EmpireRank(IntEnum):
    """Used to describe a player's ranking in the Empire."""

    NONE = 0
    OUTSIDER = 1
    SERF = 2
    MASTER = 3
    SQUIRE = 4
    KNIGHT = 5
    LORD = 6
    BARON = 7
    VISCOUNT = 8
    COUNT = 9
    EARL = 10
    MARQUIS = 11
    DUKE = 12
    PRINCE = 13
    KING = 14


class CQCRank(IntEnum):
    """Used to describe a player's ranking in Close Quarters Combat."""

    HELPLESS = 0
    MOSTLY_HELPLESS = 1
    AMATEUR = 2
    SEMI_PROFESSIONAL = 3
    PROFESSIONAL = 4
    CHAMPION = 5
    HERO = 6
    LEGEND = 7
    ELITE = 8
