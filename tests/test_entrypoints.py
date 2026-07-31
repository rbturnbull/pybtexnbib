from importlib.metadata import entry_points

from pybtexnbib import NBIBParser


def get_entry_points(group):
    discovered = entry_points()
    if hasattr(discovered, "select"):
        return discovered.select(group=group)
    return discovered.get(group, ())


def test_database_input():
    hook = "pybtex.database.input"
    nbib_entry_points = [entry_point for entry_point in get_entry_points(hook) if entry_point.name == "nbib"]

    assert len(nbib_entry_points) == 1
    assert nbib_entry_points[0].load() == NBIBParser


def test_database_input_suffixes():
    hook = "pybtex.database.input.suffixes"
    nbib_entry_points = [entry_point for entry_point in get_entry_points(hook) if entry_point.name == ".nbib"]

    assert len(nbib_entry_points) == 1
    assert nbib_entry_points[0].load() == NBIBParser
