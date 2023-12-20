import sys
import os

script_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(f'{script_path}/cmake-build-debug/')

import citePyExample

lib = citePyExample.IExample.createLibrary()
print(lib.add(1, 2))

