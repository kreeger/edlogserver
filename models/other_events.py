"""Describes models used for explaining other events."""

from .base import Base


class ApproachSettlement(Base):
    """Logged when approaching a planetary settlement."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ApproachSettlement, self).__init__(data)

        self.name = data.get("Name")


class CockpitBreached(Base):
    """Logged when cockpit canopy is breached."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(CockpitBreached, self).__init__(data)


class CommitCrime(Base):
    """Logged when a crime is recorded against the player."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(CommitCrime, self).__init__(data)

        self.crime_type = data.get("CrimeType")  # - see 11.6
        self.faction = data.get("Faction")

        # Optional parameters (depending on crime)
        self.victim = data.get("Victim")
        self.fine = data.get("Fine")
        self.bounty = data.get("Bounty")


class Continued(Base):
    """Logged when the journal file grows to 500k lines.

    When this happens, we write this event, close the file, and start a new
    one.
    """

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Continued, self).__init__(data)

        self.next_part_number = data.get("Part")


class DatalinkScan(Base):
    """Logged when scanning a data link."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(DatalinkScan, self).__init__(data)

        self.message = data.get("Message")


class DatalinkVoucher(Base):
    """Logged when scanning a datalink generates a reward."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(DatalinkVoucher, self).__init__(data)

        self.reward = data.get("Reward")
        self.victim_faction = data.get("VictimFaction")
        self.payee_faction = data.get("PayeeFaction")


class DataScanned(Base):
    """Logged when scanning some types of data links."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(DataScanned, self).__init__(data)

        # Type will typically be one of "DataLink", "DataPoint",
        #   "ListeningPost", "AbandonedDataLog", "WreckedShip", etc
        self.type = data.get("Type")


class DockFighter(Base):
    """Logged when docking a fighter back with the mothership."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(DockFighter, self).__init__(data)


class DockSRV(Base):
    """Logged when docking an SRV with the ship."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(DockSRV, self).__init__(data)


class FuelScoop(Base):
    """Logged when scooping fuel from a star."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(FuelScoop, self).__init__(data)

        self.scooped = data.get("Scooped")
        self.total = data.get("Total")


class JetConeBoost(Base):
    """Logged when enough material has been collected for an FSD boost.

    These are collected from a solar jet code (at a white dwarf or neutron
    star).
    """

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(JetConeBoost, self).__init__(data)

        self.boost_value = data.get("BoostValue")


class JetConeDamage(Base):
    """Logged when receiving damage from passing through a jet cone."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(JetConeDamage, self).__init__(data)

        self.module = data.get("Module")


class LaunchFighter(Base):
    """Logged when launching a fighter."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(LaunchFighter, self).__init__(data)

        self.loadout = data.get("Loadout")
        self.player_controlled = data.get("PlayerControlled")


class LaunchSRV(Base):
    """Logged deploying the SRV from a ship onto planet surface."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(LaunchSRV, self).__init__(data)

        self.loadout = data.get("Loadout")


class Promotion(Base):
    """Logged when the player's rank increases."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Promotion, self).__init__(data)

        self.combat = data.get("Combat")
        self.trade = data.get("Trade")
        self.explore = data.get("Explore")
        self.cqc = data.get("CQC")


class RebootRepair(Base):
    """Logged when the 'reboot repair' function is used."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(RebootRepair, self).__init__(data)

        self.modules = data.get("Modules")


class ReceiveText(Base):
    """Logged when a text message is received from another player or NPC."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ReceiveText, self).__init__(data)

        self.from_cmdr = data.get("From")
        self.message = data.get("Message")
        # wing/local/voicechat/friend/player/npc
        self.channel = data.get("Channel")


class Resurrect(Base):
    """Logged when the player restarts after death."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Resurrect, self).__init__(data)

        self.option = data.get("Option")
        self.cost = data.get("Cost")
        self.bankrupt = data.get("Bankrupt")


class SelfDestruct(Base):
    """Logged when the 'self destruct' function is used."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(SelfDestruct, self).__init__(data)


class SendText(Base):
    """Logged when a text message is sent to another player."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(SendText, self).__init__(data)

        self.to_cmdr = data.get("To")
        self.message = data.get("Message")


class Synthesis(Base):
    """Logged when synthesis is used to repair or rearm."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Synthesis, self).__init__(data)

        self.name = data.get("Name")
        self.materials = data.get("Materials")  # name - key, quant - value


class USSDrop(Base):
    """Logged when dropping from Supercruise at a USS."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(USSDrop, self).__init__(data)

        self.type = data.get("USSType")
        self.threat_level = data.get("USSThreat")


class VehicleSwitch(Base):
    """Logged when switching control between the main ship and a fighter."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(VehicleSwitch, self).__init__(data)

        self.to_vehicle = data.get("To")


class WingAdd(Base):
    """Logged when another player has joined the wing."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(WingAdd, self).__init__(data)

        self.name = data.get("Name")


class WingJoin(Base):
    """Logged when this player has joined a wing."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(WingJoin, self).__init__(data)

        self.others = data.get("Others")


class WingLeave(Base):
    """Logged when this player has left a wing."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(WingLeave, self).__init__(data)
