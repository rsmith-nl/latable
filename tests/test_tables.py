# file: test_tables.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# SPDX-License-Identifier: MIT
# Copyright © 2018 R.F. Smith <rsmith@xs4all.nl>
# Created: 2018-11-06T20:02:16+0100
# Last modified: 2019-07-09T00:02:42+0200

import pytest
import latable as lt


def test_empty_tabular():  # {{{1
    """Create empty tabular environment."""
    check = "\\begin{tabular}{lr}\n\\end{tabular}"
    lines = []
    header, _, footer = lt.prepare("lr", False)
    lines.append(header)
    lines.append(footer)
    result = "\n".join(lines)
    assert result == check  # }}}


def test_empty_table():  # {{{1
    """Create empty table environment."""
    check = r"""\begin{table}[!htbp]
  \centering
  \caption{\label{tb:foo}Bar}
  \begin{tabular}{lr}
  \end{tabular}
\end{table}"""
    lines = []
    header, _, footer = lt.prepare("lr", table=True, caption="Bar", label="foo")
    lines.append(header)
    lines.append(footer)
    result = "\n".join(lines)
    assert result == check  # }}}


def test_normal_row():  # {{{1
    """Check normal row."""
    check = "  a & b\\\\"
    _, row, _ = lt.prepare("lr")
    result = row("a", "b")
    assert result == check  # }}}


def test_short_row():  # {{{1
    """Check short row."""
    check = "  a\\\\"
    _, row, _ = lt.prepare("lr")
    result = row("a")
    assert result == check  # }}}


def test_row_ignore():  # {{{1
    """Check that ignore works."""
    check = "  a & b\\\\"
    _, row, _ = lt.prepare("lr", ignore=True)
    result = row("a", "b", "c")
    assert result == check
    result = row("a", "b", "c & d")
    assert result == check  # }}}


def test_bad_row_extra_args():  # {{{1
    """Check that too many arguments raises an exception."""
    _, row, _ = lt.prepare("lr", ignore=False)
    with pytest.raises(IndexError):
        row("a", "b", "c")  # }}}


def test_bad_row_backslashes():  # {{{1
    """Check that a double blackslash raises an exception."""
    _, row, _ = lt.prepare("lr")
    with pytest.raises(ValueError):
        row("a", "b\\\\")  # }}}


def test_bad_row_ampersand():  # {{{1
    """Check that arguments with an extra ampersand raises an exception."""
    _, row, _ = lt.prepare("lr")
    with pytest.raises(ValueError):
        row("a", "b & c")  # }}}
