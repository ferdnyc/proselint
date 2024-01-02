"""Tests for terms.animal_adjectives check."""

from proselint.checks.terms.animal_adjectives import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for terms.animal_adjectives."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "It was some bird-like creature.")
