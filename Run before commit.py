import os
FolderPath = os.path.dirname(__file__)
Command = 'cd ' + FolderPath
os.system(Command)
os.system('cmd /k "npm run build"')
