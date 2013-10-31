import os, time

def isfloat (string):
    try:
        float (string)
    except ValueError as exc :
        return False
    return True
    
def parseConfigInLog (pid, prefix):
    listConfig = []
    devel_dir = os.getenv('DEVEL_DIR')+'/install'
    with open (devel_dir + '/var/log/hpp/journal.' + str(pid) + '.log',
               'r') as f:
        for line in f:
            if line[:len(prefix)] == prefix:
                configString = line [len(prefix):].strip(' ')
                config = map (float, filter (isfloat, configString.split (' ')))
                listConfig.append (config)
    return listConfig

def playConfigs (cl, robot, configs, robotStatePublisher):
    for q in configs:
        cl.robot.setCurrentConfig (robot, q)
        if robotStatePublisher:
            robotStatePublisher.publish (q)
            time.sleep (.5)

def playPath (cl, rsp, robot, path):
    length = cl.problem.pathLength (robot, path)
    for i in range (201):
        l = i*length/200.
        cfg = cl.problem.configAtDistance (robot, path, l)
        if cl:
            cl.robot.setCurrentConfig (robot, cfg)
        if rsp:
            rsp.publish (q)
            print (q)
        time.sleep (.01)

