Generating LaTeX tables with Python
###################################

:date: 2015-05-02
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

    t = []
    t.append(lt.sheader('lr'))
    t.append(lt.line('height', '29.7 cm'))
    t.append(lt.line('width', '21.0 cm'))
    t.append(lt.sfooter())
    print('\n'.join(t))

This produces;

.. code-block:: tex

    {\hspace{-\tabcolsep}\begin{tabular}{lr}
      height & 29.7 cm\\
      width & 21.0 cm\\
    \end{tabular}}

Using the ``header`` and ``footer`` produces a floating table;

.. code-block:: python

    import latable as lt

    t = []
    t.append(lt.header('lr', 'A4 paper size', label='a4paper', pos='ht'))
    t.append(lt.line('height', '29.7 cm'))
    t.append(lt.line('width', '21.0 cm'))
    t.append(lt.footer())
    print('\n'.join(t))

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
