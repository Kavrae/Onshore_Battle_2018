import battlecode as bc
import random
import sys
import traceback
from Controllers.MissionController import *

""" This is the IRobot base class
    Only things that apply to all robots should be placed here.
    The mission controller should probably be replaced or removed
    This is the spot for things like common movement or communication
    """
class IRobot:
    """Update this constructor to remove any unnecessary settings or references"""
    def __init__(self, gameController, unitController, \
    pathfindingController, missionController, unit, unitType, mapController):
        self.game_controller = gameController
        self.unit_controller = unitController
        self.pathfinding_controller = pathfindingController
        self.mission_controller = missionController
        self.map_controller = mapController

        #Reference to the BattleCode unit object that the server side code tracks
        self.unit = unit
        self.unit_type = unitType

        #Current mission dictates the robot's actions for the turn
        self.mission = None

        #Location that the robot will move to, regardless of what the mission type is
        self.target_location = None

        #List of directions to reach the target location
        self.path = None

        #Round that the current mission started on.
        self.mission_start_round = 0

        #To allow for Missions that have a secondary action
        self.perform_second_action = False

        #last position
        self.lastPosition = None
        
        self.directions = list(bc.Direction)

    """ These actions will run at the end of every robot's turn
        After it has run all class specific actions."""
    def run(self):
        pass

