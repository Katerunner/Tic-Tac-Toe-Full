from board import *


class Game:
    """Represents tic-tac-toe game"""
    def __init__(self):
        """Initialization"""
        self.mainboard = Board()
        # You can choose whether user starts first
        self.user_starts = True

    def play(self):
        """Main play function"""
        state = self.mainboard.has_winner()
        if not self.user_starts:
            print("Computer starts")
            self.mainboard.move_random()
            print(self.mainboard)
        else:
            print("User starts")
        while not state:
            suc = 1
            while suc:
                try:
                    coord = input("Enter coordinates: ").split()
                    self.mainboard.move((int(coord[0]), int(coord[1])))
                    suc = 0
                except CellIsNotEmptyError:
                    print("Cell is already taken. Try again.")
                except (ValueError, IndexError):
                    print("Invalid format (must be'1 2' for exp.). Try again.")

            print(self.mainboard)
            state = self.mainboard.has_winner()
            if state:
                break
            boards = []

            print("...computer is thinking...")
            for i in range(3):
                for j in range(3):
                    try:
                        temp = copy.deepcopy(self.mainboard)
                        temp.move((i, j))
                        boards.append(temp)
                    except:
                        pass
            maxik = -1000000
            bordik = self.mainboard
            for i in boards:
                score = i.compute_score()
                if score >= maxik:
                    maxik = score
                    bordik = i
            self.mainboard = bordik
            print("Computer's choice")
            print(self.mainboard)
            state = self.mainboard.has_winner()

        if state == 2:
            print("DRAW\nGame Over")
        elif state == 1:
            print("NOUGHT WINNER!\nGame Over")
        else:
            print("CROSS WINNER!\nGame Over")


if __name__ == "__main__":
    game = Game()
    game.play()
