import battlecode as bc
import random
import sys
import traceback

from Entities import *
from Controllers.EnemyTrackingController import *

"""Given a robot, a target type to prioritize, and an enemy list
Determines the highest priority location to move towards
This can apply to workers looking for a build location, healers looking for allies, or rangers looking for targets
To start, focus on simply returning the closest or most valuable target
Make use of the enemy tracking controller"""
class TargettingController:
	def __init__(self, gameController, mapController, strategyController, unitController, enemyTrackingController):
		self.gameController = gameController
		self.mapController = mapController
		self.strategyController = strategyController
		self.unitController = unitController
		self.enemyTrackingController = enemyTrackingController
		self.enemyRobots = []
		self.enemyStructures = []
		self.ally = gameController.team()
		self.roundLimit = 10
		print("Targetting controller instantiated")