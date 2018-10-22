from grasp_ball_in_box import q_init, q_goal, robot, ps, graph, r, pp


for i in range(100):
	q = robot.shootRandomConfig()
	res_pl1, p_pl1, err_pl1 = graph.applyNodeConstraints('placement', q)
	if res_pl1:break
	

for i in range(100):
	q = robot.shootRandomConfig()
	res_gr1, p_gr1, err_gr1 = graph.applyNodeConstraints('grasp', q)
	if res_gr1:break

for i in range(100):
	q = robot.shootRandomConfig()
	res_pl2, p_pl2, err_pl2 = graph.applyNodeConstraints('placement', q)
	if res_pl2:break
	

for i in range(100):
	q = robot.shootRandomConfig()
	res_gr2, p_gr2, err_gr2 = graph.applyNodeConstraints('grasp', q)
	if res_gr2:break
	
for i in range(100):
	q = robot.shootRandomConfig()
	res_gab, p_gab, err_gab = graph.applyNodeConstraints('gripper-above-ball', q)
	if res_gab:break

for i in range(100):
	q = robot.shootRandomConfig()
	res_bag, p_bag, err_bag = graph.applyNodeConstraints('ball-above-ground', q)
	if res_bag:break
	
for i in range(100):
	q = robot.shootRandomConfig()
	res_gp, p_gp, err_gp = graph.applyNodeConstraints('grasp-placement', q)
	if res_gp:break
	

#Validation transition

for i in range(1000):
	qrand = robot.shootRandomConfig()
	res1, qb1, err1 = graph.generateTargetConfig('transit', p_pl1, qrand)
	if res1:
		print i
		break
		
#visualiser qb


#Validation approach ball

for i in range(1000):
	qrand = robot.shootRandomConfig()
	res2, qb2, err2 = graph.generateTargetConfig('approach-ball', p_pl1, qrand)
	if res2:
		print i
		break

#Validation move gripper away

for i in range(1000):
	qrand = robot.shootRandomConfig()
	res3, qb3, err3 = graph.generateTargetConfig('move-gripper-away', p_gab, qrand)
	if res3:
		print i
		break

#Validation grasp ball

for i in range(1000):
	qrand = robot.shootRandomConfig()
	res3, qb3, err3 = graph.generateTargetConfig('grasp-ball', p_gab, qrand)
	if res3:
		print i
		break
