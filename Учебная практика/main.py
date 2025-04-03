# main.py
from game import Game
from ai import AI


def main():
    print("Добро пожаловать в игру Крестики-нолики!")
    mode = input("Выберите режим игры (1 - два игрока, 2 - против компьютера): ")
    if mode == "2":
        level = int(
            input(
                "Выберите уровень сложности AI (1 - легкий, 2 - средний, 3 - сложный): "
            )
        )
        game = Game(against_ai=True, ai_level=level)
    else:
        game = Game()

    game.play()


if __name__ == "__main__":
    main()
