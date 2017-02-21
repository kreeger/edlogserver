"""Describes enumerations used for explaining exploration data."""

from enum import Enum


# Planets and celestial bodies

class BodyType(Enum):
    """Used to describe the type of a celestial body."""

    # (eg the barycentre of a binary star system)
    STAR = "Star"
    PLANET = "Planet"
    PLANETARY_RING = "PlanetaryRing"
    STELLAR_RING = "StellarRing"
    STATION = "Station"
    ASTEROID_CLUSTER = "AsteroidCluster"


class PlanetType(Enum):
    """Used to describe the type of a planet."""

    METAL_RICH_BODY = "Metal rich body"
    HIGH_METAL_CONTENT_BODY = "High metal content body"
    ROCKY_BODY = "Rocky body"
    ICY_BODY = "Icy body"
    ROCKY_ICE_BODY = "Rocky ice body"
    EARTHLIKE_BODY = "Earthlike body"
    WATER_WORLD = "Water world"
    AMMONIA_WORLD = "Ammonia world"
    WATER_GIANT = "Water giant"
    WATER_GIANT_WITH_LIFE = "Water giant with life"
    GAS_GIANT_WITH_WATER_BASED_LIFE = "Gas giant with water based life"
    GAS_GIANT_WITH_AMMONIA_BASED_LIFE = "Gas giant with ammonia based life"
    CLASS_I_GAS_GIANT = "Sudarsky class I gas giant"  # Ammonia clouds.
    CLASS_II_GAS_GIANT = "Sudarsky class II gas giant"  # Water clouds.
    CLASS_III_GAS_GIANT = "Sudarsky class III gas giant"  # Cloudless.
    CLASS_IV_GAS_GIANT = "Sudarsky class IV gas giant"  # Alkali metals.
    CLASS_V_GAS_GIANT = "Sudarsky class V gas giant"  # Silicate clouds.
    HELIUM_RICH_GAS_GIANT = "Helium rich gas giant"
    HELIUM_GAS_GIANT = "Helium gas giant"


class Atmosphere(Enum):
    """Used to describe the type of a planet's atmosphere."""

    NO_ATMOSPHERE = ""

    SUITABLE_FOR_WATER_BASED_LIFE = "suitable for water based life atmosphere"

    OXYGEN = "oxygen atmosphere"

    AMMONIA_AND_OXYGEN = "ammonia and oxygen atmosphere"
    AMMONIA = "ammonia atmosphere"
    THIN_AMMONIA = "thin ammonia atmosphere"
    THICK_AMMONIA = "thick ammonia atmosphere"
    AMMONIA_RICH = "ammonia rich atmosphere"
    THIN_AMMONIA_RICH = "thin ammonia rich atmosphere"
    THICK_AMMONIA_RICH = "thick ammonia rich atmosphere"

    WATER = "water atmosphere"
    THIN_WATER = "thin water atmosphere"
    THICK_WATER = "thick water atmosphere"
    HOT_WATER = "hot water atmosphere"
    HOT_THIN_WATER = "hot thin water atmosphere"
    HOT_THICK_WATER = "hot thick water atmosphere"
    WATER_RICH = "water rich atmosphere"
    THIN_WATER_RICH = "thin water rich atmosphere"
    THICK_WATER_RICH = "thick water rich atmosphere"

    CARBON_DIOXIDE = "carbon dioxide atmosphere"
    THIN_CARBON_DIOXIDE = "thin carbon dioxide atmosphere"
    THICK_CARBON_DIOXIDE = "thick carbon dioxide atmosphere"
    CARBON_DIOXIDE_RICH = "carbon dioxide rich atmosphere"
    THIN_CARBON_DIOXIDE_RICH = "thin carbon dioxide rich atmosphere"
    THICK_CARBON_DIOXIDE_RICH = "thick carbon dioxide rich atmosphere"

    SULPHUR_DIOXIDE = "sulphur dioxide atmosphere"
    THIN_SULPHUR_DIOXIDE = "thin sulphur dioxide atmosphere"
    THICK_SULPHUR_DIOXIDE = "thick sulphur dioxide atmosphere"
    HOT_SULPHUR_DIOXIDE = "hot sulphur dioxide atmosphere"
    THIN_HOT_SULPHUR_DIOXIDE = "hot thin sulphur dioxide atmosphere"
    THICK_HOT_SULPHUR_DIOXIDE = "hot thick sulphur dioxide atmosphere"

    NITROGEN = "nitrogen atmosphere"

    METHANE = "methane atmosphere"
    THIN_METHANE = "thin methane atmosphere"
    THICK_METHANE = "thick methane atmosphere"
    METHANE_RICH = "methane rich atmosphere"
    THIN_METHANE_RICH = "thin methane rich atmosphere"
    THICK_METHANE_RICH = "thick methane rich atmosphere"

    HELIUM = "helium atmosphere"

    SILICATE_VAPOUR = "silicate vapour atmosphere"
    METALLIC_VAPOUR = "metallic vapour atmosphere"

    NEON = "neon atmosphere"
    THIN_NEON = "thin neon atmosphere"
    THICK_NEON = "thick neon atmosphere"
    NEON_RICH = "neon rich atmosphere"
    THIN_NEON_RICH = "thin neon rich atmosphere"
    THICK_NEON_RICH = "thick neon rich atmosphere"

    ARGON = "argon atmosphere"
    THIN_ARGON = "thin argon atmosphere"
    THICK_ARGON = "thick argon atmosphere"
    ARGON_RICH = "argon rich atmosphere"
    THIN_ARGON_RICH = "thin argon rich atmosphere"
    THICK_ARGON_RICH = "thick argon rich atmosphere"


class Volcanism(Enum):
    """Used to describe the type of planet's volcansim."""

    NONE = ""

    ROCKY_MAGMA = "rocky magma volcanism"
    MAJOR_ROCKY_MAGMA = "major rocky magma volcanism"
    MINOR_ROCKY_MAGMA = "minor rocky magma volcanism"

    WATER_MAGMA = "water magma volcanism"
    MAJOR_WATER_MAGMA = "major water magma volcanism"
    MINOR_WATER_MAGMA = "minor water magma volcanism"

    SULPHUR_DIOXIDE_MAGMA = "sulphur dioxide magma volcanism"
    MAJOR_SULPHUR_DIOXIDE_MAGMA = "major sulphur dioxide magma volcanism"
    MINOR_SULPHUR_DIOXIDE_MAGMA = "minor sulphur dioxide magma volcanism"

    AMMONIA_MAGMA = "ammonia magma volcanism"
    MAJOR_AMMONIA_MAGMA = "major ammonia magma volcanism"
    MINOR_AMMONIA_MAGMA = "minor ammonia magma volcanism"

    METHANE_MAGMA = "methane magma volcanism"
    MAJOR_METHANE_MAGMA = "major methane magma volcanism"
    MINOR_METHANE_MAGMA = "minor methane magma volcanism"

    NITROGEN_MAGMA = "nitrogen magma volcanism"
    MAJOR_NITROGEN_MAGMA = "major nitrogen magma volcanism"
    MINOR_NITROGEN_MAGMA = "minor nitrogen magma volcanism"

    SILICATE_MAGMA = "silicate magma volcanism"
    MAJOR_SILICATE_MAGMA = "major silicate magma volcanism"
    MINOR_SILICATE_MAGMA = "minor silicate magma volcanism"

    METALLIC_MAGMA = "metallic magma volcanism"
    MAJOR_METALLIC_MAGMA = "major metallic magma volcanism"
    MINOR_METALLIC_MAGMA = "minor metallic magma volcanism"

    WATER_GEYSERS = "water geysers volcanism"
    MAJOR_WATER_GEYSERS = "major water geysers volcanism"
    MINOR_WATER_GEYSERS = "minor water geysers volcanism"

    CARBON_DIOXIDE_GEYSERS = "carbon dioxide geysers volcanism"
    MAJOR_CARBON_DIOXIDE_GEYSERS = "major carbon dioxide geysers volcanism"
    MINOR_CARBON_DIOXIDE_GEYSERS = "minor carbon dioxide geysers volcanism"

    AMMONIA_GEYSERS = "ammonia geysers volcanism"
    MAJOR_AMMONIA_GEYSERS = "major ammonia geysers volcanism"
    MINOR_AMMONIA_GEYSERS = "minor ammonia geysers volcanism"

    METHANE_GEYSERS = "methane geysers volcanism"
    MAJOR_METHANE_GEYSERS = "major methane geysers volcanism"
    MINOR_METHANE_GEYSERS = "minor methane geysers volcanism"

    NITROGEN_GEYSERS = "nitrogen geysers volcanism"
    MAJOR_NITROGEN_GEYSERS = "major nitrogen geysers volcanism"
    MINOR_NITROGEN_GEYSERS = "minor nitrogen geysers volcanism"

    HELIUM_GEYSERS = "helium geysers volcanism"
    MAJOR_HELIUM_GEYSERS = "major helium geysers volcanism"
    MINOR_HELIUM_GEYSERS = "minor helium geysers volcanism"

    SILICATE_VAPOUR_GEYSERS = "silicate vapour geysers volcanism"
    MAJOR_SILICATE_VAPOUR_GEYSERS = "major silicate vapour geysers volcanism"
    MINOR_SILICATE_VAPOUR_GEYSERS = "minor silicate vapour geysers volcanism"


class TerraformState(Enum):
    """Used to describe the terraforming state of a planet."""

    NONE = ""
    TERRAFORMABLE = "Terraformable"
    TERRAFORMING = "Terraforming"
    TERRAFORMED = "Terraformed"


# Stars

class StarType(Enum):
    """Used to describe the type of a star."""

    # Main sequence
    MAIN_SEQUENCE_O = "O"
    MAIN_SEQUENCE_B = "B"
    MAIN_SEQUENCE_A = "A"
    MAIN_SEQUENCE_F = "F"
    MAIN_SEQUENCE_G = "G"
    MAIN_SEQUENCE_K = "K"
    MAIN_SEQUENCE_M = "M"
    MAIN_SEQUENCE_L = "L"
    MAIN_SEQUENCE_T = "T"
    MAIN_SEQUENCE_Y = "Y"
    MAIN_SEQUENCE_A_BLUE_WHITE_SUPERGIANT = "A_BlueWhiteSuperGiant"
    MAIN_SEQUENCE_F_WHITE_SUPERGIANT = "F_WhiteSuperGiant"
    MAIN_SEQUENCE_M_RED_SUPERGIANT = "M_Red_SuperGiant"
    MAIN_SEQUENCE_M_RED_GIANT = "M_RedGiant"
    MAIN_SEQUENCE_K_ORANGE_GIANT = "K_OrangeGiant"

    # Proto
    PROTO_TTS = "TTS"
    PROTO_AeBe = "AeBe"

    # Wolf-Rayet
    WOLF_RAYET_W = "W"
    WOLF_RAYET_WN = "WN"
    WOLF_RAYET_WNC = "WNC"
    WOLF_RAYET_WC = "WC"
    WOLF_RAYET_WO = "WO"

    # Carbon stars
    CARBON_CS = "CS"
    CARBON_C = "C"
    CARBON_CN = "CN"
    CARBON_CJ = "CJ"
    CARBON_CH = "CH"
    CARBON_CHd = "CHd"
    CARBON_MS = "MS"
    CARBON_S = "S"

    # White dwarf stars
    WHITE_DWARF_D = "D"
    WHITE_DWARF_DA = "DA"
    WHITE_DWARF_DAB = "DAB"
    WHITE_DWARF_DAO = "DAO"
    WHITE_DWARF_DAZ = "DAZ"
    WHITE_DWARF_DAV = "DAV"
    WHITE_DWARF_DB = "DB"
    WHITE_DWARF_DBZ = "DBZ"
    WHITE_DWARF_DBV = "DBV"
    WHITE_DWARF_DO = "DO"
    WHITE_DWARF_DOV = "DOV"
    WHITE_DWARF_DQ = "DQ"
    WHITE_DWARF_DC = "DC"
    WHITE_DWARF_DCV = "DCV"
    WHITE_DWARF_DX = "DX"

    # Non-sequence stars
    NEUTRON = "N"
    BLACK_HOLE = "H"
    EXOTIC = "X"
    SUPERMASSIVE_BLACK_HOLE = "SupermassiveBlackHole"
    ROGUE_PLANET = "RoguePlanet"
    NEBULA = "Nebula"
    STELLAR_REMNANT_NEBULA = "StellarRemnantNebula"


# Other

class MaterialCategory(Enum):
    """Used to describe the type of a material."""

    RAW = "Raw"
    MANUFACTURED = "Manufactured"
    ENCODED = "Encoded"
