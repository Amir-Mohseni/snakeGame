import consts


class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        next_place = self.get_head()
        next_place = (next_place[0] + self.dx[self.direction] + self.game.size, next_place[1] + self.dy[self.direction] + self.game.size)

        next_place = next_place[0] % self.game.size, next_place[1] % self.game.size


        if self.game.get_cell(next_place).color != consts.back_color and self.game.get_cell(next_place).color != consts.fruit_color:
            self.game.kill(self)
        else:
            self.cells.append(next_place)
            if self.game.get_cell(next_place).color == consts.back_color:
                self.game.get_cell(self.cells[0]).set_color(consts.back_color)
                self.cells = self.cells[1:]
            self.game.get_cell(next_place).set_color(self.color)

    def handle(self, keys):
        for key in keys:
            if key in self.keys:
                if self.dx[self.keys[key]] == -self.dx[self.direction] and self.dy[self.keys[key]] == -self.dy[self.direction]:
                    continue
                if self.dx[self.keys[key]] == self.dx[self.direction] and self.dy[self.keys[key]] == self.dy[self.direction]:
                    continue
                self.direction = self.keys[key]
                break
