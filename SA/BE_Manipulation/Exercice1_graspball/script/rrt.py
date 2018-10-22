from hpp.corbaserver.practicals.ur5 import Robot
from hpp.corbaserver import ProblemSolver
from hpp.gepetto import ViewerFactory, PathPlayer

import readline
import rlcompleter
readline.parse_and_bind("tab: complete")

robot = Robot ('ur5')
ps = ProblemSolver (robot)

vf = ViewerFactory (ps)

vf.loadObstacleModel ("hpp_practicals","ur_benchmark/obstacles","obstacles")
vf.loadObstacleModel ("hpp_practicals","ur_benchmark/table","table")
vf.loadObstacleModel ("hpp_practicals","ur_benchmark/wall","wall")

r = vf.createViewer ()

q1 = [0, -1.57, 1.57, 0, 0, 0]; q2 = [0.2, -1.57, -1.8, 0, 0.8, 0]
q3 = [1.57, -1.57, -1.8, 0, 0.8, 0]

r (q2)
r (q1)

ps.setInitialConfig (q2)
ps.addGoalConfig (q1)

from motion_planner import MotionPlanner
m = MotionPlanner (robot, ps)
pathId = m.solveBiRRT (maxIter = 1000)
ps.solve()
pp = PathPlayer (robot.client, r)
pid = ps.numberPaths () - 1
if pid < 0: raise RuntimeError ("No path in vector")

pp (pid)
