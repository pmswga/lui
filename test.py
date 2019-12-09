
from translator.preprocessor.preprocessor import *

code = """

a = [1,2,3]

#LUI
#FILENAME=window
#VERSION=1.0

Window {
    title: "Hello"
    width: 125
    height: 125
}


"""

pre = Preprocessor()

print(pre.parse(code))
print(pre.defines)

