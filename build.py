from pybuilder.core import use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")

default_task = "publish"

name = "CS3280 Project 2 - Resistor"
version = "0.0.1"
