"""Many a singular.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Many a singular.
date:       2014-06-10 12:31:19
categories: writing
---

The idiom 'many a' requires a singular verb.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.many_a"
    msg = "'many a' requires a singular verb."

    preferences = [
        ["is many a", ["are many a"]],
        ["has been many a", ["have been many a"]],
        ["was many a", ["were many a"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
