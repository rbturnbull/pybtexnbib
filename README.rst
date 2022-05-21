============
pybtexnbib
============

.. start-badges

|pipline badge| |coverage badge| |black badge| |git3moji badge|

.. |pipline badge| image:: https://github.com/rbturnbull/pybtexnbib/actions/workflows/coverage.yml/badge.svg
    :target: https://github.com/rbturnbull/pybtexnbib/actions
    
.. |coverage badge| image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/rbturnbull/e93cbe3d6bef10cf72db901d962719ba/raw/coverage-badge.json
    :target: https://rbturnbull.github.io/pybtexnbib/

.. |black badge| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    
.. |git3moji badge| image:: https://img.shields.io/badge/git3moji-%E2%9A%A1%EF%B8%8F%F0%9F%90%9B%F0%9F%93%BA%F0%9F%91%AE%F0%9F%94%A4-fffad8.svg
    :target: https://robinpokorny.github.io/git3moji/

.. end-badges

A pybtex plugin for NBIB/Medline/PubMed files. For information on the file format, see the documentation at the `National Library of Medicine <https://www.nlm.nih.gov/bsd/mms/medlineelements.html>`_.

Installation
============

Install pybtexnbib from PyPI using pip::

    pip install pybtexnbib

Command-line usage
==================

To convert an NBIB file to another format, use the ``pybtex-convert`` command. For example::

    pybtex-convert bibliography.nbib bibliography.bib

The extension of the output file must be supported by ``pybtex`` or an associated plugin.

To format an NBIB file into a human-readable bibliography, use the pybtex-format command. For example::

    pybtex-format bibliography.nbib bibliography.txt

For more information, see `the documentation for pybtex <https://docs.pybtex.org/cmdline.html>`_.

Programmatic usage
==================

NBIB files can be formatted into a human-readable bibliography as a string as follows:

.. code-block:: python

    from pybtex import format_from_file
    bibliography_string = format_from_file(
        "path/to/file.nbib", 
        style="plain", 
        output_backend="plaintext",
        bib_format="nbib",
    )

Multiple NBIB files can be formatted in a similar way:

.. code-block:: python

    from pybtex import format_from_files
    bibliography_string = format_from_files(
        ["path/to/file1.nbib", "path/to/file2.nbib"],
        style="plain", 
        output_backend="plaintext",
        bib_format="nbib",
    )

By giving ``"suffix"`` as the argument to ``bib_format``, 
NBIB files can be combined with bibliography files of other formats (such as BibTeX or RIS):

.. code-block:: python

    from pybtex import format_from_files
    bibliography_string = format_from_files(
        ["path/to/file1.nbib", "path/to/file2.bib", "path/to/file3.ris"],
        style="plain", 
        output_backend="plaintext",
        bib_format="suffix",
    )

The RIS parser comes from `pybtexris <https://github.com/rbturnbull/pybtexris>`_. 
Parsers for the files for other formats need to be registered on the ``pybtex.database.input.suffixes``
entry point as discussed pybtex `plugin documentation <https://docs.pybtex.org/api/plugins.html>`_.

For more information on programmatic use of pybtex, 
see `the documentation of the Python API of pybtex <https://docs.pybtex.org/api/index.html>`_.

Credit
==================

Robert Turnbull (Melbourne Data Analytics Platform, University of Melbourne)
