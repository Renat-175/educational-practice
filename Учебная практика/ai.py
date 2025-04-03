# ai.py
import random


class AI:
    def __init__(self, level=1):
        self.level = level

    def get_best_move(self, game):
        """Получение лучшего хода."""
        if self.level == 1:
            return self.random_move(game)
        elif self.level == 2:
            return self.medium_move(game)
        elif self.level == 3:
            return self.minimax_move(game)

    def random_move(self, game):
        """Случайный ход."""
        empty_cells = [
            (i, j) for i in range(3) for j in range(3) if game.board[i][j] == " "
        ]
        return random.choice(empty_cells)

    def medium_move(self, game):
        """Ход средней сложности."""
        # Попытка блокировать победу игрока
        for i in range(3):
            for j in range(3):
                if game.board[i][j] == " ":
                    game.board[i][j] = "O"
                    if game.check_win("O"):
                        game.board[i][j] = " "
                        return i, j
                    game.board[i][j] = " "

        for i in range(3):
            for j in range(3):
                if game.board[i][j] == " ":
                    game.board[i][j] = "X"
                    if game.check_win("X"):
                        game.board[i][j] = " "
                        return i, j
                    game.board[i][j] = " "

        return self.random_move(game)

    def minimax_move(self, game):
        """Минимаксный алгоритм."""
        best_score = float("-inf")
        best_move = None

        for i in range(3):
            for j in range(3):
                if game.board[i][j] == " ":
                    game.board[i][j] = "O"
                    score = self.minimax(game, False)
                    game.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        return best_move

    def minimax(self, game, is_maximizing):
        """Реализация минимаксного алгоритма."""
        if game.check_win("O"):
            return 1
        if game.check_win("X"):
            return -1
        if game.check_draw():
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(3):
                for j in range(3):
                    if game.board[i][j] == " ":
                        game.board[i][j] = "O"
                        score = self.minimax(game, False)
                        game.board[i][j] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if game.board[i][j] == " ":
                        game.board[i][j] = "X"
                        score = self.minimax(game, True)
                        game.board[i][j] = " "
                        best_score = min(score, best_score)
            return best_score
