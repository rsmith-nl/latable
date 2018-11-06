# file: test_tables.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>
# Created: 2018-11-06T20:02:16+0100
# Last modified: 2018-11-06T23:13:36+0100

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


def test_normal_row():
    """Check normal row."""
    check = '  a & b\\\\'
    row = lt.rowfn('lr')
    result = row('a', 'b')
    assert result == check


def test_short_row():
    """Check short row."""
    check = '  a\\\\'
    row = lt.rowfn('lr')
    result = row('a')
    assert result == check


def test_row_ignore():
    """Check that ignore works."""
    row = lt.rowfn('lr', ignore=True)
    check = '  a & b\\\\'
    result = row('a', 'b', 'c')
    assert result == check
    result = row('a', 'b', 'c & d')
    assert result == check


def test_bad_row_extra_args():
    """Check that too many arguments raises an exception."""
    row = lt.rowfn('lr')
    with pytest.raises(IndexError):
        row('a', 'b', 'c')


def test_bad_row_backslashes():
    """Check that a double blackslash raises an exception."""
    row = lt.rowfn('lr')
    with pytest.raises(ValueError):
        row('a', 'b\\\\')


def test_bad_row_ampersand():
    """Check that arguments with an extra ampersand raises an exception."""
    row = lt.rowfn('lr')
    with pytest.raises(ValueError):
        row('a', 'b & c')
