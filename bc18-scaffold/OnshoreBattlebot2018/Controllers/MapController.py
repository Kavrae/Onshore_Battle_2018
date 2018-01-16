import random
import sys
import traceback
import battlecode as bc

# Reads the Earth and Mars maps at the beginning of the game (time intensive)
# Store the two grids in a readable format
# Provides read and write access for other controllers to easily utilize
# May be responsible for keeping track of comets
class MapController:

      """This is the Map Controller"""
      def __init__(self, gameController):
        self.gameController = gameController
        self.map = {}
        self.marsMap = {}
        #access properties of earthMap like this self.earth_map[3][5]['isPassable']
        #which will access the isPassable bool for map location x = 3 y = 5
        self.earth_map = []
        self.mars_map = []

      def InitializeEarthMap(self):
            try:
                  print("Initializing Earth map")
                  self.map = self.gameController.starting_map(bc.Planet.Earth)
                  print(self.map.width)
                  print(self.map.height)
                  self.earth_Map = []
                  for mapX in range(self.map.height):
                        self.earth_map.append([])
                        for mapY in range(self.map.width):
                              mapLoc = bc.MapLocation(bc.Planet.Earth,mapX, mapY)
                              self.earth_map[mapX].append({"x": mapX, "y": mapY, "hash": self.hashCoordanates(mapX, mapY), "isPassable": self.map.is_passable_terrain_at(mapLoc), "karboniteCount": self.map.initial_karbonite_at(mapLoc)})
                  print(self.map.planet)
            except Exception as e:
                  print('Error:', e)
                  # use this to show where the error was
                  traceback.print_exc()

      def InitializeMarsMap(self):
            try:
                  print("Initializing Mars Map")
                  self.marsMap = self.gameController.starting_map(bc.Planet.Mars)
                  self.mars_map = []
                  for mapX in range(self.marsMap.width):
                        self.mars_map.append([])
                        for mapY in range(self.marsMap.height):
                              mapLoc = bc.MapLocation(bc.Planet.Mars, mapX, mapY)
                              self.mars_map[mapX].append({"x": mapX, "y": mapY, "hash": self.hashCoordanates(mapX, mapY), "isPassable": self.marsMap.is_passable_terrain_at(mapLoc), "karboniteCount": self.marsMap.initial_karbonite_at(mapLoc)})
                  print(self.marsMap.planet)
            except Exception as e:
                  print('Error:', e)
                  # use this to show where the error was
                  traceback.print_exc()
                  
      def hashCoordanates(self, inX, inY):
            hash = 23;
            hash = 29 * hash + inX;
            hash = 29 * hash + inY;
            return hash

      def GetNode(self, planet, mapX, mapY):
            if planet == bc.Planet.Earth:
                  node = self.GetNodeEarth(mapX, mapY)
            else:
                  node = self.GetNodeMars(mapX, MapY)
            return node
            
      def GetNodeEarth(self, mapX, mapY):
            if (mapX <= self.map.width - 1 and mapY <= self.map.height - 1 and mapX > -1 and mapY > -1):
                  node = self.earthMap[mapX][mapY]
                  return node
            return None

      def GetNodeMars(self, mapX, mapY):
            if (mapX <= self.marsMap.width - 1 and mapY <= self.marsMap.height - 1 and mapX > -1 and mapY > -1):
                  node = self.marsMap[mapX][mapY]
                  return node
            return None