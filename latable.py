# file: latable.py
# vim:fileencoding=utf-8:ft=python:fdm=indent
#
# Copyright © 2012,2013,2015-2017 R.F. Smith <rsmith@xs4all.nl>.
# All rights reserved.
# Created: 2012-05-19 15:51:09 +0200
# Last modified: 2017-02-04 15:13:53 +0100
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

import re

__version__ = '1.1.0'


class Tabular(object):
    """Simple LaTeX tabular generator."""

    def __init__(self, columns, toprule=False, bottomrule=False):
        """
        Create a LaTeX tabular environment.

        Arguments:
            columns: A string containing the specification for the columns.
                This string is scanned for the ‘l’, ‘c’, ‘r’ and ‘p’
                specifiers. The ‘*’ specifier is *not* handled.
            toprule: Print a horizontal rule at the top of the table.
            bottomrule: Print a horizontal rule at the bottom of the table.
        """
        self.header = r'\begin{tabular}{' + columns + r'}'
        # Find the number of columns. Note that this does *not* handle *{}{}!
        self.numcols = len(re.findall('l|c|r|p{.*?}', columns))
        self.rows = []
        self.footer = r'\end{tabular}'
        self.toprule = toprule
        self.bottomrule = bottomrule

    def row(self, *args):
        r"""Add a row to the table.

        Arguments:
            args: Every argument forms a column of the table. Note that the
                arguments cannot contain '\\'. The amount of arguments
                should not exceed ‘self.numcols’, and it should be less if the
                arguments contain '&'

        Raises:
            ValueError: If any of the arguments contain '\\' or if the row
                contains too many '&'.
            IndexError: When more than ‘self.numcols’ arguments are supplied.
        """
        if len(args) > self.numcols:
            raise IndexError('too many columns specified')
        content = '  ' + r' & '.join(args) + r'\\'
        if r'\\' in ' '.join(args):
            raise ValueError("arguments should not contain \\\\.")
        if content.count('&') > self.numcols-1:
            raise ValueError("Too many '&'")
        self.rows.append('  ' + r' & '.join(args) + r'\\')

    def midrule(self):
        r"""Add a \midrule to the table."""
        self.rows.append(r'  \midrule')

    def __str__(self):
        """
        Return the string rendering of the environment.
        """
        table = [self.header]
        if self.toprule:
            table += [r'  \toprule']
        table += self.rows
        if self.toprule:
            table += [r'  \bottomrule']
        table += [self.footer]
        return '\n'.join(table)


class Table(Tabular):
    """Floating LaTeX table generator."""

    def __init__(self, columns, caption, pos='!htbp', label=None,
                 toprule=False, bottomrule=False):
        """Create a LaTeX table float.

        Arugments:
            columns: The columns of the table, e.g. 'lcr'
            caption: The caption for the table.
            pos: Indicates the position of the float on the page. Defaults to
                '!htbp'.
            label: Optional label for the table. Defaults to None
        """
        Tabular.__init__(self, columns, toprule=toprule, bottomrule=bottomrule)
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
