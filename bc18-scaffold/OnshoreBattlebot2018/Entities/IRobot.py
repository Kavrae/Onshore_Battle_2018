import battlecode as bc
import random
import sys
import traceback

class IRobot:
	def __init__(self, gameController, robotId):
		self.gameController = gameController
		self.unit = self.gameController.unit(robotId)

	def run(self):
		# Actions that the default robot should perform each turn
		# Change method to accept whatever options are needed from other controllers to make its decisions
		print("Do robot things")
		
		direction = bc.Direction(random.randint(0,8))
		print("Moving randomly in direction {}".format(direction))
		self.tryMove(direction)

		chance = random.randint(0,100)
		if chance == 0:
			print("Randomly self destructing    1% chance")
			self.selfDestruct()

			
	def tryMove(self, direction) :
		if not self.gameController.is_move_ready(self.unit.id):
			print("Move for Robot [{}] is not ready".format(self.unit.id))
			return False
		if not self.gameController.can_move(self.unit.id, direction):
			print("Robot [{}] cannot move in direction {}".format(self.unit.id, direction))
			return False
		
		self.gameController.move_robot(self.unit.id, direction)
		return True
	
	
	def selfDestruct(self):
		"Robot [{}] self destructing".format(self.unit.id)
		self.gameController.disintegrate_unit(self.unit.id)