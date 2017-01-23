"""Describes exploration models."""

from .base import Base


class Scan(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Scan, self).__init__(data)


class MaterialCollected(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MaterialCollected, self).__init__(data)


class MaterialDiscarded(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MaterialDiscarded, self).__init__(data)


class MaterialDiscovered(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MaterialDiscovered, self).__init__(data)


class BuyExplorationData(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(BuyExplorationData, self).__init__(data)


class SellExplorationData(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(SellExplorationData, self).__init__(data)


class Screenshot(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Screenshot, self).__init__(data)
