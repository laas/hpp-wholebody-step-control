# Copyright 2011, Sebastien Dalibard, CNRS
#
# This file is part of hpp-wholebody-step-test.
# hpp-wholebody-step-test is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# hpp-wholebody-step-test is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# hpp-wholebody-step-test. If not, see <http://www.gnu.org/licenses/>.

# Requires at least CMake 2.6 to configure the package.
CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

INCLUDE(cmake/base.cmake)
INCLUDE(cmake/python.cmake)

SET(PROJECT_NAME hpp-wholebody-step-test)
SET(PROJECT_DESCRIPTION "Scripts to test hpp-wholebody-step-planner.")
SET(PROJECT_URL "https://github.com/laas/hpp-wholebody-step-control")

SETUP_PROJECT()

FINDPYTHON()
ADD_REQUIRED_DEPENDENCY("hpp-environment-data >= 1.0")
ADD_REQUIRED_DEPENDENCY("hpp-wholebody-step-corba >= 0.2")
ADD_REQUIRED_DEPENDENCY("hpp-corbaserver >= 2.4")

INSTALL(FILES
  src/hpp/corbaserver/wholebody_step/hands.py
  src/hpp/corbaserver/wholebody_step/__init__.py
  DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/wholebody_step
)
  

SETUP_PROJECT_FINALIZE()
