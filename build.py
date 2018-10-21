from pybuilder.core import use_plugin
from pybuilder.core import task
import os

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")

default_task = "publish"


@task("run_http_server", description="Starts the server on port 8000")
def run_http_server(project):
    server_path = os.path.join(
        os.getcwd(), 'src', 'main', 'python', 'service.py')
    os.system('python ' + server_path)


name = "CS3280 Project 2 - Resistor"
version = "0.0.1"
