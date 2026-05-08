import sys
import random
import runpy
import os

INSTALL_DIR = os.path.dirname(os.path.abspath(__file__))


def run(script):
    runpy.run_path(os.path.join(INSTALL_DIR, script), run_name="__main__")


args = sys.argv[1:]

if "--fire" in args:
    run("fire.py")
elif "--snow" in args:
    run("snow.py")
else:
    run(random.choice(["snow.py", "fire.py"]))
