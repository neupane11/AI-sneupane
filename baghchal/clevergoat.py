from typing import List, Tuple, Optional
from agent import Agent
from game import Game
from const import Const
from move import Move
import random

class CleverGoat(Agent):
    def __init__(self,game : Game, side : int):
        super(CleverGoat, self).__init__(game,side)
        if side != Const.MARK_GOAT:
            raise ValueError("side must be goat")
    def propose(self) -> Move:
        moves = self.game.goatMoves()
        for move in moves:
            if move.goat:
                return move
        return random.choice(moves)
