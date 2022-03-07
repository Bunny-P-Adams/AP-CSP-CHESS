import turtle as t

board = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
         ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
         ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
         ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
         ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
         ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
         ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
         ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]

chess_pieces = ["white_pawn.gif", "black_pawn.gif", "white_bishop.gif", "black_bishop.gif", "white_knight.gif", "black_knight.gif",
                "white_rook.gif", "black_rook.gif", "white_queen.gif", "black_queen.gif", "white_king.gif", "black_king.gif"]

piece_setup = ["apawn", "bpawn", "cpawn", "dpawn", "epawn", "fpawn", "gpawn", "hpawn",
               "arook", "bknight", "cbishop", "dqueen", "eking", "fbishop", "gknight", "hrook"]

white_pieces = []
black_pieces = []

wn = t.Screen()
wn.bgcolor("black")
for piece in chess_pieces:
    wn.addshape(piece)


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

xcor = -350
ycor = -350
row = 0
col = 0
for r in board:
    for c in r:
        c = t.Turtle()
        c.shape("square")
        c.turtlesize(5)
        c.penup()
        c.speed(0)
        c.goto(xcor, ycor)
        xcor += 100
        
        if col % 2 == 0:
            c.color("burlywood")
        else:
            c.color("brown")
       
        col += 1
    ycor += 100
    xcor = -350
    col += 1
    row += 1


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

gameActive = True
while gameActive:
    turn = 0
    if turn % 2 == 0:
        for piece in white_pieces:
            piece.turtle.ondrag(piece.turtle.goto)
    else:
        for piece in black_pieces:
            piece.turtle.ondrag(piece.turtle.goto)

    turn += 1

wn.mainloop()
