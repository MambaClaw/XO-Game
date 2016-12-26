import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

WIDTH = 200
HEIGHT = 200

RED = 1

BLUE = 2

MARGIN = 1

class MyApplication(arcade.Window):
    def __init__(self, width, height):
        self.TURN = 0
        self.player1Wins = False
        self.player2Wins = False

        super().__init__(width, height)

        self.Matrix = []

        for row in range(3):
            self.Matrix.append([])

            for column in range(3):
                self.Matrix[row].append(0)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        for row in range(3):
            for column in range(3):
                if self.Matrix[row][column] == RED:
                    color = arcade.color.RED
                elif self.Matrix[row][column] == BLUE:
                    color = arcade.color.BLUE
                else:
                    color = arcade.color.YELLOW
                    
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
                
                if self.player1Wins :
                    self.gameOver = arcade.Sprite('images/player1Wins.jpg')
                    self.gameOver.set_position(300, 300)
                    self.gameOver.draw()
                elif self.player2Wins :
                    self.gameOver = arcade.Sprite('images/player2Wins.jpg')
                    self.gameOver.set_position(300, 300)
                    self.gameOver.draw()
                elif(self.TURN == 9 and self.player1Wins == False and self.player2Wins == False):
                    self.gameOver = arcade.Sprite('images/draw.jpg')
                    self.gameOver.set_position(300, 300)
                    self.gameOver.draw()

    def on_mouse_press(self, x, y, button, modifiers):

        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        if(self.TURN%2 == 0 and self.Matrix[row][column] == 0):
            self.Matrix[row][column] = RED
            self.TURN += 1
        elif(self.TURN%2 == 1 and self.Matrix[row][column] == 0):
            self.Matrix[row][column] = BLUE
            self.TURN += 1

        if(self.Matrix[0][0] == 1 and self.Matrix[0][1] == 1 and self.Matrix[0][2] == 1):
            self.player1Wins = True
        elif(self.Matrix[1][0] == 1 and self.Matrix[1][1] == 1 and self.Matrix[1][2] == 1):
            self.player1Wins = True
        elif(self.Matrix[2][0] == 1 and self.Matrix[2][1] == 1 and self.Matrix[2][2] == 1):
            self.player1Wins = True
        elif(self.Matrix[0][0] == 1 and self.Matrix[1][0] == 1 and self.Matrix[2][0] == 1):
            self.player1Wins = True
        elif(self.Matrix[0][1] == 1 and self.Matrix[1][1] == 1 and self.Matrix[2][1] == 1):
            self.player1Wins = True
        elif(self.Matrix[0][2] == 1 and self.Matrix[1][2] == 1 and self.Matrix[2][2] == 1):
            self.player1Wins = True
        elif(self.Matrix[0][0] == 1 and self.Matrix[1][1] == 1 and self.Matrix[2][2] == 1):
            self.player1Wins = True
        elif(self.Matrix[0][2] == 1 and self.Matrix[1][1] == 1 and self.Matrix[2][0] == 1):
            self.player1Wins = True
        else: self.player1Wins = False

        if(self.Matrix[0][0] == 2 and self.Matrix[0][1] == 2 and self.Matrix[0][2] == 2):
            self.player2Wins = True
        elif(self.Matrix[1][0] == 2 and self.Matrix[1][1] == 2 and self.Matrix[1][2] == 2):
            self.player2Wins = True
        elif(self.Matrix[2][0] == 2 and self.Matrix[2][1] == 2 and self.Matrix[2][2] == 2):
            self.player2Wins = True
        elif(self.Matrix[0][0] == 2 and self.Matrix[1][0] == 2 and self.Matrix[2][0] == 2):
            self.player2Wins = True
        elif(self.Matrix[0][1] == 2 and self.Matrix[1][1] == 2 and self.Matrix[2][1] == 2):
            self.player2Wins = True
        elif(self.Matrix[0][2] == 2 and self.Matrix[1][2] == 2 and self.Matrix[2][2] == 2):
            self.player2Wins = True
        elif(self.Matrix[0][0] == 2 and self.Matrix[1][1] == 2 and self.Matrix[2][2] == 2):
            self.player2Wins = True
        elif(self.Matrix[0][2] == 2 and self.Matrix[1][1] == 2 and self.Matrix[2][0] == 2):
            self.player2Wins = True
        else: self.player2Wins = False
        
window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()
