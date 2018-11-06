import random
import sys
import traceback

import battlecode as bc
from enum import Enum
from .StrategyController import *

"""
    This class does not currently work as intented.  We're not sure why
    The intention is to create a queue of robot-specific missions. 
    For now, it's better to have the unitController decide what each bot should do
    or default to the individual bots to decide.  Mission controller is the "advanced"
    method to explore when time allows.
"""
class Missions(Enum):
    Idle = 0
    RandomMovement = 1 # Assign location to move to
    Mining = 2 # Assign location to mine
    FollowUnit = 3 # Assign Unit to follow
    Scout = 4 # Assign location to scout
    Patrol = 5 # Assign two locations to partrol
    DestroyTarget = 6 # Assign unit to destroy
    DefendTarget = 7 # Assign unit to defend
    Build = 8 # Assign location to build a factory
    CreateBlueprint = 9 # Assign location to lay down blueprint
    TrainBot = 10 # Instruct Factory to build a bot
    BuildRocket = 11 # Instruct Factory to build a rocket
    Garrison = 12 # Assign target factory to garrison
    HealTarget = 13 # Assign target to heal
    GoToRocket = 14 # Assign rocket and location
    LoadRocket = 14 # Assign unit to load
    UnloadRocket = 15 # Assign rocket to unload
    LuanchRocket = 16 # Assign rocket

class MissionTypes(Enum):
    Worker = 0
    Healer = 1
    Combat = 2
    Factory = 3
    Rocket = 4

class Mission:
    def __init__(self):
        self.action = None
        self.info = None

class MissionInfo:
    def __init__(self):
        self.map_location = None
        self.unit_id = None
        self.unit = None
        self.isRocket = False

# Controller that handles the creation and managment of missions
class MissionController:
    def __init__(self, gameController, strategyController, mapController, researchTreeController):
        self.game_controller = gameController
        self.strategy_controller = strategyController
        self.map_controller = mapController
        self.researchTreeController = researchTreeController

        self.combat_missions = []
        self.healer_missions = []
        self.worker_missions = []
        self.factory_missions = []
        self.rocket_missions = []

        self.rocketCount = 0
        self.MustBuildRocket = False
        self.structureNeedsBuild = False
        print("Mission controller instantiated")