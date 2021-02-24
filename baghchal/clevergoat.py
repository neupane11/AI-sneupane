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
    
    def isEdgesOpen(self, row, col):
        game = self.game
        board = game.board
        move = [row,col]

        if move == [0,2] or move == [2,0] or move == [2,4] or move == [4,2]:
            if board[row][col] == Const.MARK_NONE:
                return True
        elif move == [0,1] or move == [1,0] or move == [1,4] or move == [4,1] :
            if board[row][col] == Const.MARK_NONE:
                return True
        elif move == [0,3] or move == [3,0] or move == [3,4] or move == [4,3] :
            if board[row][col] == Const.MARK_NONE:
                return True
        elif move == [0,0] or move == [0,4] or move == [4,0] or move == [4,4] :
            if board[row][col] == Const.MARK_NONE:
                return True
        else:        
            return False
    
        
    def isCloseToTiger(self,row : int, col : int):
        game : Game = self.game
        board : List[List[int]] = game.board
        for (dRow,dCol) in Const.DIRS[(row,col)]:
            if board[row+dRow][col+dCol] == Const.MARK_TIGER:
                return True
        return False

    def propose(self) -> Move:
        notClose : List[Move] =  []
        edgeMoves : List[Move] = []
        willBeEaten: List[Move] = []
        safe : List[Move]=[]
        tigerMovement = self.game.tigerMoves() 
        moves = self.game.goatMoves()
        for move in moves:
            if self.isEdgesOpen(move.toRow,move.toCol):
                edgeMoves.append(move)
            if  not self.isCloseToTiger(move.toRow,move.toCol):
                notClose.append(move)
            for movements in tigerMovement:
                if abs(movements.toRow - move.toRow) == 1:
                    willBeEaten.append(move)
                else:
                    safe.append(move)

                if abs(movements.toCol - move.toCol) == 1:
                    willBeEaten.append(move)
                else:
                    safe.append(move)
        
        if len(edgeMoves) > 0:
            return random.choice(edgeMoves)
        elif len(notClose) > 0:
            return random.choice(notClose)
        
        if len(notClose) > 0:
            return random.choice(notClose)
        
        
        else:
            return random.choice(moves)
           