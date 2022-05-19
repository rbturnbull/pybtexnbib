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

A pybtex plugin for inputting NBIB files. The format used by `PubMed <https://www.nlm.nih.gov/bsd/mms/medlineelements.html>`_.

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

Credit
==================

Robert Turnbull (Melbourne Data Analytics Platform, University of Melbourne)

I have also created `pybtexris <https://github.com/rbturnbull/pybtexris>`_ to handle RIS files.