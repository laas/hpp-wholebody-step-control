import sys, os
import commands
from hpp.corbaserver import Client as HppClient
from hpp.corbaserver.wholebody_step.client import Client as WbsClient
from hpp_corbaserver.hpp import Configuration
from hpp.corbaserver.wholebody_step import openHand, closeHand

cl = HppClient()
clw = WbsClient()

pkgconfig_command = 'pkg-config --variable=datarootdir hpp-environment-data'
output = commands.getstatusoutput (pkgconfig_command)
if output [0] != 0:
    raise RuntimeError ('"' + pkgconfig_command + '" failed')

env_dir = output [1] + "/hpp-environment/2012ijrr-shelves"

cl.robot.loadRobotModel ("hrp2_14", .01, "_capsule", "_capsule", "")
half_sitting = cl.robot.getCurrentConfig(0)

cl.problem.initializeProblem()
cl.problem.parseFile(env_dir + "/env.kxml")

## Reaching motion starting from half-sitting
target = (0.628, 0.078, 1.12)
away = (target [0], target [1], 3.)
cl.obstacle.moveObstacleConfig ("Sphere",
                                Configuration (trs = away,
                                               rot = (1, 0, 0,
                                                      0, 1, 0,
                                                      0, 0, 1)))
# Set right hand locked open
openHand (cl, True, True)
# Set left hand lock closed
closeHand (cl, False, True)
q = cl.robot.getCurrentConfig (0)
q_init = q [::]
cl.problem.setInitialConfig(0, q)

qgoals = []
while len (qgoals) == 0:
    clw.problem.generateGoalConfig (target [0], target [1], target [2], 8)
    qgoals = cl.problem.getGoalConfig (0)

if cl.problem.solve () != 0:
    raise RuntimeError ("Failed to reach the object")

## Transfer motion
pathId = cl.problem.countPaths (0) - 1
length = cl.problem.pathLength (0, pathId)
q = cl.problem.configAtDistance (0, pathId, length)
cl.problem.resetGoalConfig (0)
qgoals = []
cl.problem.setInitialConfig(0, q)
target = (0.62, -0.16, 0.82)
while len (qgoals) == 0:
    clw.problem.generateGoalConfig (target [0], target [1], target [2], 8)
    qgoals = cl.problem.getGoalConfig (0)

if cl.problem.solve () != 0:
    raise RuntimeError ("Failed to transfer the object")

## Return motion
pathId = cl.problem.countPaths (0) - 1
length = cl.problem.pathLength (0, pathId)
q = cl.problem.configAtDistance (0, pathId, length)
cl.problem.resetGoalConfig (0)
cl.problem.setInitialConfig(0, q)
cl.problem.addGoalConfig (0, q_init)
cl.problem.setPathOptimizer (0, "random", 50)
if cl.problem.solve () != 0:
    raise RuntimeError ("Failed to return to initial configuration")

pathId = cl.problem.countPaths (0) - 1
