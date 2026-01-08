from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    game.display()
    # Тут пользователь вводит координаты ячейки.
    row = int(input('Введите номер строки: '))
    if row < 0 or row >= game.field_size:
        raise FieldIndexError
    column = int(input('Введите номер столбца: '))
    if column < 0 or column >= game.field_size:
        raise FieldIndexError
    # В метод make_move передаются те координаты, которые ввёл пользователь.
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()


if __name__ == '__main__':
    main()
