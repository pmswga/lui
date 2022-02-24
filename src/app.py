import sys
from translator.translator import *


class LuiApp:
    def __init__(self):
        '''
        Constructor.

        Returns:
            void
        '''
        
        self.translator = LuiTranslator()
        self.code = ""
        self.is_debug = False

    
    def helpCommand(self):
        '''
        Print all translator commands.

        Returns:
            void
        '''
    
        print("List of lui cmd args:")
        print("\t --help        - view list of lui cmd args")
        print("\t --file=[path] - select path to *.lui file")
        print("\t --debug       - turn on debug mode")
        print("\t --version     - view Lui version")
        self.exit()

    def fileCommand(self, path):
        '''
        Get filename from arg '--file'.

        Returns:
            void
        '''
        
        filename = path.split("=")

        if filename is not None:
            with open(filename[1]) as f:
                self.code = f.read()

    def debugCommand(self):
        '''
        Set debug mode.

        Returns:
            void
        '''
    
        self.is_debug = not self.is_debug if True else False

    def versionCommand(self):
        '''
        Print translator version.

        Returns:
            void
        '''
        
        print("Lui version: 1.1")
        self.exit()

    def run(self):
        self.translator.code = self.code
        self.translator.is_debug = self.is_debug

        #try:
        self.translator.run()
        #except Exception as e:
        #    print(e)

    def exit(self):
        sys.exit(0)
