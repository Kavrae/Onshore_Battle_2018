import random
import battlecode as bc
from Controllers.MissionController import *
from .IRobot import IRobot

"""
    Mage wrapper. One of these will be instantiated per mage on the board
    It should know how to do all possible mage actions with appropriate safety checks
    When to do those actions should be controlled by the UnitController
    With defaults of what to do if given no commands
"""
class Mage(IRobot):
    
    """ Super init calls the IRobot constructor to set up all components that 
            are common between all robot types
            Additional mage specific setup goes after this"""
    def __init__(self, gameController, unitController, \
    pathfindingController, missionController, unit,mapController):
        super().__init__(gameController, unitController, \
        pathfindingController, missionController, unit, bc.UnitType.Mage,mapController,mapController)

    """Place logic here which will run every turn
    Can be controlled by the unitController by passing in parameters or by
    creating other methods to encapsulate specific actions"""
    def run(self):
        print("Running mage")
