"""Describes enumerations used for explaining specific star types."""

from enum import Enum, auto


class MainSequence(Enum):
    """Used to describe the type of a main-sequence star."""

    CLASS_O = auto()
    CLASS_B = auto()
    CLASS_A = auto()
    CLASS_F = auto()
    CLASS_G = auto()
    CLASS_K = auto()
    CLASS_M = auto()
    CLASS_L = auto()
    CLASS_T = auto()
    CLASS_Y = auto()

    CLASS_A_BLUE_WHITE_SUPERGIANT = auto()
    CLASS_F_WHITE_SUPERGIANT = auto()
    CLASS_M_RED_SUPERGIANT = auto()
    CLASS_M_RED_GIANT = auto()
    CLASS_K_ORANGE_GIANT = auto()


class Proto(Enum):
    """Used to describe the type of a proto star."""

    CLASS_TTS = auto()
    CLASS_AeBe = auto()


class WolfRayet(Enum):
    """Used to describe the type of a wolf-rayet star."""

    CLASS_W = auto()
    CLASS_WN = auto()
    CLASS_WNC = auto()
    CLASS_WC = auto()
    CLASS_WO = auto()


class Carbon(Enum):
    """Used to describe the type of a carbon star."""

    CLASS_CS = auto()
    CLASS_C = auto()
    CLASS_CN = auto()
    CLASS_CJ = auto()
    CLASS_CH = auto()
    CLASS_CHd = auto()
    CLASS_MS = auto()
    CLASS_S = auto()


class WhiteDwarf(Enum):
    """Used to describe the type of a white dwarf star."""

    CLASS_D = auto()
    CLASS_DA = auto()
    CLASS_DAB = auto()
    CLASS_DAO = auto()
    CLASS_DAZ = auto()
    CLASS_DAV = auto()
    CLASS_DB = auto()
    CLASS_DBZ = auto()
    CLASS_DBV = auto()
    CLASS_DO = auto()
    CLASS_DOV = auto()
    CLASS_DQ = auto()
    CLASS_DC = auto()
    CLASS_DCV = auto()
    CLASS_DX = auto()


class NonSequence(Enum):
    """Used to describe the type of a non-sequence star."""

    NEUTRON = auto()
    BLACK_HOLE = auto()
    EXOTIC = auto()
    SUPERMASSIVE_BLACK_HOLE = auto()
    ROGUE_PLANET = auto()
    NEBULA = auto()
    STELLAR_REMNANT_NEBULA = auto()
