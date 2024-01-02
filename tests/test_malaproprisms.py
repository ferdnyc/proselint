"""Tests for malaproprisms.misc check."""

from proselint.checks.malapropisms.misc import check

from .conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for malaproprisms.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "Found in the Infinitesimal Universe.")
