import random
import sys
import traceback
import battlecode as bc
from Controllers.MissionController import *
from .IStructure import IStructure

""" 
    Factory wrapper. One of these will be instantiated per factory on the board
    It determines when to create units and then instantiates both them and the attached
    wrapper class
    It also handles garrisoning
"""
class Factory(IStructure):
    
    """Place any factory specific setup after the call to Super"""
    def __init__(self, gameController, unitController, unit, missionController):
        super(Factory, self).__init__(gameController, unitController, unit, missionController)
        print("Factory instantiated")

    """Place logic here which will run every turn
    #Can be controlled by the buildController by passing in parameters or by
    creating other methods to encapsulate specific actions"""
    def run(self):
        print("Running Factory")
