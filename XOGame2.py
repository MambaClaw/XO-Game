import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 200
HEIGHT = 200

# This sets the margin between each cell
MARGIN = 1


class MyApplication(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        self.TURN = 0
        self.player1Wins = False
        self.player2Wins = False
        """
        Set up the application.
        """
        super().__init__(width, height)
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.Matrix = []
        for row in range(3):
            # Add an empty array that will hold each cell
            # in this row
            self.Matrix.append([])
            for column in range(3):
                self.Matrix[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid

        for row in range(3):
            for column in range(3):
                # Figure out what color to draw the box
                if self.Matrix[row][column] == 1:
                    color = arcade.color.BLACK
                elif self.Matrix[row][column] == 2:
                    color = arcade.color.WHITE
                else:
                    color = arcade.color.GRAY

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
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
                    self.gameOver.set_position(600, 600)
                    self.gameOver.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        # Set that location to one
        if(self.TURN%2 == 0 and self.Matrix[row][column] == 0):
            self.Matrix[row][column] = 1
            self.TURN += 1
        elif(self.TURN%2 == 1 and self.Matrix[row][column] == 0):
            self.Matrix[row][column] = 2
            self.TURN += 1
        print("Click coordinates: ({}, {}). Grid coordinates: ({}, {})"
              .format(x, y, row, column))
        print(self.TURN)

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

        print (self.Matrix)
        print (self.player1Wins)
        print (self.player2Wins)
        print (self.TURN)


window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()
