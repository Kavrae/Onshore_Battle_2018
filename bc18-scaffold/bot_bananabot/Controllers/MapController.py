import random
import sys
import traceback
import battlecode as bc

"""Reads the Earth and Mars maps at the beginning of the game
This is a time intensive process that takes a lot of resoruces, so we read it once
then store it.
Store the two grids in a readable format
Provides read and write access for other controllers to easily utilize
May be responsible for keeping track of comets"""
class MapController:
      def __init__(self, gameController):
        self.gameController = gameController
        self.map = {}
        self.marsMap = {}
        #access properties of earthMap like this self.earth_map[3][5]['isPassable']
        #which will access the isPassable bool for map location x = 3 y = 5
        self.earth_map = []
        self.mars_map = []
        self.my_team_start = []
        self.enemy_team_start = []
        self.startLocation = [0,0]
        print("Map controller instantiated")

      """
      Read the earth map from the gamecontroller then store it in some readable format
      """
      def InitializeEarthMap(self):
            print("Earth map initialized")

      """
      Read the earth map from the gamecontroller then store it in some readable format
      Check the rules. You may not be able to do this until you have a unit on the planet, not sure
      """
      def InitializeMarsMap(self):
            print("Mars map initialized")