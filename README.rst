Generating LaTeX tables with Python
###################################


Introduction
============

This module was distilled out of the boilerplate code that I've added to
Python scripts to generate LaTeX output.

Version 2 switches from objects to pure functions.

Usage
=====

Create a simple, non-floating table;

.. code-block:: python

    import latable as lt

    colspec = 'lr'
    print(lt.header(colspec))
    print(lt.row(colspec, 'height', '29.7 cm'))
    print(lt.row(colspec, 'width', '21.0 cm'))
    print(lt.footer())

This produces;

.. code-block:: tex

    \begin{tabular}{lr}
    height & 29.7 cm\\
    width & 21.0 cm\\
    \end{tabular}}

Alternatively, a floating table environment can be used;

.. code-block:: python

    import latable as lt

    colspec = 'lr'
    print(lt.header(colspec, table=True, caption='A4 paper size',
                    pos='ht', label='a4paper'))
    print(lt.row(colspec, 'height', '29.7 cm'))
    print(lt.row(colspec, 'width', '21.0 cm'))
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


.. note:: The ``row`` function will raise a ``ValueError`` if one of its arguments
    contains ``&`` or ``\\``.
