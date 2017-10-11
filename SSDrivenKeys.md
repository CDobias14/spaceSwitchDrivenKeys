#Set Driven Key script for connecting Follow attributes to constraints.

import maya.cmds as cmds

#Finds how many enum values there are for the Follow attribute
weights=[0,1,2,3]

#Set the values for each weight attribute on the parent constraint
for i in weights:

    #Sets the value of the currently selected weight attribute to 1
    cmds.setDrivenKeyframe(at='w%i'%i, cd='L_arm_IK_PV_CTRL.follow', dv=i, v=1)
    
    #Sets the value of all of the other weight attributes to 0
    for n in weights:
        if weights[n] == i:
            continue
        else:
            cmds.setDrivenKeyframe(at='w%i'%i, cd='L_arm_IK_PV_CTRL.follow', dv=n, v=0)
