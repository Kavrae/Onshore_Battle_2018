import battlecode as bc
import random
import sys
import traceback

from Controllers import *
from Entities import *

class RunEarth:

	# Initialize controllers
	# Initialize all class variables
	# Only include code that should be initialized once at the beginning of the match
	def __init__(self, gameController):
		self.gameController = gameController
		self.mapController = MapController(gameController)
		self.strategyController = StrategyController(gameController, self.mapController)
		self.researchTreeController = ResearchTreeController(gameController, self.strategyController)
		self.buildController = BuildController(gameController, self.mapController, self.strategyController)
		self.unitController = UnitController(gameController, self.strategyController)
		self.targettingController = TargettingController(gameController, self.mapController, self.strategyController)
		self.pathfindingController = PathfindingController(gameController, self.mapController)
		self.enemyTrackingController = EnemyTrackingController(gameController)
	  
	 
	# Runs once per turn for this planet only
	def Run(self):
		self.round = self.gameController.round()
		if self.round == 1:
			print("Running first turn test")
			print("Creating worker class from default worker")
			firstWorker = Worker(self.gameController, self.gameController.my_units()[0].id)
			print("Calling Run() on firstWorker, which exists on parent class")
			firstWorker.run()