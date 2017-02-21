"""Describes base models."""

import dateutil.parser


class Base(object):
    """Base object from which all other objects inherit."""

    def __str__(self):
        """Return a proper string representation."""
        return "%s %r" % (self.__class__.__name__, self.__dict__)


class BaseModel(Base):
    """Base model from which all other models inherit."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(BaseModel, self).__init__()

        # self._data = data
        self.event = data.get("event")
        if "timestamp" in data:
            self.timestamp = dateutil.parser.parse(data.get("timestamp"))
        else:
            self.timestamp = None


class FileHeader(BaseModel):
    """The first event logged into a file."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(FileHeader, self).__init__(data)

        self.part = data.get("part")
        self.language = data.get("language")
        self.game_version = data.get("gameversion")
        self.build = data.get("build")
