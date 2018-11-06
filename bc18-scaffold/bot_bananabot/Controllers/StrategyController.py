from enum import Enum

"""Uses all known information from various controllers to determine the current strategy
Stores the values from enums, for easy access
Start by simply returning {"Default"} until we get the basics finished.
This probably shouldn't be touched until the default strategy is solid"""
class StrategyController:
    def __init__(self, gameController, mapController, enemyTrackingController):
        self.game_controller = gameController
        self.map_controller = mapController
        self.enemy_tracking_controller = enemyTrackingController

        self.macro_strategy = MacroStrategies.Default
        self.unit_strategy = UnitStrategies.Default
        print("Strategy controller instantiated")

"""Examples of macro strategies that could be utilized by the entire 
controller stack"""
class MacroStrategies(Enum):
    Default = 0
    ZergRush = 1
    Turtle = 2
    MarsRush = 3

"""Examples of micro strategies
that could be utilized by the unit controller or build controller"""
class UnitStrategies(Enum):
    Default = 0
    WorkerRush = 1
    KnightRush = 2
    MageRush = 3
    RangerRush = 4
    HealerRush = 5
