import os
import platform
import sys

project_root = os.path.dirname(os.path.realpath(__file__))
if platform.system() == 'Windows':
    command = '"' + sys.executable + '"' + ' -m pip freeze > "' + project_root + '\\requirements.txt"'
os.popen(command)