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

Copyright © 2012,2013,2015 R.F. Smith <rsmith@xs4all.nl>.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

  1. Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
  2. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY AUTHOR AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN
NO EVENT SHALL AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


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
