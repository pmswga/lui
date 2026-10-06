import sys
from pathlib import Path

import pytest
from hypothesis.extra.lark import from_lark
from lark import Lark

sys.path.insert(0, str(Path(__file__).parent))


@pytest.fixture(scope="session")
def grammar() -> str:
    GRAMMAR = ""

    try:
        with open("specs/grammar.lark") as fp:
            GRAMMAR = fp.read()
    except FileNotFoundError:
        print("Grammar not found")
        sys.exit(1)

    return GRAMMAR


@pytest.fixture(scope="session")
def parser(grammar):
    return Lark(grammar)


@pytest.fixture(scope="session")
def strategy(parser):
    return from_lark(parser)
