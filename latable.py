#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright © 2012 R.F. Smith <rsmith@xs4all.nl>. All rights reserved.
# $Date$
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
# THIS SOFTWARE IS PROVIDED BY AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

"Generate LaTeX tables from Python."

__version__ = '$Revision$'[11:-2]

rule = (r'  \toprule'+'\n', r'  \midrule'+'\n', r'\bottomrule'+'\n')


def sheader(align):
    """
    Return the start for a simple table LaTeX environment that aligns the left
    colum with the textblock.

    Arguments:
    align -- A string containing the LaTeX alignments for the columns.
    """
    return r'{\hspace{-\tabcolsep}\begin{tabular}{'+align+r'}'


def header(align, caption, label=None, pos='!htbp'):
    """
    Return the start for a standard table LaTeX environment that contains a
    tabular environment.

    Arguments:
    align -- a string containing the LaTeX alignments for the columns.
    caption -- a string containing the caption for the table.
    label -- an optional label. The LaTeX label will be tb:+label.
    pos -- positioning string for the table
    """
    rs = r'\begin{table}['+pos+']\n'
    rs += '  \\centering\n'
    if label:
        rs += r'  \caption{\label{tb:'+str(label)+r'}'+caption+r'}'+'\n'
    else:
        rs += r'  \caption{'+caption+r'}'+'\n'
    rs += r'  \begin{tabular}{'+align+r'}'
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
    rs = r'  \end{tabular}'+'\n'
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
    rs = rs[:-len(sep)]+r'\\'
    return rs


def num(fmt):
    """
    Embed the single format spec argument using the \num macro from the
    SIunitx package.
    """
    return '\\num{{{:'+fmt+'}}}'


# Built-in test.
# if __name__ == '__main__':
#    pass
