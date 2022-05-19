import pkg_resources
from pybtexnbib import NBIBParser

def test_database_input():
    hook = "pybtex.database.input"
    nbib_entry_points = []
    for entry_point in pkg_resources.iter_entry_points(hook):
        if entry_point.name == "nbib":
            nbib_entry_points.append(entry_point)

    assert len(nbib_entry_points) == 1
    assert nbib_entry_points[0].load() == NBIBParser

def test_database_input_suffixes():
    hook = "pybtex.database.input.suffixes"
    nbib_entry_points = []
    for entry_point in pkg_resources.iter_entry_points(hook):
        if entry_point.name == ".nbib":
            nbib_entry_points.append(entry_point)

    assert len(nbib_entry_points) == 1
    assert nbib_entry_points[0].load() == NBIBParser
