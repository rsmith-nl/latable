# file: latable.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# SPDX-License-Identifier: MIT
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>
# Created: 2018-11-06T00:33:19+0100
# Last modified: 2018-11-06T07:43:18+0100
"""Generate LaTeX tables from Python."""

from functools import lru_cache
import re

__version__ = 2.0


def header(columns, table=False, caption='Undefined', pos='!htbp', label=None):
    """Create a table header.

    Arguments:
        table: Use a table environment when true, otherwise just use a tabular environment.
            The rest of the arguments only needs to be supplied when table=True.
        caption: String to use for the table caption.
        pos: Positioning string for the table.
        label: Optional label for the table.

    Returns:
        The header for the table.
    """
    if not table:
        return r'\begin{tabular}{' + columns + r'}'
    rs = r'\begin{table}[' + pos + ']\n'
    rs += '  \\centering\n'
    if label:
        rs += r'  \caption{\label{tb:' + str(label) + '}' + caption + \
            '}\n'
    else:
        rs += r'  \caption{' + caption + '}\n'
    rs += r'  \begin{tabular}{' + columns + '}'
    return rs


def footer(table=False):
    """Create a table footer.

    Arguments:
        table: Use a table environment when true, otherwise just use a
        tabular environment.

    Returns:
        The footer for the table.
    """
    if not table:
        return r'\end{tabular}'
    return r'  \end{tabular}' + '\n' + r'\end{table}'


@lru_cache(maxsize=24)
def _numcols(columns):
    """Find the number of columns."""
    return len(re.findall('l|c|r|p{.*?}', columns))


def row(columns, *args):
    r"""Create a table row.

    Arguments:
        columns: A string containing the specification for the columns.
            This string is scanned for the ‘l’, ‘c’, ‘r’ and ‘p’
            specifiers. The ‘*’ specifier is *not* handled.
        args: Every argument forms a column of the table. Note that the
            arguments cannot contain '\\'. The amount of arguments
            should not exceed ‘self.numcols’, and it should be less if the
            arguments contain '&'

    Returns:
        The new row.
    """
    numcols = _numcols(columns)
    if len(args) > numcols:
        raise IndexError('too many columns specified')
    content = '  ' + r' & '.join(args) + r'\\'
    if r'\\' in ' '.join(args):
        raise ValueError("arguments should not contain \\\\.")
    if content.count('&') > numcols - 1:
        raise ValueError("Too many '&'")
    return '  ' + r' & '.join(args) + r'\\'
