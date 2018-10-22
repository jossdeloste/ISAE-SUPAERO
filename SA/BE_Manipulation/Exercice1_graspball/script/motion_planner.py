class MotionPlanner:
  def __init__ (self, robot, ps):
    self.robot = robot
    self.ps = ps

  def solveBiRRT (self, maxIter = float("inf")):
    self.ps.prepareSolveStepByStep ()
    finished = False

    # In the framework of the course, we restrict ourselves to 2 connected components.
    nbCC = self.ps.numberConnectedComponents ()
    if nbCC != 2:
      raise Exception ("There should be 2 connected components.")

    iter = 0
    
    
    #con_comp = zeros(len(q_goal)+1,1)
    #con_comp[0][0] = q_init
    #for i in range(len(q_goal)):
	#	con_comp[i+1][0] = q_goal[i]
    
    
    while True:
      #### RRT begin
             
      #Generate a random configuration  
      q_new = self.robot.shootRandomConfig()
      
      
      for i in range(nbCC):
		#Addind a configuration between the random config and the closest configuration of the connected component
		#And adding the edge to the connected component
		q_cci_near, dist = self.ps.getNearestConfig(q_new,i)
		Path_valid, PathID, err = self.ps.directPath(q_cci_near, q_new, True)
		added_config = self.ps.configAtParam(PathID,self.ps.pathLength(PathID));
		self.ps.addConfigToRoadmap(added_config)
		self.ps.addEdgeToRoadmap(q_cci_near, added_config, PathID, 1)
			
			
      #### RRT end
      ## Check if the problem is solved.
      nbCC = self.ps.numberConnectedComponents ()
      if nbCC == 1:
        # Problem solved
        finished = True
        break
      iter = iter + 1
      if iter > maxIter:
        break
    if finished:
        self.ps.finishSolveStepByStep ()
        return self.ps.numberPaths () - 1

  def solvePRM (self):
    self.ps.prepareSolveStepByStep ()
    #### PRM begin
    #### PRM end
    self.ps.finishSolveStepByStep ()
