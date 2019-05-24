import copy
import random
from tree import *
from node import *


class CellIsNotEmptyError(Exception):
    """Cell is already taken Exception"""
    pass


"""
!!!
Written with an inspiration from example code given by Oles
!!!
"""

class Board:
    """Represents board"""
    NOUGHT = 1
    CROSS = -1
    EMPTY = 0

    NOUGHT_WINNER = 1
    CROSS_WINNER = -1
    DRAW = 2
    NOT_FINISHED = 0

    WINNING_COMBINATIONS = []
    for i in range(3):
        temp1, temp2 = [], []
        for j in range(3):
            temp1.append((i, j))
            temp2.append((j, i))
        WINNING_COMBINATIONS.append(temp1)
        WINNING_COMBINATIONS.append(temp2)

    WINNING_COMBINATIONS.append([(0, 0), (1, 1), (2, 2)])
    WINNING_COMBINATIONS.append([(0, 2), (1, 1), (2, 0)])

    def __init__(self):
        """Initialization"""
        self.cells = [[0] * 3 for _ in range(3)]
        self.previous = Board.NOUGHT
        self.number_of_moves = 0

    def move(self, cell):
        """Puts cross or nought to certain cell"""
        if self.cells[cell[0]][cell[1]] != 0:
            raise CellIsNotEmptyError
        self.previous = -self.previous
        self.cells[cell[0]][cell[1]] = self.previous
        self.number_of_moves += 1
        return True

    def has_winner(self):
        """Checks if there is a winner"""
        for i in self.WINNING_COMBINATIONS:
            lst = []
            for j in i:
                lst.append(self.cells[j[0]][j[1]])
            if max(lst) == min(lst) and max(lst) != Board.EMPTY:
                return max(lst)
        if self.number_of_moves == 9:
            return Board.DRAW

        return Board.NOT_FINISHED

    def move_random(self):
        """Puts cross or nought to random cell"""
        available = []
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == Board.EMPTY:
                    available.append((i, j))
        cell = random.choice(available)
        self.previous = -self.previous
        self.cells[cell[0]][cell[1]] = self.previous
        self.number_of_moves += 1
        return True

    def compute_score(self):
        """Calculates decision score"""
        computetree = Tree()
        computetree._root = Node(self)
        has_winner = self.has_winner()
        if has_winner:
            winner_scores = {Board.NOUGHT_WINNER: 1, Board.CROSS_WINNER: -1, Board.DRAW: 0}
            return winner_scores[has_winner]
        boards = []
        for i in range(3):
            for j in range(3):
                temp = copy.deepcopy(self)
                try:
                    temp.move((i, j))
                    boards.append(temp)
                except:
                    pass

        computetree._root.next = boards
        return sum([i.compute_score() for i in boards])

    def __str__(self):
        """String representation"""
        data = {0: " ", 1: "O", -1: "X"}
        result = ""
        for i in self.cells:
            for j in i:
                result += str(data[j]) + " "
            result += "\n"
        return result


if __name__ == "__main__":
    board1 = Board()
    board1.move_random()
    board2 = Board()
    board2.move_random()
    print(board1)
    print(board1.compute_score())
    print(board2)
    print(board2.compute_score())
