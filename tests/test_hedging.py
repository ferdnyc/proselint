"""Tests for hedging.misc check."""

from proselint.checks.hedging.misc import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for hedging.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "I would argue that this is a good test.")
