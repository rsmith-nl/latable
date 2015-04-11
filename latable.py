# file: latable.py
# vim:fileencoding=utf-8:ft=python
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2012-05-19 15:51:09
# $Date$
# $Revision$
#
# To the extent possible under law, <rsmith@xs4all.nl> has waived all
# copyright and related or neighboring rights to latable.py. This work is
# published from the Netherlands. See
# http://creativecommons.org/publicdomain/zero/1.0/

"Generate LaTeX tables from Python."

__version__ = '$Revision$'[11:-2]


def sheader(align):
    """
    Return the start for a simple table LaTeX environment that aligns the left
    colum with the textblock.

    :param align: A string containing the LaTeX alignments for the columns.
    :returns: The start of a simple aligned tabular environment.
    """
    return r'{\hspace{-\tabcolsep}\begin{tabular}{' + align + r'}'


def header(align, caption, label=None, pos='!htbp'):
    """
    Return the start for a standard table LaTeX environment that contains a
    tabular environment.

    :param align: A string containing the LaTeX alignments for the columns.
    :param caption: A string containing the caption for the table.
    :param label: An optional label. The LaTeX label will be tb:+label.
    :param pos: Positioning string for the table
    :returns: The start of a table.
    """
    rs = r'\begin{table}[' + pos + ']\n'
    rs += '  \\centering\n'
    if label:
        rs += r'  \caption{\label{tb:' + str(label) + '}' + caption + \
              '}\n'
    else:
        rs += r'  \caption{' + caption + '}\n'
    rs += r'  \begin{tabular}{' + align + '}'
    return rs


def sfooter():
    """
    Return the end for a simple table LaTeX environment.
    """
    return r'\end{tabular}}'


def footer():
    """
    Return the end for a standard table LaTeX environment that contains a
    tabular environment.
    """
    rs = r'  \end{tabular}' + '\n'
    rs += r'\end{table}'
    return rs


def line(*args):
    """
    Return the arguments as a line in the table, properly serparated and
    closed with a double backslash.
    """
    rs = '  '
    sep = r' & '
    for n in args:
        rs += str(n)+sep
    rs = rs[:-len(sep)] + r'\\'
    return rs
