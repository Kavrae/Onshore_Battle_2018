import battlecode as bc
import random
import sys
import traceback

"""Structure base class for any settings of logic that's common to both
    factories and rockets"""
class IStructure:
    def __init__(self, gameController, unitController, unit, missionController):
        self.game_controller = gameController
        self.unit_controller = unitController
        self.mission_controller = missionController
        self.unit = unit
        self.mission = None
        

""" These actions will run at the end of every structure's turn
    After it has run all class specific actions."""
def run(self):
    pass