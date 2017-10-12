# Set Driven Key script for connecting Follow attributes to parent / point / orient constraints.

import maya.cmds as cmds


### VARIABLES

## Name of the control with the .follow attribute.
ctrl = "neckEnd_IK_CTRL"

## Empty weights list
weights = []


### FUNCTIONS

## Appends values to the list based on the last character of the selected constraint's weights
def weightList():
    for raw in weightsRaw:
        weights.append(int(raw[-1:]))

## Sets Driven Keys for space switching on the selected constraint
def setSwitchKeys():
    for i in weights:
        # Sets the value of the currently selected weight attribute to 1
        cmds.setDrivenKeyframe(at='w{}'.format(i), cd='{}.follow'.format(ctrl), dv=i, v=1)
    
        # Sets the value of all of the other weight attributes to 0
        for n in weights:
            if weights[n] == i:
                continue
            else:
                cmds.setDrivenKeyframe(at='w{}'.format(i), cd='{}.follow'.format(ctrl), dv=n, v=0)


### SCRIPT

## Finds how many weight attributes there are on a given parent / point / orient constraint,
## Then creates the weight list via the weightList function, and finally calls the setSwitchKeys function.
## The script ends if the selected node is not a constraint.
if cmds.objectType(cmds.ls(sl=True)) == 'parentConstraint':
    weightsRaw = cmds.parentConstraint(q=True, wal=True)
    weightList()
    setSwitchKeys()
elif cmds.objectType(cmds.ls(sl=True)) == 'pointConstraint':
    weightsRaw = cmds.pointConstraint(q=True, wal=True)
    weightList()
    setSwitchKeys()
elif cmds.objectType(cmds.ls(sl=True)) == 'orientConstraint':
    weightsRaw = cmds.orientConstraint(q=True, wal=True)
    weightList()
    setSwitchKeys()

else:
    print("The selected node is not a parent, point, or orient constraint.")
