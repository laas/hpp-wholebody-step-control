def setHand (cl, right, alpha, lock):
    if right:
        rank = 28
    else:
        rank = 16
    q = cl.robot.getCurrentConfig (0)
    q[rank:rank+6] = [alpha, -alpha, alpha, -alpha, alpha, -alpha]
    cl.robot.setCurrentConfig (0,q)
    for dof in range (rank, rank+6):
        cl.robot.setDofLocked (0, dof, lock, q [dof])

def openHand (cl, right, lock):
    setHand (cl, right, .75, lock)

def closeHand (cl, right, lock):
    setHand (cl, right, .38, lock)
