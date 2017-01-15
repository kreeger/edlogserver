#!/usr/bin/env python

import json


class Parser:
    def __init__(self, filepath):
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
