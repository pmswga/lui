from app import *

app = LuiApp()
if len(sys.argv) > 1:
    try:
        for arg in sys.argv:
            if arg.find("--file=") != -1:
                app.fileCommand(arg)

            if arg.find("--debug") != -1:
                app.debugCommand()

            if arg.find("--help") != -1:
                app.helpCommand()

            if arg.find("--version") != -1:
                app.versionCommand()

        app.run()
    except Exception as e:
        print(e)
else:
    app.helpCommand()
