import turtle as t
t.speed("fastest")
#t.tracer(0,0)
# chess piece images
chess_pieces = ["white_pawn.gif", "black_pawn.gif", "white_bishop.gif", "black_bishop.gif", "white_knight.gif", "black_knight.gif",
                "white_rook.gif", "black_rook.gif", "white_queen.gif", "black_queen.gif", "white_king.gif", "black_king.gif"]

# screen init
wn = t.Screen()
wn.bgcolor("black")
for piece in chess_pieces:
    wn.addshape(piece)

s = t.Turtle()
s.shape("square")
s.color("burlywood")
s.penup()
s.turtlesize(5)
s.goto(-350, -350)
s.speed(0)


class Piece:
    def __init__(self, turtle, piece, team, posX, posY):
        self.turtle = turtle
        self.piece = piece
        self.team = team
        self.posX = posX
        self.posY = posY
        turtle = t.Turtle()
        turtle.shape(team + "_" + piece + ".gif")
        turtle.penup()
        turtle.speed(0)
        turtle.goto(posX, posY)


'''class Pawn(Piece):
    def __init__(self, turtle, shape, team, posX, posY):
        super().__init__(turtle, shape, team, posX, posY)
'''

#board = [["" for i in range(8)] for i in range(8)]
board = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
         ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
         ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
         ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
         ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
         ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
         ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
         ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]

for r in board:
    for c in r:
        print(c)
        c = t.Turtle()
        c.shape("square")
'''
x = 0
y = 0
num = 8
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
for i in range(64):
    #TODO: array of turtles for chess board
    #name = letters[y] + str(num)
    
    name = board[x][y]
    name = t.Turtle()
    board[x][y] = t.Turtle()
    print(board[x][y])
    y += 1
    i += 1
    if i % 2 == 0:
        board[x][y].color("burlywood")
    else:
        board[x][y].color("brown")
    if i % 8 == 0:
        x += 1
        y = 0
        num -= 1
'''
x = 100

for i in range(1, 64):
    s.stamp()

    s.goto(s.xcor()+x, s.ycor())
    
    if i % 2 == 0:
        s.color("burlywood")
    else:
        s.color("brown")
    if i % 8 == 0:
        if i % 16 == 0:
            s.goto(s.xcor()+100, s.ycor()+100)
        else:
            s.goto(s.xcor()-100, s.ycor()+100)
        x *= -1

    

piece_setup = ["apawn", "bpawn", "cpawn", "dpawn", "epawn", "fpawn", "gpawn", "hpawn",
               "arook", "bknight", "cbishop", "dqueen", "eking", "fbishop", "gknight", "hrook"]

white_pieces = []
black_pieces = []

x = -350
y = -250
for piece in piece_setup:
    if piece == "arook":
        y -= 100
        x = -350
    piece = Piece(piece, piece[1:], "white", x, y)
    white_pieces.append(piece)
    x += 100

x = -350
y = 250
for piece in piece_setup:
    if piece == "arook":
        y += 100
        x = -350
    piece = Piece(piece, piece[1:], "black", x, y)
    black_pieces.append(piece)
    x += 100

for i in white_pieces:
    print(i.turtle)

#t.update()
wn.mainloop()

