# file: latable.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# SPDX-License-Identifier: MIT
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>
# Created: 2018-11-06T00:33:19+0100
# Last modified: 2019-07-08T23:12:19+0200
"""Generate LaTeX tables from Python."""

import re

__version__ = "2019.07.08"


def prepare(
    columns, ignore=True, table=False, caption="Undefined", pos="!htbp", label=None
):
    """Prepare a table.

    Arguments:
        columns (str): Column layout in LaTeX format. Currently supports
            ‘l’, ‘c’, ‘r’ and ‘p’.
        ignore (bool): Have the row function ignore extra columns.
        table (bool): Use a table environment when true, otherwise just use a
            tabular environment. The rest of the arguments only needs to be supplied
            when table=True.
        caption (str): String to use for the table caption.
        pos (str): Positioning string for the table.
        label (str): Optional label for the table.

    Returns:
        a 3-tuple containing the header for the table, a function to generate rows
        and a footer.

    The generated row function accepts multiple arguments or a single list or
    tuple. It will try to convert its arguments to strings. But for more
    control it is recommended that the user formats the arguments as strings.

    Example:
    >>> import latable
    >>> header, row, footer = latable.prepare('ll')
    >>> print(header)
    \begin{tabular}{ll}
    >>> print(row('1', '2'))
    1 & 2\\
    >>> print(row(3, 4.56))
    3 & 4\\
    >>> print(footer)
    \end{tabular}
    """
    numcols = len(re.findall("l|c|r|p{.*?}", columns))

    def rowfn(*args):
        """Function for generating rows."""
        if len(args) == 1 and type(args[0] in (list, tuple)):
            args = args[0]
        if ignore:
            args = args[:numcols]
        elif len(args) > numcols:
            raise IndexError("too many columns specified")
        # Try to convert other types of arguments to strings.
        args = [a if isinstance(a, str) else str(a) for a in args]
        content = " & ".join(args)
        if r"\\" in content:
            raise ValueError("arguments should not contain \\\\.")
        if content.count("&") > numcols - 1:
            raise ValueError("Too many '&'")
        if table:
            indent = "    "
        else:
            indent = "  "
        return indent + content + r"\\"

    if not table:
        header = r"\begin{tabular}{" + columns + r"}"
        footer = r"\end{tabular}"
    else:
        header = r"\begin{table}[" + pos + "]\n  \\centering\n"
        if label:
            header += r"  \caption{\label{tb:" + str(label) + "}" + caption + "}\n"
        else:
            header += r"  \caption{" + caption + "}\n"
        header += r"  \begin{tabular}{" + columns + "}"
        footer = "  \\end{tabular}\n\\end{table}"
    return (header, rowfn, footer)


def midrule():
    return "  \\midrule"
