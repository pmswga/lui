import pathlib

from hypothesis import given
from lark import Lark


def test_grammar(strategy, parser):

    @given(strategy)
    def test(example_grammar):
        tree = parser.parse(example_grammar)
        assert tree is not None

    test()


def test_examples(grammar):
    l = Lark(grammar)

    for example in pathlib.Path("examples").glob("*.lui"):
        tree = l.parse(example.read_text())
        assert tree is not None
