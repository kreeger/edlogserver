"""Describes models that are written to the logs upon startup."""

from .base import BaseModel
from .enums.ranks import CombatRank, TradeRank, ExplorationRank, CQCRank
from .enums.ranks import FederationRank, EmpireRank


class ClearSavedGame(BaseModel):
    """Logged if you should ever reset your game."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ClearSavedGame, self).__init__(data)

        self.commander_name = data.get("Name")


class NewCommander(BaseModel):
    """Logged when creating a new commander."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(NewCommander, self).__init__(data)

        self.commander_name = data.get("Name")
        self.package = data.get("Package")


class LoadGame(BaseModel):
    """Logged at startup, when loading from main menu into game."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(LoadGame, self).__init__(data)

        self.commander_name = data.get("Commander")
        self.ship = data.get("Ship")
        self.ship_id = data.get("ShipID")
        self.game_mode = data.get("GameMode")
        self.group = data.get("Group")
        self.credits = data.get("Credits")
        self.loan = data.get("Loan")
        self.start_landed = data.get("StartLanded")


class Progress(BaseModel):
    """Logged at startup with percentages to the next levels."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Progress, self).__init__(data)

        self.combat = data.get("Combat")
        self.trade = data.get("Trade")
        self.explore = data.get("Explore")
        self.empire = data.get("Empire")
        self.federation = data.get("Federation")
        self.cqc = data.get("CQC")


class Rank(BaseModel):
    """Logged at startup."""

    # TODO: Add true rank names
    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Rank, self).__init__(data)

        self.combat = CombatRank(data.get("Combat"))
        self.trade = TradeRank(data.get("Trade"))
        self.explore = ExplorationRank(data.get("Explore"))
        self.empire = EmpireRank(data.get("Empire"))
        self.federation = FederationRank(data.get("Federation"))
        self.cqc = CQCRank(data.get("CQC"))
