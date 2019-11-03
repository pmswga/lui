
import runpy

def isList():
    code = "[1, 2, 3, 4, 5, 6, 7]"

    res = exec(code)

    print(res)

    if isinstance(res, list):
        print("Nice")


lst = eval("[1, 2, 3, 4, 5]")

print(lst)

#isList()