from pybuilder.core import use_plugin, init
from pybuilder.core import task
#from pybuilder.plugins.exec_plugin import *

import time

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "bilder_start"
default_task = "publish"

@init
def set_properties(project):
    project.build_depends_on('mockito')

"""
    logger.info("Hello, PyBuilder--set_properties--")
    project.set_property('unittest_module_glob','selenium')


@task
def run_unit_tests(project, logger):
    logger.info("Hello --run_unit_tests---")
    run_command('run_unit_tests', project, logger)

@task
def publish (logger):
   logger.info("Hello, PyBuilder--publish---")

@task
def say_hello ():
    print("Hello, PyBuilder--say_hello--")

@task
def say_hello_logger (logger):
   logger.error("Hello, PyBuilder--say_hello_logger--")
"""