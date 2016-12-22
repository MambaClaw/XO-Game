import arcade
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
w = 3
h = 3
Matrix = [[0 for x in range(w)] for y in range(h)]
class SpaceGameWindow(arcade.Window):
    WIDTH = 3
    LENGTH = 3
    P1Turn = True
    st = 0
    player1Wins = False
    player2Wins = False
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)
        self.table00_sprite = arcade.Sprite('images/assets/space.png')
        self.table01_sprite = arcade.Sprite('images/assets/space.png')
        self.table02_sprite = arcade.Sprite('images/assets/space.png')
        self.table10_sprite = arcade.Sprite('images/assets/space.png')
        self.table11_sprite = arcade.Sprite('images/assets/space.png')
        self.table12_sprite = arcade.Sprite('images/assets/space.png')
        self.table20_sprite = arcade.Sprite('images/assets/space.png')
        self.table21_sprite = arcade.Sprite('images/assets/space.png')
        self.table22_sprite = arcade.Sprite('images/assets/space.png')

        if(Matrix[0][0] == 1):
            self.table00_spite = arcade.Sprite('images/assets/x.png')
        if(Matrix[0][1] == 1):
            self.table01_sprite = arcade.Sprite('images/assets/x.png')
        if(Matrix[0][2] == 1):
            self.table02_sprite = arcade.Sprite('images/assets/x.png')
        if(Matrix[1][0] == 1):
            self.table10_sprite = arcade.Sprite('images/assets/x.png')
        if(Matrix[1][1] == 1):
            self.table11_sprite = arcade.Sprite('images/assets/x.png')
        if(Matrix[1][2] == 1):
            self.table12_sprite = arcade.Sprite('images/assets/x.png')
        if(Matrix[2][0] == 1):
            self.table20_sprite = arcade.Sprite('images/assets/x.png')
        if(Matrix[2][1] == 1):
            self.table21_sprite = arcade.Sprite('images/assets/x.png')
        if(Matrix[2][2] == 1):
            self.table22_sprite = arcade.Sprite('images/assets/x.png')

        if(Matrix[0][0] == 2):
            self.table00_spite = arcade.Sprite('images/assets/o.png')
        if(Matrix[0][1] == 2):
            self.table01_sprite = arcade.Sprite('images/assets/o.png')
        if(Matrix[0][2] == 2):
            self.table02_sprite = arcade.Sprite('images/assets/o.png')
        if(Matrix[1][0] == 2):
            self.table10_sprite = arcade.Sprite('images/assets/o.png')
        if(Matrix[1][1] == 2):
            self.table11_sprite = arcade.Sprite('images/assets/o.png')
        if(Matrix[1][2] == 2):
            self.table12_sprite = arcade.Sprite('images/assets/o.png')
        if(Matrix[2][0] == 2):
            self.table20_sprite = arcade.Sprite('images/assets/o.png')
        if(Matrix[2][1] == 2):
            self.table21_sprite = arcade.Sprite('images/assets/o.png')
        if(Matrix[2][2] == 2):
            self.table22_sprite = arcade.Sprite('images/assets/o.png')

        self.table00_sprite.set_position(100, 500)
        self.table10_sprite.set_position(100, 300)
        self.table20_sprite.set_position(100, 100)
        self.table01_sprite.set_position(300, 500)
        self.table11_sprite.set_position(300, 300)
        self.table21_sprite.set_position(300, 100)
        self.table02_sprite.set_position(500, 500)
        self.table12_sprite.set_position(500, 300)
        self.table22_sprite.set_position(500, 100)
        
 
    def on_draw(self):
        arcade.start_render()
        self.table00_sprite.draw()
        self.table01_sprite.draw()
        self.table02_sprite.draw()
        self.table10_sprite.draw()
        self.table11_sprite.draw()
        self.table12_sprite.draw()
        self.table20_sprite.draw()
        self.table21_sprite.draw()
        self.table22_sprite.draw()

    def calculate(self, delta):
        st = input()
        if(P1Turn):
            if(st=='q'):
                if(Matrix[0][0] == 0):
                    Matrix[0][0] = 1
                    P1Turn = False
            elif(st=='w'):
                if(Matrix[0][1] == 0):
                    Matrix[0][1] = 1
                    P1Turn = False
            elif(st=='e'):
                if(Matrix[0][2] == 0):
                    Matrix[0][2] = 1
                    P1Turn = False
            elif(st=='a'):
                if(Matrix[1][0] == 0):
                    Matrix[1][0] = 1
                    P1Turn = False
            elif(st=='s'):
                if(Matrix[1][1] == 0):
                    Matrix[1][1] = 1
                    P1Turn = False
            elif(st=='d'):
                if(Matrix[1][2] == 0):
                    Matrix[1][2] = 1
                    P1Turn = False
            elif(st=='z'):
                if(Matrix[2][0] == 0):
                    Matrix[2][0] = 1
                    P1Turn = False
            elif(st=='x'):
                if(Matrix[2][1] == 0):
                    Matrix[2][1] = 1
                    P1Turn = False
            elif(st=='c'):
                if(Matrix[2][2] == 0):
                    Matrix[2][2] = 1
                    P1Turn = False
        if(P1Turn == False):
            if(st=='u'):
                if(Matrix[0][0] == 0):
                    Matrix[0][0] = 2
                    P1Turn = True
            elif(st=='i'):
                if(Matrix[0][1] == 0):
                    Matrix[0][1] = 2
                    P1Turn = True
            elif(st=='o'):
                if(Matrix[0][2] == 0):
                    Matrix[0][2] = 2
                    P1Turn = True
            elif(st=='h'):
                if(Matrix[1][0] == 0):
                    Matrix[1][0] = 2
                    P1Turn = True
            elif(st=='j'):
                if(Matrix[1][1] == 0):
                    Matrix[1][1] = 2
                    P1Turn = True
            elif(st=='k'):
                if(Matrix[1][2] == 0):
                    Matrix[1][2] = 2
                    P1Turn = True
            elif(st=='b'):
                if(Matrix[2][0] == 0):
                    Matrix[2][0] = 2
                    P1Turn = True
            elif(st=='n'):
                if(Matrix[2][1] == 0):
                    Matrix[2][1] = 2
                    P1Turn = True
            elif(st=='m'):
                if(Matrix[2][2] == 0):
                    Matrix[2][2] = 2
                    P1Turn = True
        checkTable()

    def checkTable(self, delta):
        if(Matrix[0][0] == 1 and Matrix[0][1] == 1 and Matrix[0][2] == 1):
            player1Wins = True
        if(Matrix[1][0] == 1 and Matrix[1][1] == 1 and Matrix[1][2] == 1):
            player1Wins = True
        if(Matrix[2][0] == 1 and Matrix[2][1] == 1 and Matrix[2][2] == 1):
            player1Wins = True
        if(Matrix[0][0] == 1 and Matrix[1][0] == 1 and Matrix[2][0] == 1):
            player1Wins = True
        if(Matrix[0][1] == 1 and Matrix[1][1] == 1 and Matrix[2][1] == 1):
            player1Wins = True
        if(Matrix[0][2] == 1 and Matrix[1][2] == 1 and Matrix[2][2] == 1):
            player1Wins = True
        if(Matrix[0][0] == 1 and Matrix[1][1] == 1 and Matrix[2][2] == 1):
            player1Wins = True
        if(Matrix[0][2] == 1 and Matrix[1][1] == 1 and Matrix[2][0] == 1):
            player1Wins = True
            
        if(Matrix[0][0] == 2 and Matrix[0][1] == 2 and Matrix[0][2] == 2):
            player2Wins = True
        if(Matrix[1][0] == 2 and Matrix[1][1] == 2 and Matrix[1][2] == 2):
            player2Wins = True
        if(Matrix[2][0] == 2 and Matrix[2][1] == 2 and Matrix[2][2] == 2):
            player2Wins = True
        if(Matrix[0][0] == 2 and Matrix[1][0] == 2 and Matrix[2][0] == 2):
            player2Wins = True
        if(Matrix[0][1] == 2 and Matrix[1][1] == 2 and Matrix[2][1] == 2):
            player2Wins = True
        if(Matrix[0][2] == 2 and Matrix[1][2] == 2 and Matrix[2][2] == 2):
            player2Wins = True
        if(Matrix[0][0] == 2 and Matrix[1][1] == 2 and Matrix[2][2] == 2):
            player2Wins = True
        if(Matrix[0][2] == 2 and Matrix[1][1] == 2 and Matrix[2][0] == 2):
            player2Wins = True

class Table:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def animate(self, delta):
        pass
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
