Generating LaTeX tables with Python
###################################

:date: 2015-05-16
:tags: LaTeX, Python 3
:author: Roland Smith


Introduction
============

This module was distilled out of the boilerplate code that I've added to
Python scripts to generate LaTeX output.


License
=======

To the extent possible under law, Roland Smith has waived all copyright and
related or neighboring rights to latable.py. This work is published from the
Netherlands. See http://creativecommons.org/publicdomain/zero/1.0/


Usage
=====

Create a simple, non-floating table;

.. code-block:: python

    import latable as lt

    t = lt.Tabular('lr')
    t.add_row('height', '29.7 cm')
    t.add_row('width', '21.0 cm')
    print(t)

This produces;

.. code-block:: tex

    {\hspace{-\tabcolsep}\begin{tabular}{lr}
    height & 29.7 cm\\
    width & 21.0 cm\\
    \end{tabular}}

Alternatively, a floating table environment can be used;

.. code-block:: python

    import latable as lt

    t = lt.Table('lr', 'A4 paper size', pos='ht', label='a4paper')
    t.add_row('height', '29.7 cm')
    t.add_row('width', '21.0 cm')
    print(t)

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

.. note:: The ``line`` function will raise a ``ValueError`` if one of its arguments
    contains ``&`` or ``\\``.
