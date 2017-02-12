"""Describes station services models."""

from .base import Base


class BuyAmmo(Base):
    """Logged when purchasing ammunition."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(BuyAmmo, self).__init__(data)

        self.cost = data.get("Cost")


class BuyDrones(Base):
    """Logged when purchasing drones."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(BuyDrones, self).__init__(data)

        self.type = data.get("Type")
        self.count = data.get("Count")
        self.buy_price = data.get("BuyPrice")
        self.total_cost = data.get("TotalCost")


class CommunityGoalDiscard(Base):
    """Logged when opting out of a community goal."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(CommunityGoalDiscard, self).__init__(data)

        self.name = data.get("Name")
        self.system = data.get("System")


class CommunityGoalJoin(Base):
    """Logged when signing up to a community goal."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(CommunityGoalJoin, self).__init__(data)

        self.name = data.get("Name")
        self.system = data.get("System")


class CommunityGoalReward(Base):
    """Logged when receiving a reward for a community goal."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(CommunityGoalReward, self).__init__(data)

        self.name = data.get("Name")
        self.system = data.get("System")
        self.reward = data.get("Reward")


class CrewAssign(Base):
    """Logged when changing the task assignment of a member of crew."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(CrewAssign, self).__init__(data)

        self.name = data.get("Name")
        self.role = data.get("Role")


class CrewFire(Base):
    """Logged when dismissing a member of crew."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(CrewFire, self).__init__(data)

        self.name = data.get("Name")


class CrewHire(Base):
    """Logged when engaging a new member of crew."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(CrewHire, self).__init__(data)

        self.name = data.get("Name")
        self.faction = data.get("Faction")
        self.cost = data.get("Cost")
        self.combat_rank = data.get("CombatRank")


class EngineerApply(Base):
    """Logged when applying an engineer's upgrade to a module."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(EngineerApply, self).__init__(data)

        self.engineer_name = data.get("Engineer")
        self.blueprint = data.get("Blueprint")
        self.level = data.get("Level")
        self.override = data.get("Override")


class EngineerCraft(Base):
    """Logged when requesting an engineer upgrade."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(EngineerCraft, self).__init__(data)

        self.engineer = data.get("Engineer")
        self.blueprint = data.get("Blueprint")
        self.level = data.get("Level")
        self.ingredients = data.get("Ingredients")


class EngineerProgress(Base):
    """Logged when a player increases their access to an engineer."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(EngineerProgress, self).__init__(data)
        self.engineer = data.get("Engineer")
        self.rank = data.get("Rank")
        # Invited/Acquainted/Unlocked/Barred
        self.progress = data.get("Progress")


class FetchRemoteModule(Base):
    """Logged when requesting a module from storage at another station."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(FetchRemoteModule, self).__init__(data)

        self.storage_slot = data.get("StorageSlot")
        self.stored_item = data.get("StoredItem")
        self.server_id = data.get("ServerId")
        self.transfer_cost = data.get("TransferCost")
        self.ship = data.get("Ship")
        self.shipId = data.get("ShipId")


class MassModuleStore(Base):
    """Logged when putting multiple modules into storage."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MassModuleStore, self).__init__(data)

        self.ship = data.get("Ship")
        self.ship_id = data.get("ShipId")

        # TODO: Parse into MassModuleStoreItem instances
        self.items = data.get("Items")


class MassModuleStoreItem(Base):
    """An individual entry in a MassModuleStore record."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MassModuleStoreItem, self).__init__(data)

        self.slot = data.get("Slot")
        self.name = data.get("Name")
        self.engineer_modifications = data.get("EngineerModifications")


class MissionAbandoned(Base):
    """Logged when a mission has been abandoned."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MissionAbandoned, self).__init__(data)

        self.name = data.get("Name")
        self.mission_id = data.get("MissionID")


class MissionAccepted(Base):
    """Logged when starting a mission."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MissionAccepted, self).__init__(data)

        self.name = data.get("Name")
        self.faction = data.get("Faction")
        self.mission_id = data.get("MissionID")

        # Optional Parameters (depending on mission type)
        self.commodity = data.get("Commodity")
        self.count = data.get("Count")
        self.target = data.get("Target")
        self.target_type = data.get("TargetType")
        self.target_faction = data.get("TargetFaction")
        self.expiry = data.get("Expiry")
        self.destination_system = data.get("DestinationSystem")
        self.destination_station = data.get("DestinationStation")
        self.passenger_count = data.get("PassengerCount")
        self.passenger_vips = data.get("PassengerVIPs")
        self.passenger_wanted = data.get("PassengerWanted")
        self.passenger_type = data.get("PassengerType")


class MissionCompleted(Base):
    """Logged when a mission is completed."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MissionCompleted, self).__init__(data)

        self.name = data.get("Name")
        self.faction = data.get("Faction")
        self.mission_id = data.get("MissionID")

        # Optional parameters (depending on mission type)
        self.commodity = data.get("Commodity")
        self.count = data.get("Count")
        self.target = data.get("Target")
        self.target_type = data.get("TargetType")
        self.target_faction = data.get("TargetFaction")
        self.reward = data.get("Reward")
        self.donation = data.get("Donation")
        self.permits_awarded = data.get("PermitsAwarded")
        self.commodity_reward = data.get("CommodityReward")  # name, count


class MissionFailed(Base):
    """Logged when a mission has failed."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(MissionFailed, self).__init__(data)

        self.name = data.get("Name")
        self.mission_id = data.get("MissionID")


class ModuleBuy(Base):
    """Logged when buying a module in outfitting."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ModuleBuy, self).__init__(data)

        self.slot = data.get("Slot")
        self.buy_item = data.get("BuyItem")
        self.buy_price = data.get("BuyPrice")
        self.ship = data.get("Ship")
        self.ship_id = data.get("ShipID")
        # If replacing an existing module:
        self.sell_item = data.get("SellItem")
        self.sell_price = data.get("SellPrice")


class ModuleRetrieve(Base):
    """Logged when fetching a previously stored module."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ModuleRetrieve, self).__init__(data)

        self.slot = data.get("Slot")
        self.ship = data.get("Ship")
        self.ship_id
        self.retrieved_item = data.get("RetrievedItem")
        self.engineer_modifications = data.get("EngineerModifications")
        self.swap_out_item = data.get("SwapOutItem")
        self.cost = data.get("Cost")


class ModuleSell(Base):
    """Logged when selling a module in outfitting."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ModuleSell, self).__init__(data)

        self.slot = data.get("Slot")
        self.sell_item = data.get("SellItem")
        self.sell_price = data.get("SellPrice")
        self.ship = data.get("Ship")
        self.ship_id = data.get("ShipID")


class ModuleSellRemote(Base):
    """Logged when selling a module in storage at another station."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ModuleSellRemote, self).__init__(data)

        self.storage_slot = data.get("StorageSlot")
        self.sell_item = data.get("SellItem")
        self.server_id = data.get("ServerId")
        self.sell_price = data.get("SellPrice")
        self.ship = data.get("Ship")
        self.ship_id = data.get("ShipId")


class ModuleStore(Base):
    """Logged when storing a module in Outfitting."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ModuleStore, self).__init__(data)

        self.slot = data.get("Slot")
        self.ship = data.get("Ship")
        self.ship_id = data.get("ShipID")
        self.stored_item = data.get("StoredItem")
        self.engineer_modifications = data.get("EngineerModifications")
        self.replacement_item = data.get("ReplacementItem")
        self.cost = data.get("Cost")


class ModuleSwap(Base):
    """Logged when moving a module to a different slot on the ship."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ModuleSwap, self).__init__(data)

        self.from_slot = data.get("FromSlot")
        self.to_slot = data.get("ToSlot")
        self.from_item = data.get("FromItem")
        self.to_item = data.get("ToItem")
        self.ship = data.get("Ship")
        self.ship_id = data.get("ShipID")


class PayFines(Base):
    """Logged when paying fines."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PayFines, self).__init__(data)

        self.amount = data.get("Amount")
        self.broker_percentage = data.get("BrokerPercentage")


class PayLegacyFines(Base):
    """Logged when paying legacy fines."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PayLegacyFines, self).__init__(data)

        self.amount = data.get("Amount")
        self.broker_percentage = data.get("BrokerPercentage")


class RedeemVoucher(Base):
    """Logged when claiming payment for combat bounties and bonds."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(RedeemVoucher, self).__init__(data)

        self.type = data.get("Type")  # bounty, bond
        self.amount = data.get("Amount")
        self.broker_percentage = data.get("BrokerPercentage")


class RefuelAll(Base):
    """Logged when doing a full-tank refuel."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(RefuelAll, self).__init__(data)

        self.cost = data.get("Cost")
        self.amount = data.get("Amount")


class RefuelPartial(Base):
    """Logged when doing a partial tank refuel."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(RefuelPartial, self).__init__(data)

        self.cost = data.get("Cost")
        self.amount = data.get("Amount")


class Repair(Base):
    """Logged when repairing the ship."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(Repair, self).__init__(data)

        self.item = data.get("Item")
        self.cost = data.get("Cost")


class RepairAll(Base):
    """Logged when repairing everything."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(RepairAll, self).__init__(data)

        self.cost = data.get("Cost")


class RestockVehicle(Base):
    """Logged when purchasing an SRV or Fighter."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(RestockVehicle, self).__init__(data)

        self.type = data.get("Type")
        self.loadout = data.get("Loadout")
        self.cost = data.get("Cost")
        self.count = data.get("Count")


class ScientificResearch(Base):
    """Logged when contributing materials to a "research" community goal."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ScientificResearch, self).__init__(data)

        self.name = data.get("Name")
        self.category = data.get("Category")
        self.count = data.get("Count")


class SellDrones(Base):
    """Logged when selling unwanted drones back to the market."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(SellDrones, self).__init__(data)

        self.type = data.get("Type")
        self.count = data.get("Count")
        self.sell_price = data.get("SellPrice")
        self.total_sale = data.get("TotalSale")


class ShipyardBuy(Base):
    """Logged when buying a new ship in the shipyard.

    Note that the new ship's ShipID will be logged in a separate event after
    the purchase.
    """

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ShipyardBuy, self).__init__(data)

        self.ship_type = data.get("ShipType")
        self.ship_price = data.get("ShipPrice")
        self.store_old_ship = data.get("StoreOldShip")
        self.store_ship_id = data.get("StoreShipID")
        self.sell_old_ship = data.get("SellOldShip")
        self.sell_ship_id = data.get("SellShipID")
        self.sell_price = data.get("SellPrice")


class ShipyardNew(Base):
    """Logged after a new ship has been purchased."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ShipyardNew, self).__init__(data)

        self.ship_type = data.get("ShipType")
        self.ship_id = data.get("ShipID")


class ShipyardSell(Base):
    """Logged when selling a ship stored in the shipyard."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ShipyardSell, self).__init__(data)

        self.ship_type = data.get("ShipType")
        self.sell_ship_id = data.get("SellShipID")
        self.ship_price = data.get("ShipPrice")
        self.system = data.get("System")


class ShipyardTransfer(Base):
    """Logged when requesting a ship be transported to this station."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ShipyardTransfer, self).__init__(data)

        self.ship_type = data.get("ShipType")
        self.ship_id = data.get("ShipID")
        self.system = data.get("System")
        self.distance = data.get("Distance")
        self.transfer_price = data.get("TransferPrice")


class ShipyardSwap(Base):
    """Logged when switching to another ship already stored at this station."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(ShipyardSwap, self).__init__(data)

        self.ship_type = data.get("ShipType")
        self.ship_id = data.get("ShipID")
        self.store_old_ship = data.get("StoreOldShip")
        self.store_ship_id = data.get("StoreShipID")
        self.sell_old_ship = data.get("SellOldShip")
        self.sell_ship_id = data.get("SellShipID")
