import random
import sys
import traceback

"""Manages communications between Earth and Mars
Provides public methods for reading and writing
Messages must be as small and efficient as possible
Be sure to account for the delay
Do not bother with this until we're at the point of using mars"""

class CommunicationController:
    def __init__(self, gameController):
        self.game_controller = gameController
        print("communication controller instantiated")