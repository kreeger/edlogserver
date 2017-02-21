"""Describes exploration models."""

from .base import BaseModel
from .enums.exploration import StarType, PlanetType, Atmosphere, Volcanism
from .enums.exploration import TerraformState, MaterialCategory


class Scan(BaseModel):
    """Logged upon a detailed discovery scan of a star, planet or moon."""

    @classmethod
    def from_api(cls, data):
        """Determine scan type from data and return the proper instance."""
        if "StarType" in data:
            return StarScan(data)
        else:
            return PlanetScan(data)

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Scan, self).__init__(data)

        self.body_name = data.get("BodyName")
        self.distance_from_arrival_ls = data.get("DistanceFromArrivalLS")
        self.semi_major_axis = data.get("SemiMajorAxis")
        self.eccentricity = data.get("Eccentricity")
        self.orbital_inclination = data.get("OrbitalInclination")
        self.periapsis = data.get("Periapsis")
        self.orbital_period = data.get("OrbitalPeriod")
        self.rotation_period = data.get("RotationPeriod")
        self.surface_temperature = data.get("SurfaceTemperature")
        if "Rings" in data:
            self.rings = [CelestialRing(d) for d in data.get("Rings")]
        else:
            self.rings = []


class StarScan(Scan):
    """Logged upon a detailed discovery scan of a star."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(StarScan, self).__init__(data)

        self.star_type = StarType(data.get("StarType"))
        self.stellar_mass = data.get("StellarMass")
        self.radius = data.get("Radius")
        self.absolute_magnitude = data.get("AbsoluteMagnitude")
        self.age_my = data.get("Age_MY")


class PlanetScan(Scan):
    """Logged upon a detailed discovery scan of a planet or moon."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PlanetScan, self).__init__(data)

        self.tidal_lock = data.get("TidalLock")
        terraform_state = data.get("TerraformState")
        self.terraform_state = TerraformState(terraform_state)
        self.planet_class = PlanetType(data.get("PlanetClass"))
        self.atmosphere = Atmosphere(data.get("Atmosphere"))
        self.volcanism = Volcanism(data.get("Volcanism"))
        self.surface_gravity = data.get("SurfaceGravity")
        self.surface_pressure = data.get("SurfacePressure")
        self.landable = data.get("Landable")
        self.materials = data.get("Materials")


class CelestialRing(BaseModel):
    """Logged upon a detailed discovery scan of a ring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(CelestialRing, self).__init__(data)

        self.name = data.get("Name")
        self.ring_class = data.get("RingClass")
        self.mass_mt = data.get("MassMT")
        self.inner_rad = data.get("InnerRad")
        self.outer_rad = data.get("OuterRad")


class MaterialCollected(BaseModel):
    """Logged whenever materials are collected."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MaterialCollected, self).__init__(data)

        self.category = MaterialCategory(data.get("Category"))
        self.name = data.get("Name")
        self.count = data.get("Count")


class MaterialDiscarded(BaseModel):
    """Logged whenever materials are discarded."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MaterialDiscarded, self).__init__(data)

        self.category = MaterialCategory(data.get("Category"))
        self.name = data.get("Name")
        self.count = data.get("Count")


class MaterialDiscovered(BaseModel):
    """Logged when a new material is discovered."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MaterialDiscovered, self).__init__(data)

        self.category = MaterialCategory(data.get("Category"))
        self.name = data.get("Name")
        self.discovery_number = data.get("DiscoveryNumber")


class BuyExplorationData(BaseModel):
    """Logged when buying system data via the galaxy map."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(BuyExplorationData, self).__init__(data)

        self.system = data.get("System")
        self.cost = data.get("Cost")


class SellExplorationData(BaseModel):
    """Logged when selling exploration data in Universal Cartographics."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(SellExplorationData, self).__init__(data)

        self.system_names = data.get("Systems")
        self.discovered_bodies = data.get("Discovered")
        self.base_value = data.get("BaseValue")
        self.bonus = data.get("Bonus")


class Screenshot(BaseModel):
    """Logged when a screen snapshot is saved."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Screenshot, self).__init__(data)

        self.filename = data.get("Filename")
        self.width = data.get("Width")
        self.height = data.get("Height")
        self.system = data.get("System")
        self.body = data.get("Body")
