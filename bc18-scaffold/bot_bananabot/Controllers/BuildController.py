import random
import sys
import traceback

"""Keeps track of friendly units and structures
Utilize other controllers for data
Set build priorities and locations
Workers access this class to determine what to build next"""
class BuildController:
    def __init__(self, gameController, mapController, strategyController):
        self.game_controller = gameController
        self.map_controller = mapController
        self.strategy_controller = strategyController