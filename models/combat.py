"""Describes combat models."""

from .base import Base


class Bounty(Base):
    """Logged when a player is awarded a bounty for a kill.."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Bounty, self).__init__(data)

        # TODO: Parse these into Reward objects (faction, reward)
        self.rewards = data.get("Rewards")
        self.victim_faction = data.get("VictimFaction")
        self.total_reward = data.get("TotalReward")
        self.shared_with_others = data.get("SharedWithOthers")


class _Bond(Base):
    """Logged when a an internal base class for a combat bond."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(_Bond, self).__init__(data)

        self.reward = data.get("Reward")
        self.awarding_faction = data.get("AwardingFaction")
        self.victim_faction = data.get("VictimFaction")


class CapShipBond(_Bond):
    """Logged when a the player has been rewarded for a capital ship combat."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(CapShipBond, self).__init__(data)


class Died(Base):
    """Logged when a player was killed."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Died, self).__init__(data)

        self.killer_name = data.get("KillerName")
        self.killer_ship = data.get("KillerShip")
        self.killer_rank = data.get("KillerRank")

        # Or, if killed by a wing. Name, Ship, Rank.
        self.killers = data.get("Killers")


class EscapeInterdiction(Base):
    """Logged when a player has escaped interdiction."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(EscapeInterdiction, self).__init__(data)

        self.interdictor = data.get("Interdictor")
        self.is_player = data.get("IsPlayer")


class FactionKillBond(_Bond):
    """Logged when a player rewarded for taking part in a combat zone."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(FactionKillBond, self).__init__(data)


class HeatDamage(Base):
    """Logged when a when taking damage due to overheating."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(HeatDamage, self).__init__(data)


class HeatWarning(Base):
    """Logged when a when heat exceeds 100%."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(HeatWarning, self).__init__(data)


class HullDamage(Base):
    """Logged when a when hull health drops below a threshold (20% steps)."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(HullDamage, self).__init__(data)

        self.health = data.get("Health")


class Interdicted(Base):
    """Logged when a player was interdicted by player or npc."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Interdicted, self).__init__(data)

        self.submitted = data.get("Submitted")
        self.interdictor = data.get("Interdictor")
        self.is_player = data.get("IsPlayer")
        self.combat_rank = data.get("CombatRank")
        self.faction = data.get("Faction")
        self.power = data.get("Power")


class Interdiction(Base):
    """Logged when a player has attempted to interdict a player or npc."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Interdiction, self).__init__(data)

        self.success = data.get("Success")
        self.interdictor = data.get("Interdictor")
        self.is_player = data.get("IsPlayer")
        self.combat_rank = data.get("CombatRank")
        self.faction = data.get("Faction")
        self.power = data.get("Power")


class PVPKill(Base):
    """Logged when a when this player has killed another player."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PVPKill, self).__init__(data)

        self.victim = data.get("Victim")
        self.combat_rank = data.get("CombatRank")


class ShieldState(Base):
    """Logged when a when shields are disabled in combat, or recharged."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ShieldState, self).__init__(data)

        self.shields_up = data.get("ShieldsUp")
