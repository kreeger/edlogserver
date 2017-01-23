"""Describes classes used when converting JSON strings into dictionaries."""

import json


class JSONParser:
    """Loading up JSON strings and converting them into dictionaries."""

    def __init__(self, filepath):
        """Initialize and return an instance given a path to a JSON file."""
        self.data = self._parse(filepath)

    def _parse(self, filepath):
        lines = []

        with open(filepath, "r") as f:
            for line in f:
                cleaned = line.strip()
                if cleaned:
                    lines.append(cleaned)

        json_data = "[%s]" % ",".join(lines)
        loaded = json.loads(json_data)
        return loaded
