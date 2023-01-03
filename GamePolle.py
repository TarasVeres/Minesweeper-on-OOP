from random import randint

from Cell import *

class GamePolle: # ігрове поле
    def __init__(self, N, M):
        self.N = N  # розмір поля N x N
        self.M = M  # кількість мін на полі
        self.pole = [[Cell() for _ in range(N)]for _ in range(N)]
        self.init()
        self.counter_mine()

    def init(self):  # рандомно розкинути міни по полю
        for i in range(self.M):
            while True:
                random_mine_line, random_mine_colum = randint(0, self.N-1), randint(0, self.N-1)
                if not self.pole[random_mine_line][random_mine_colum].mine:
                    self.pole[random_mine_line][random_mine_colum].mine = True
                    break
                else:
                    pass

    def show(self):  # відображення поля в консолі у вигляді таблиці чисел відкритих клітинок( якщо клітинка закрита - # )
        print_pole = [['#' for _1 in range(self.N)]for _ in range(self.N)]
        for i in range(self.N):
            for l in range(self.N):
                if self.pole[i][l].fl_open:
                    if self.pole[i][l].mine:
                        print_pole[i][l] = '*'
                    else:
                        print_pole[i][l] = self.pole[i][l].around_mines
        for _ in print_pole:
            print(*_)

    def counter_mine(self):  # підрахунок кількості мін навколо клітинки
        for rows in range(self.N):
            for columns in range(self.N):
                if not self.pole[rows][columns].mine:
                    count = [-1, 0, 1]
                    for i in count:
                        for li in count:
                            if (0 <= (rows + i) < self.N) and (0 <= (columns + li) < self.N):
                                try:
                                    if self.pole[rows+i][columns+li].mine:
                                        self.pole[rows][columns].around_mines += 1
                                except IndexError:
                                    pass

    def game_player(self, x, y):  # функція на відкриття клітинки якщо на неї походив гравець
        self.pole[x][y].fl_open = True
        if self.pole[x][y].mine:
            return False
        return True

# [
#     [0, 0, 0],
#     [0, 1, 1],
#     [0, 1, *]
# ]