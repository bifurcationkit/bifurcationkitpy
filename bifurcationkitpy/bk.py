import sys
from . import load_julia_packages
bk, _ = load_julia_packages("BifurcationKit", "PythonCall")
from juliacall import Main
sys.modules[__name__] = bk # mutate myself