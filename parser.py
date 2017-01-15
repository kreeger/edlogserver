#!/usr/bin/env python

import json


class Parser:
    def __init__(self, filepath):
        self.data = self.__parse(filepath)

    def __parse(self, filepath):
        lines = []

        with open(filepath, "r") as f:
            for line in f:
                cleaned = line.strip()
                if cleaned:
                    lines.append(cleaned)

        json_data = "[%s]" % ",".join(lines)

        events = json.loads(json_data)
        for event_dict in events:
            print(event_dict)
        return events
