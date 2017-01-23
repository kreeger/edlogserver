"""Describes base models."""

import dateutil.parser


class Base(object):
    """Base model from which all other models inherit."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        if data.get("timestamp"):
            self.timestamp = dateutil.parser.parse(data.get("timestamp"))
        else:
            self.timestamp = None
        self.event = data.get("event")

    def __str__(self):
        """Return a proper string representation."""
        return "%s %r" % (self.__class__.__name__, self.__dict__)


class FileHeader(Base):
    """The first event logged into a file."""

    def __init__(self, data):
        """Initialize and return an instance with an API data dictionary."""
        super(FileHeader, self).__init__(data)

        self.part = data.get("part")
        self.language = data.get("language")
        self.game_version = data.get("gameversion")
        self.build = data.get("build")
