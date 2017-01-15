#!/usr/bin/env python

from .base import Base


class FileHeader(Base):
    def part(self):
        return self._part

    def language(self):
        return self._language

    def game_version(self):
        return self._gameversion

    def build(self):
        return self._build
