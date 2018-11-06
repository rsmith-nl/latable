# file: test_tables.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>
# Created: 2018-11-06T20:02:16+0100
# Last modified: 2018-11-06T21:21:23+0100

import pytest
import latable as lt


def test_empty_tabular():
    """Create empty tabular environment."""
    check = '\\begin{tabular}{lr}\n\\end{tabular}'
    lines = []
    lines.append(lt.header('lr', False))
    lines.append(lt.footer())
    result = '\n'.join(lines)
    assert result == check


def test_empty_table():
    """Create empty table environment."""
    check = '''\\begin{table}[!htbp]
  \\centering
  \\caption{\label{tb:foo}Bar}
  \\begin{tabular}{lr}
  \\end{tabular}
\\end{table}'''
    lines = []
    lines.append(lt.header('lr', table=True, caption='Bar', label='foo'))
    lines.append(lt.footer(table=True))
    result = '\n'.join(lines)
    assert result == check


def test_rows():
    """Check normal and short rows."""
    check = '  a & b\\\\'
    result = lt.row('lr', 'a', 'b')
    assert result == check
    check = '  a\\\\'
    result = lt.row('lr', 'a')
    assert result == check


def test_bad_rows():
    """Check exceptions."""
    with pytest.raises(IndexError):
        lt.row('lr', 'a', 'b', 'c')
    with pytest.raises(ValueError):
        lt.row('lr', 'a', 'b\\\\')
    with pytest.raises(ValueError):
        lt.row('lr', 'a', 'b & c')
