from random import randint
from math import ceil

from GamePolle import GamePolle

class Play:  # клас самої гри
    def __init__(self, level=0, mine=0, pole=0, winer=True):
        self.pole = pole
        self.mine = mine
        self.level = level
        self.winer = winer
        self.go_play()

    def go_run(self):  # визначення розміру ігрового поля та складності гри
        print('Введіть бажаний розмір поля (кількість клітинок в рядку та стовпчику)  від 3 до 20:')
        while True:
            pole = input()
            if pole.isnumeric():
                pole = int(pole)
                if 3 <= pole <= 20:
                    self.pole = pole
                    break
                else:
                    print('Ви ввели невірну кількість, введіть цифру від 3 до 20')
            else:
                print('Введіть будь ласка цифру (ціле число від 3 до 20):')

        print('Оберіть рівень складності:\n'
              'Легкий (мін на полі від 1% до 15%) - 1\n'
              'Середній (мін на полі від 15% до 30%) - 2\n'
              'Складний (мін на полі від 30% до 50%) - 3')
        while True:
            level = input()
            if level.isnumeric():
                level = int(level)
                if 1 <= level <= 3:
                    self.level = level
                    break
                else:
                    print('Ви ввели невірну кількість, введіть цифру від 1 до 3')
            else:
                print('Введіть будь ласка цифру (ціле число від 1 до 3):')

    def mine_random(self):  # рандомне визначення кількості мін залежно від рівня складності
        global count_min, count_max
        if self.level == 1:
            count_min, count_max = 1, ceil(self.pole * 0.15)
        elif self.level == 2:
            count_min, count_max = ceil(self.pole * 0.15), ceil(self.pole * 0.3)
        elif self.level == 3:
            count_min, count_max = ceil(self.pole * 0.3), ceil(self.pole * 0.5)
        self.mine = randint(count_min, count_max)
        print(self.mine)

    def check_cell_open(self, game_pole):
        count = 0
        for i in range(self.pole):
            for l in range(self.pole):
                if not game_pole.pole[i][l].fl_open:
                    if not game_pole.pole[i][l].mine:
                        count += 1
        if count > 0:
            pass
        else:
            game_pole.show()
            self.check_winer()


    def go_play(self):  # запуск гри
        print('Вітаємо вас у грі сапер!')
        self.go_run()
        self.mine_random()
        play = GamePolle(self.pole, self.mine)
        while True:
            play.show()
            while True:
                global step_player
                try:
                    step_player = list(map(int, input().split()))
                    if len(step_player) == 2:
                        if (0 < step_player[0] <= self.pole) and (0 < step_player[1] <= self.pole):
                            step_player = play.game_player(step_player[0]-1, step_player[1]-1)
                            break
                        else:
                            print(f'Введіть числа координат, кожне з яких більше 0 та не більше {self.pole}:')
                    else:
                        print('Введіть два числа:')
                except ValueError:
                    print('Введіть будь ласка цифри:')
            self.check_cell_open(play)
            if not step_player:
                self.winer = False
                play.show()
                self.check_winer()




    def check_winer(self):  # запит на нову гру
        finish = 'Ви перемогли!' if self.winer else 'Нажаль ви програли!'
        print(finish + ' Бажаєте зіграти ще (Так/Ні)?')
        while True:
            next_game = input()
            if str(next_game).lower() in 'так':
                self.go_play()
                break
            elif str(next_game).lower() in 'ні':
                print('Бувайте здорові!')
                exit()
            else:
                print('Бажаєте зіграти ще (Так/Ні)?')

start = Play()











# c1 = Cell (around_mines, mine)
# pole_game = GamePole(N=10, M=12)