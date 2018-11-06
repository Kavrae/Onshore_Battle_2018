import battlecode as bc
import random
from Entities import *
from Controllers.MissionController import Missions

"""Keeps a list of all friendly units
Loops over all units, running their "Run" methods one at a time
Can prioritize robots by importance or any other activation order
Responsible for putting robots back into the queue if a healer resets their cooldowns
Be aware that keeping track of units can be difficult, as the wrappers are not
deleted whenever the unit is killed and are not created if you start the game with
any robots"""
class UnitController:
    def __init__(self, gameController, strategyController, \
    pathfindingController, missionController, mapController, researchTreeController):
        self.game_controller = gameController
        self.strategy_controller = strategyController
        self.pathfinding_controller = pathfindingController
        self.mission_controller = missionController
        self.mapController = mapController
        self.researchTreeController = researchTreeController

        self.robots = []
        self.structures = []

        self.workerCount = 0
        self.factoryCount = 0
        self.rocketCount = 0
        self.mustBuildRocket = False
        print("Unit controller instantiated")