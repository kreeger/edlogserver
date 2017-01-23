"""Describes trading models."""

from .base import Base


class BuyTradeData(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(BuyTradeData, self).__init__(data)


class CollectCargo(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(CollectCargo, self).__init__(data)


class EjectCargo(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(EjectCargo, self).__init__(data)


class MarketBuy(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MarketBuy, self).__init__(data)


class MarketSell(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MarketSell, self).__init__(data)


class MiningRefined(Base):
    """Docstring."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MiningRefined, self).__init__(data)
