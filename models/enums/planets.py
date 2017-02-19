"""Describes enumerations used for explaining specific planet types."""

from enum import Enum, auto


class BodyType(Enum):
    """Used to describe the type of a celestial body."""

    # (eg the barycentre of a binary star system)
    NULL = auto()
    STAR = auto()
    PLANET = auto()
    PLANETARY_RING = auto()
    STELLAR_RING = auto()
    STATION = auto()
    ASTEROID_CLUSTER = auto()


class PlanetType(Enum):
    """Used to describe the type of a planet."""

    METAL_RICH_BODY = auto()
    HIGH_METAL_CONTENT_BODY = auto()
    ROCKY_BODY = auto()
    ICY_BODY = auto()
    ROCKY_ICE_BODY = auto()
    EARTHLIKE_BODY = auto()
    WATER_WORLD = auto()
    AMMONIA_WORLD = auto()
    WATER_GIANT = auto()
    WATER_GIANT_WITH_LIFE = auto()
    GAS_GIANT_WITH_WATER_BASED_LIFE = auto()
    GAS_GIANT_WITH_AMMONIA_BASED_LIFE = auto()
    SUDARSKY_CLASS_I_GAS_GIANT = auto()
    SUDARSKY_CLASS_II_GAS_GIANT = auto()
    SUDARSKY_CLASS_III_GAS_GIANT = auto()
    SUDARSKY_CLASS_IV_GAS_GIANT = auto()
    SUDARSKY_CLASS_V_GAS_GIANT = auto()
    HELIUM_RICH_GAS_GIANT = auto()
    HELIUM_GAS_GIANT = auto()


class AtmosphereType(Enum):
    """Used to describe the type of a planet's atmosphere."""

    NO_ATMOSPHERE = auto()
    SUITABLE_FOR_WATER_BASED_LIFE = auto()
    AMMONIA_AND_OXYGEN = auto()
    AMMONIA = auto()
    WATER = auto()
    CARBON_DIOXIDE = auto()
    SULPHUR_DIOXIDE = auto()
    NITROGEN = auto()
    WATER_RICH = auto()
    METHANE_RICH = auto()
    AMMONIA_RICH = auto()
    CARBON_DIOXIDE_RICH = auto()
    METHANE = auto()
    HELIUM = auto()
    SILICATE_VAPOUR = auto()
    METALLIC_VAPOUR = auto()
    NEON_RICH = auto()
    ARGON_RICH = auto()
    NEON = auto()
    ARGON = auto()
    OXYGEN = auto()


class VolcanismType(Enum):
    """Used to describe the type of planet's volcansim."""

    NONE = auto()
    MAJOR_WATER_MAGMA = auto()
    MINOR_WATER_MAGMA = auto()
    MAJOR_SULPHUR_DIOXIDE_MAGMA = auto()
    MINOR_SULPHUR_DIOXIDE_MAGMA = auto()
    MAJOR_AMMONIA_MAGMA = auto()
    MINOR_AMMONIA_MAGMA = auto()
    MAJOR_METHANE_MAGMA = auto()
    MINOR_METHANE_MAGMA = auto()
    MAJOR_NITROGEN_MAGMA = auto()
    MINOR_NITROGEN_MAGMA = auto()
    MAJOR_SILICATE_MAGMA = auto()
    MINOR_SILICATE_MAGMA = auto()
    MAJOR_METALLIC_MAGMA = auto()
    MINOR_METALLIC_MAGMA = auto()
    MAJOR_WATER_GEYSERS = auto()
    MINOR_WATER_GEYSERS = auto()
    MAJOR_CARBON_DIOXIDE_GEYSERS = auto()
    MINOR_CARBON_DIOXIDE_GEYSERS = auto()
    MAJOR_AMMONIA_GEYSERS = auto()
    MINOR_AMMONIA_GEYSERS = auto()
    MAJOR_METHANE_GEYSERS = auto()
    MINOR_METHANE_GEYSERS = auto()
    MAJOR_NITROGEN_GEYSERS = auto()
    MINOR_NITROGEN_GEYSERS = auto()
    MAJOR_HELIUM_GEYSERS = auto()
    MINOR_HELIUM_GEYSERS = auto()
    MAJOR_SILICATE_VAPOUR_GEYSERS = auto()
    MINOR_SILICATE_VAPOUR_GEYSERS = auto()
