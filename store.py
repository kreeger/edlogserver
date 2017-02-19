"""Handles all data storage needs for importing JSON models."""

import models


class Store:
    """Handles all data storage needs for importing JSON models."""

    def __init__(self, loader):
        """Create an instance of this store with a loader object."""
        self.loader = loader
        self.models = []

    def import_data(self):
        """Import all model data using the loader."""
        self.models = [self.type_for(o)(o) for o in self.loader.load()]
        return self.models

    @staticmethod
    def type_for(data):
        """Return the class type to be used for a given event name."""
        switcher = {
            # Startup
            "FileHeader": models.FileHeader,
            "ClearSavedGame": models.ClearSavedGame,
            "NewCommander": models.NewCommander,
            "LoadGame": models.LoadGame,
            "Progress": models.Progress,
            "Rank": models.Rank,
            # Travel
            "Docked": models.Docked,
            "DockingCancelled": models.DockingCancelled,
            "DockingDenied": models.DockingDenied,
            "DockingGranted": models.DockingGranted,
            "DockingRequested": models.DockingRequested,
            "DockingTimeout": models.DockingTimeout,
            "FSDJump": models.FSDJump,
            "Liftoff": models.Liftoff,
            "Location": models.Location,
            "SupercruiseEntry": models.SupercruiseEntry,
            "SupercruiseExit": models.SupercruiseExit,
            "Touchdown": models.Touchdown,
            "Undocked": models.Undocked,
            # Combat
            "Bounty": models.Bounty,
            "CapShipBond": models.CapShipBond,
            "Died": models.Died,
            "EscapeInterdiction": models.EscapeInterdiction,
            "FactionKillBond": models.FactionKillBond,
            "HeatDamage": models.HeatDamage,
            "HeatWarning": models.HeatWarning,
            "HullDamage": models.HullDamage,
            "Interdicted": models.Interdicted,
            "Interdiction": models.Interdiction,
            "PVPKill": models.PVPKill,
            "ShieldState": models.ShieldState,
            # Exploration
            "Scan": models.Scan,
            "MaterialCollected": models.MaterialCollected,
            "MaterialDiscarded": models.MaterialDiscarded,
            "MaterialDiscovered": models.MaterialDiscovered,
            "BuyExplorationData": models.BuyExplorationData,
            "SellExplorationData": models.SellExplorationData,
            "Screenshot": models.Screenshot,
            # Trade
            "BuyTradeData": models.BuyTradeData,
            "CollectCargo": models.CollectCargo,
            "EjectCargo": models.EjectCargo,
            "MarketBuy": models.MarketBuy,
            "MarketSell": models.MarketSell,
            "MiningRefined": models.MiningRefined,
            # Station Services
            "BuyAmmo": models.BuyAmmo,
            "BuyDrones": models.BuyDrones,
            "CommunityGoalDiscard": models.CommunityGoalDiscard,
            "CommunityGoalJoin": models.CommunityGoalJoin,
            "CommunityGoalReward": models.CommunityGoalReward,
            "CrewAssign": models.CrewAssign,
            "CrewFire": models.CrewFire,
            "CrewHire": models.CrewHire,
            "EngineerApply": models.EngineerApply,
            "EngineerCraft": models.EngineerCraft,
            "EngineerProgress": models.EngineerProgress,
            "FetchRemoteModule": models.FetchRemoteModule,
            "MassModuleStore": models.MassModuleStore,
            "MissionAbandoned": models.MissionAbandoned,
            "MissionAccepted": models.MissionAccepted,
            "MissionCompleted": models.MissionCompleted,
            "MissionFailed": models.MissionFailed,
            "ModuleBuy": models.ModuleBuy,
            "ModuleRetrieve": models.ModuleRetrieve,
            "ModuleSell": models.ModuleSell,
            "ModuleSellRemote": models.ModuleSellRemote,
            "ModuleStore": models.ModuleStore,
            "ModuleSwap": models.ModuleSwap,
            "PayFines": models.PayFines,
            "PayLegacyFines": models.PayLegacyFines,
            "RedeemVoucher": models.RedeemVoucher,
            "RefuelAll": models.RefuelAll,
            "RefuelPartial": models.RefuelPartial,
            "Repair": models.Repair,
            "RepairAll": models.RepairAll,
            "RestockVehicle": models.RestockVehicle,
            "ScientificResearch": models.ScientificResearch,
            "SellDrones": models.SellDrones,
            "ShipyardBuy": models.ShipyardBuy,
            "ShipyardNew": models.ShipyardNew,
            "ShipyardSell": models.ShipyardSell,
            "ShipyardTransfer": models.ShipyardTransfer,
            "ShipyardSwap": models.ShipyardSwap,
            # Powerplay
            "PowerplayCollect": models.PowerplayCollect,
            "PowerplayDefect": models.PowerplayDefect,
            "PowerplayDeliver": models.PowerplayDeliver,
            "PowerplayFastTrack": models.PowerplayFastTrack,
            "PowerplayJoin": models.PowerplayJoin,
            "PowerplayLeave": models.PowerplayLeave,
            "PowerplaySalary": models.PowerplaySalary,
            "PowerplayVote": models.PowerplayVote,
            "PowerplayVoucher": models.PowerplayVoucher,
            # Other Events
            "ApproachSettlement": models.ApproachSettlement,
            "CockpitBreached": models.CockpitBreached,
            "CommitCrime": models.CommitCrime,
            "Continued": models.Continued,
            "DatalinkScan": models.DatalinkScan,
            "DatalinkVoucher": models.DatalinkVoucher,
            "DataScanned": models.DataScanned,
            "DockFighter": models.DockFighter,
            "DockSRV": models.DockSRV,
            "FuelScoop": models.FuelScoop,
            "JetConeBoost": models.JetConeBoost,
            "JetConeDamage": models.JetConeDamage,
            "LaunchFighter": models.LaunchFighter,
            "LaunchSRV": models.LaunchSRV,
            "Promotion": models.Promotion,
            "RebootRepair": models.RebootRepair,
            "ReceiveText": models.ReceiveText,
            "Resurrect": models.Resurrect,
            "SelfDestruct": models.SelfDestruct,
            "SendText": models.SendText,
            "Synthesis": models.Synthesis,
            "USSDrop": models.USSDrop,
            "VehicleSwitch": models.VehicleSwitch,
            "WingAdd": models.WingAdd,
            "WingJoin": models.WingJoin,
            "WingLeave": models.WingLeave,
        }
        return switcher.get(data["event"], models.Base)
