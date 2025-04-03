# game.py
class Game:
    def __init__(self, against_ai=False, ai_level=1):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # Игровое поле
        self.current_player = 'X'  # Текущий игрок ('X' или 'O')
        self.against_ai = against_ai  # Режим игры с компьютером
        self.ai_level = ai_level  # Уровень сложности AI

    def display_board(self):
        """Вывод игрового поля в консоль."""
        print("\n")
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)
        print("\n")

    def make_move(self, row, col):
        """Выполнение хода."""
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_win(self, player):
        """Проверка победы."""
        # Проверка строк, столбцов и диагоналей
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        """Проверка ничьей."""
        return all(cell != ' ' for row in self.board for cell in row)

    def switch_player(self):
        """Смена игрока."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        """Основной цикл игры."""
        while True:
            self.display_board()
            if self.against_ai and self.current_player == 'O':
                # Ход компьютера
                print("Ход компьютера...")
                row, col = self.get_ai_move()
            else:
                # Ход игрока
                print(f"Ход игрока {self.current_player}. Введите строку и столбец (0-2): ")
                try:
                    row, col = map(int, input().split())
                except ValueError:
                    print("Неверный ввод! Попробуйте снова.")
                    continue

            if not self.make_move(row, col):
                print("Невалидный ход! Попробуйте снова.")
                continue

            if self.check_win(self.current_player):
                self.display_board()
                print(f"Игрок {self.current_player} победил!")
                break

            if self.check_draw():
                self.display_board()
                print("Ничья!")
                break

            self.switch_player()

    def get_ai_move(self):
        """Получение хода компьютера."""
        # Простая реализация для примера
        import random
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        return random.choice(empty_cells)