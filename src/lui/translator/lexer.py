import json

from lark import Lark, LarkError, ParseError, ParseTree

from .grammar import GRAMMAR


class LexerError(Exception):
    pass


class Lexer:
    def __init__(self, code: str | None) -> None:
        try:
            self.parser: Lark =  Lark(GRAMMAR, parser='lalr')
        except LarkError as e:
            raise LexerError(e)

        self.parsed_tree: ParseTree | None = None

        if code:
            try:
                self.parsed_tree = self.parser.parse(code)
            except ParseError as e:
                raise LexerError(e)

    def getParsedTree(self) -> ParseTree | None:
        return self.parsed_tree

