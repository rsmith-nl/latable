Generating LaTeX tables with Python
###################################


Introduction
============

This module was distilled out of the boilerplate code that I've added to
Python scripts to generate LaTeX output.

Version 2 switches from objects to pure functions and a more functional style.

Usage
=====

Create a simple, non-floating table;

.. code-block:: python

    import latable as lt

    colspec = 'lr'
    row = lt.rowfn(colspec)
    print(lt.header(colspec))
    print(row('height', '29.7 cm'))
    print(row('width', '21.0 cm'))
    print(lt.footer())

This produces;

.. code-block:: tex

    \begin{tabular}{lr}
      height & 29.7 cm\\
      width & 21.0 cm\\
    \end{tabular}}

The ``rowfn`` is special in that it returns a specialized function that knows
about the amount of columns. It can raise an exception if too many columns are
used, or it can ignore extra columns.

As an alternative to ``tabular``, a floating ``table`` environment can be used;

.. code-block:: python

    import latable as lt

    colspec = 'lr'
    row = lt.rowfn(colspec)
    print(lt.header(colspec, table=True, caption='A4 paper size',
                    pos='ht', label='a4paper'))
    print(row('height', '29.7 cm'))
    print(row('width', '21.0 cm'))
    print(lt.footer(True))

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
