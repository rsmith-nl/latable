# file: latable.py
# vim:fileencoding=utf-8:ft=python
#
# Copyright © 2012,2013,2015 R.F. Smith <rsmith@xs4all.nl>.
# All rights reserved.
# Created: 2012-05-19 15:51:09 +0200
# Last modified: 2015-09-20 16:47:52 +0200
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY AUTHOR AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN
# NO EVENT SHALL AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Generate LaTeX tables from Python."""

__version__ = '0.3.2'


class Tabular(object):
    """Simple tabular environment for LaTeX. Aligns the left of the table with
    the left of the text block."""

    def __init__(self, columns):
        """
        Create a LaTeX tabular environment. It is not a bare table, but the
        first column is aligned with the surroundings by moving it to the left
        by tabcolsep.

        Arguments:
            columns: A string containing the specification for the columns.
        """
        self.header = r'{\hspace{-\tabcolsep}\begin{tabular}{' + columns + r'}'
        self.rows = []
        self.footer = r'\end{tabular}}'

    def add_row(self, *args):
        r"""
        Add a row to the table.

        Arguments:
            args: Every argument forms a column of the table. Note that the
                arguments cannot contain '&' or '\\'. Currently this does not
                check that the amount of arguments matches with the columns
                specfication given in the init method.
        """
        rs = '  '
        sep = r' & '
        illegal = ('&', r'\\')
        es = "argument should not contain '{}'"
        for n in args:
            for symbol in illegal:
                if symbol in n:
                    raise ValueError(es.format(symbol))
            rs += str(n)+sep
        rs = rs[:-len(sep)] + r'\\'
        self.rows.append(rs)

    def __str__(self):
        """
        Return the string rendering of the environment.
        """
        table = [self.header] + self.rows + [self.footer]
        return '\n'.join(table)


class Table(Tabular):

    def __init__(self, columns, caption, pos='!htbp', label=None):
        """Create a LaTeX table float.

        Arugments:
            columns: The columns of the table, e.g. 'lcr'
            caption: The caption of the table.
            pos: Indicates the position of the float on the page. Defaults to
                '!htbp'.
            label: Optional label for the table.
        """
        Tabular.__init__(self, columns)
        rs = r'\begin{table}[' + pos + ']\n'
        rs += '  \\centering\n'
        if label:
            rs += r'  \caption{\label{tb:' + str(label) + '}' + caption + \
                '}\n'
        else:
            rs += r'  \caption{' + caption + '}\n'
        rs += r'  \begin{tabular}{' + columns + '}'
        self.header = rs
        self.footer = r'  \end{tabular}' + '\n' + r'\end{table}'
