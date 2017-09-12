import gameConfig


class Person:
    # This class is making a person entity which is inherited by bomberman and
    # enemies

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = ['', '']
        

    def update_Cordinate(self):
        pass

    def get_pos(self):
        return self.position

    def set_Pos(self, x, y):
        self.position = [x, y]

    def left_Move(self):
        [x, y] = self.get_pos()
        if y-4 <2 or gameConfig.global_arr[x][y- 4] in self.ocuupied:
                pass
        else:
            self.set_Pos(x, y - 4)

    def right_Move(self):
        [x, y] = self.get_pos()
        if y+4 > 76 or gameConfig.global_arr[x][y+4] in self.ocuupied:
                pass
        else:
            self.set_Pos(x, y +4)
        
    def up_Move(self):
        [x, y] = self.get_pos()
        if x<3 or  gameConfig.global_arr[x-2][y] in self.ocuupied:
                pass
        else:
            self.set_Pos(x-2, y)

    def down_Move(self):
        [x, y] = self.get_pos()
        if x>36 or  gameConfig.global_arr[x+2][y] in self.ocuupied:
                pass
        else:
            self.set_Pos(x+2, y)