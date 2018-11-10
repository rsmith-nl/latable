# file: latable.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# SPDX-License-Identifier: MIT
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>
# Created: 2018-11-06T00:33:19+0100
# Last modified: 2018-11-10T09:55:45+0100
"""Generate LaTeX tables from Python."""

import re

__version__ = 3.0


def prepare(
    columns, table=False, caption='Undefined', pos='!htbp', label=None, ignore=False
):
    """Prepare a table.

    Arguments:
        table: Use a table environment when true, otherwise just use a tabular environment.
            The rest of the arguments only needs to be supplied when table=True.
        caption: String to use for the table caption.
        pos: Positioning string for the table.
        label: Optional label for the table.
        ignore: Have the row function ignore extra columns.

    Returns:
        a 3-tuple containing the header for the table, a function to generate rows
        and a footer. The generated row function accepts multiple arguments or a single
        list or tuple.
    """
    numcols = len(re.findall('l|c|r|p{.*?}', columns))

    def rowfn(*args):
        if len(args) == 1 and type(args[0] in (list, tuple)):
            args = args[0]
        if ignore:
            args = args[:numcols]
        elif len(args) > numcols:
            raise IndexError('too many columns specified')
        content = ' & '.join(args)
        if r'\\' in content:
            raise ValueError("arguments should not contain \\\\.")
        if content.count('&') > numcols - 1:
            raise ValueError("Too many '&'")
        if table:
            indent = '    '
        else:
            indent = '  '
        return indent + content + r'\\'

    if not table:
        header = r'\begin{tabular}{' + columns + r'}'
        footer = r'\end{tabular}'
    else:
        header = r'\begin{table}[' + pos + ']\n  \\centering\n'
        if label:
            header += r'  \caption{\label{tb:' + str(label) + '}' + caption + '}\n'
        else:
            header += r'  \caption{' + caption + '}\n'
        header += r'  \begin{tabular}{' + columns + '}'
        footer = '  \\end{tabular}\n\\end{table}'
    return (header, rowfn, footer)


def midrule():
    return '  \\midrule'
