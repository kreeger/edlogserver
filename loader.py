#!/usr/bin/env python

import json
from os import walk, path


class Loader:
    def __init__(self, directory, parser_cls):
        self._parser_cls = parser_cls
        self.filepaths = self._get_files(directory)

    def load(self):
        dicts = []
        for filepath in self.filepaths:
            parser = self._parser_cls(filepath)
            dicts.extend(parser.data)
        return dicts

    def _get_files(self, directory):
        all_files = []

        for (dirpath, dirnames, filenames) in walk(directory):
            real_path = path.realpath(dirpath)

            for dirname in dirnames:
                files = self._get_files(dirname)
                all_files.extend(files)

            for filename in [f for f in filenames if not f.startswith(".")]:
                all_files.append(path.join(real_path, filename))

        return all_files
