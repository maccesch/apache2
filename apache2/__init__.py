import os
import subprocess

def a2reload():
    subprocess.call([os.path.join(os.path.realpath(os.path.dirname(__file__)), 'a2reload')], shell=True)
