class Cell:   #управління клітинкой ігрового поля
    def __init__(self, around_mines=0, mine=False, fl_open=False):
        self.around_mines = around_mines  # число мін навколо клітинки
        self.mine = mine  # наявність міни в клітинці
        self.fl_open = fl_open  # закрита чи відкрита клітинка для відображення
