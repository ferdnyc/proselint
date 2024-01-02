"""Tests for misc.apologizing check."""

from proselint.checks.misc.apologizing import check

from .conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.apologizing."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "More research is needed.")
