import random
import sys
import traceback
import battlecode as bc
from Controllers.MissionController import *
from .IStructure import IStructure

""" 
    Rocket wrapper. One of these will be instantiated per rocket on the board
    It should handle the loading and unloading of robots
    And its own launch sequence
"""
class Rocket(IStructure):
    def __init__(self, gameController, unitController, unit,missionController):
        super(Rocket, self).__init__(gameController, unitController, unit,missionController)

        self.passengerId = None
        self.expectedLoad = 1
        self.rocketIsFull = False
        self.rocketLauchRound = 0

    def run(self):
        print("Running rocket")
