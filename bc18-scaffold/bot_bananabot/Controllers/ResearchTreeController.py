import random
import sys
import traceback

import battlecode as bc
from .StrategyController import *

"""Keeps track of the current tech tree progress
Items can be added to the queue individually
Items can only be removed from the queue all at once, cancelling any progress
Start by hard coding a research strategy, then make it depend on the situation"""
class ResearchTreeController:
    def __init__(self, gameController, strategyController):
        self.game_controller = gameController
        self.strategy_controller = strategyController
        print("Research tree controller instantiated")