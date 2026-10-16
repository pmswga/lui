import argparse
import sys
from typing import Any

from lui.translator import (
    IRError,
    IRRepresentation,
    Lexer,
    Lexer2IR,
    LexerError,
    StringRepresentation,
)


def debug_print(header: str, content: Any) -> None:
    print(f"==[{header}]==")
    print(content)
    print("====")


def main(args):
    try:
        # Read code
        with open(args.file, "r") as fp:
            code = fp.read()

        # Get lexer
        l = Lexer(code)
        tree = l.getParsedTree()

        if args.debug:
            debug_print("Lexer tree", tree)

        # Get IR
        transformer = Lexer2IR()
        ir: IRRepresentation = transformer.transform(tree)

        if args.debug:
            debug_print("Inner representation", StringRepresentation(ir))

        # Check syntax

        # Generate code
        generated_code = [
            "# LUI code"
        ]

        # Write out
        with open(args.out, "w") as fp:
            fp.writelines(generated_code)
    except OSError as e:
        print(e)
        sys.exit(1)
    except LexerError as e:
        print(e)
        sys.exit(1)
    except IRError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Lui translator tool", usage="[OPTIONS] --file [FILENAME] --out [FILENAME]"
    )

    parser.add_argument("--file", help="lui source file")
    parser.add_argument("--out", default='out.py', help="filename for generated code")
    parser.add_argument("--debug", action="store_true", default=False, help="Show debug")

    args = parser.parse_args()

    if not args.file:
        print("Choose FILENAME")
        sys.exit(1)

    main(args)
