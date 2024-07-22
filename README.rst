Generating LaTeX tables with Python
###################################


Introduction
============

This module was distilled out of the boilerplate code that I've added to
Python scripts to generate LaTeX output.

Version 2 switches from objects to pure functions and a more functional style.
Version 3 was then further simplified.
After 3.1 I switched to a date-based versioning system, 2019.07.


Installation
============

This module has no requirements outside the standard library.
The installation uses  ``build`` and ``flit_core``.

On some systems, python 3 is installed as ``python3``. On others, it's
installed as just ``python``. Adapt the following commands accordingly.

First, create a wheel::

    > python3 -m build -n -w

Installing it for the local user is the preferred method, since this doesn't
require root/administrator privileges.
To install it for the local user::

    > python3 -m pip install --user dist/*.whl

To install it system-wide (requires root privileges)::

    # python3 -m pip install dist/*.whl

To remove the installation (require root privileges in case of a system-wide
installation)::

    python3 -m pip uninstall latable


Usage
=====

Create a simple, non-floating table;

.. code-block:: python

    import latable as lt

    header, row, footer = lt.prepare('lr')
    print(header)
    print(row('height', '29.7 cm'))
    print(row('width', '21.0 cm'))
    print(footer)

This produces;

.. code-block:: tex

    \begin{tabular}{lr}
      height & 29.7 cm\\
      width & 21.0 cm\\
    \end{tabular}

The ``row`` is a specialized function that knows about the amount of columns.
It can raise an exception if too many columns are used, or it can ignore extra
columns.

As an alternative to ``tabular``, a floating ``table`` environment can be used;

.. code-block:: python

    import latable as lt

    header, row, footer = lt.prepare('lr', table=True, caption='A4 paper size',
                                     pos='ht', label='a4paper')
    print(header)
    print(row('height', '29.7 cm'))
    print(row('width', '21.0 cm'))
    print(footer)

This produces;

.. code-block:: tex

    \begin{table}[ht]
      \centering
      \caption{\label{tb:a4paper}A4 paper size}
      \begin{tabular}{lr}
        height & 29.7 cm\\
        width & 21.0 cm\\
      \end{tabular}
    \end{table}

.. note:: The generated ``row`` function will raise a ``ValueError`` if one of its
    arguments contains ``&`` or ``\\``. Additionally an ``IndexError`` is raised if it
    contains more column arguments than the column specification allows.
    Unless the argument ``ignore=True`` is supplied to ``prepare``, in which
    case extra columns will be ignored.


Tests
=====

py.test
-------

The code comes with functional tests. Running those requires pytest_.

.. _pytest: https://docs.pytest.org/en/latest/

Running the tests is done from the package's root directory like this.

.. code-block:: console

   pytest-3.7 -v tests/

Adjust this to suit your pytest installation.

pylama
------

Code checking is done with pylama_.

.. _pylama: https://github.com/klen/pylama

In Python 3.7 pylama gives an annoying FutureWarning in pydocstyle. So
I explicitly ignore that by running the command from the package's root
directory like this.

.. code-block:: console

   env PYTHONWARNINGS=ignore::FutureWarning pylama -i E501 latable.py tests/*.py
