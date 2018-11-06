import random
import sys
import traceback
import battlecode as bc
from Controllers import *
from Entities import *

""" This class is meant to handle all Earth specific logic
    It should determine what to do by calling the various controllers
    It should never determine HOW to do something
    Turn-specific logic also belongs here
    Feel free to remove controllers that are not used, or add new ones that are needed"""
class RunEarth:
    def __init__(self, gameController):
        self.game_controller = gameController
        self.map_controller = MapController(gameController)
        self.enemy_tracking_controller = EnemyTrackingController(gameController)
        self.strategy_controller = StrategyController(gameController, \
        self.map_controller, self.enemy_tracking_controller)
        self.research_tree_controller = ResearchTreeController(gameController, \
        self.strategy_controller)
        self.build_controller = BuildController(gameController, self.map_controller, \
        self.strategy_controller)
        self.pathfinding_controller = PathfindingController(gameController, self.map_controller)
        self.mission_controller = MissionController(gameController, self.strategy_controller, \
        self.map_controller, self.research_tree_controller)
        self.unit_controller = UnitController(gameController, self.strategy_controller, \
        self.pathfinding_controller, self.mission_controller,self.map_controller, self.research_tree_controller)
        self.targetting_controller = TargettingController(gameController, \
        self.map_controller, self.strategy_controller, self.unit_controller, self.enemy_tracking_controller)
        print("Earth controller instantiated")
        
    def Run(self):
        #This runs on Earth once per turn
        #Make calls to controllers here
        print("Running Earth turn")