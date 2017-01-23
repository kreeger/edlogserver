"""Describes classes used to load up JSON files from disk and parse them."""

from os import walk, path


class Loader:
    """Handles reading JSON files and parsing them with a given class."""

    def __init__(self, directory, parser_cls):
        """
        Init and return an instance of this class.

        Takes a directory where log files are stored, and the name of a class
        to use when parsing all of the log files.
        """
        self._parser_cls = parser_cls
        self.filepaths = self._get_files(directory)

    def load(self):
        """Execute a load-and-parse operation."""
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
