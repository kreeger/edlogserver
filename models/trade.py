"""Describes trading models."""

from .base import Base


class BuyTradeData(Base):
    """Logged when buying trade data in the galaxy map."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(BuyTradeData, self).__init__(data)

        self.system = data.get("System")
        self.cost = data.get("Cost")


class CollectCargo(Base):
    """Logged when scooping cargo from space or planet surface."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(CollectCargo, self).__init__(data)

        self.type = data.get("Type")
        self.stolen = data.get("Stolen")


class EjectCargo(Base):
    """Logged when cargo is ejected."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(EjectCargo, self).__init__(data)

        self.type = data.get("Type")
        self.count = data.get("Count")
        self.abandoned = data.get("Abandoned")
        self.powerplay_origin = data.get("PowerplayOrigin")


class MarketBuy(Base):
    """Logged when purchasing goods in the market."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MarketBuy, self).__init__(data)

        self.type = data.get("Type")
        self.count = data.get("Count")
        self.buy_price = data.get("BuyPrice")
        self.total_cost = data.get("TotalCost")


class MarketSell(Base):
    """Logged when selling goods in the market."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MarketSell, self).__init__(data)

        self.type = data.get("Type")
        self.count = data.get("Count")
        self.sell_price = data.get("SellPrice")
        self.total_sale = data.get("TotalSale")
        self.average_price_paid = data.get("AvgPricePaid")
        self.illegal_goods = data.get("IllegalGoods")
        self.stolen_goods = data.get("StolenGoods")
        self.black_market = data.get("BlackMarket")


class MiningRefined(Base):
    """Logged when mining fragments are refined into a unit of cargo."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MiningRefined, self).__init__(data)

        self.type = data.get("Type")
