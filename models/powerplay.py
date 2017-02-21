"""Describe Powerplay models."""

from .base import BaseModel


class PowerplayCollect(BaseModel):
    """Logged when collecting powerplay commodities for delivery."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PowerplayCollect, self).__init__(data)

        self.power = data.get("Power")
        self.type = data.get("Type")
        self.count = data.get("Count")


class PowerplayDefect(BaseModel):
    """Logged when a player defects from one power to another."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PowerplayDefect, self).__init__(data)

        self.from_power = data.get("FromPower")
        self.to_power = data.get("ToPower")


class PowerplayDeliver(BaseModel):
    """Logged when delivering powerplay commodities."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PowerplayDeliver, self).__init__(data)

        self.power = data.get("Power")
        self.type = data.get("Type")
        self.count = data.get("Count")


class PowerplayFastTrack(BaseModel):
    """Logged when paying to fast-track allocation of commodities."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PowerplayFastTrack, self).__init__(data)

        self.power = data.get("Power")
        self.cost = data.get("Cost")


class PowerplayJoin(BaseModel):
    """Logged when joining up with a power."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PowerplayJoin, self).__init__(data)

        self.power = data.get("Power")


class PowerplayLeave(BaseModel):
    """Logged when leaving a power."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PowerplayLeave, self).__init__(data)

        self.power = data.get("Power")


class PowerplaySalary(BaseModel):
    """Logged when receiving salary payment from a power."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PowerplaySalary, self).__init__(data)

        self.power = data.get("Power")
        self.amount = data.get("Amount")


class PowerplayVote(BaseModel):
    """Logged when voting for a system expansion."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PowerplayVote, self).__init__(data)

        self.power = data.get("Power")
        self.votes = data.get("Votes")
        self.system = data.get("System")


class PowerplayVoucher(BaseModel):
    """Logged when receiving payment for powerplay combat."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(PowerplayVoucher, self).__init__(data)

        self.power = data.get("Power")
        self.systems = data.get("Systems")
