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


font_setup = ("Comic Sans MS", 25, "normal")


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
        self.name = self.turtle + self.team
        self.turtle = t.Turtle()
        self.turtle.shape(self.team + "_" + self.piece + ".gif")
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(self.posX, self.posY)

        self.firstmove = True
        self.showingMoves = False
        self.possibleMoves = []
        self.possibleMovesX = 0
        self.possibleMovesY = 0

    def getPos(self):
        return self.turtle.xcor(), self.turtle.ycor()
    def getX(self):
        return self.turtle.xcor()
    def getY(self):
        return self.turtle.ycor()
    def showMoves(self):
        self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()+100)
        pos = self.turtle.xcor(), self.turtle.ycor()
        badMove = False
        print("check pos", pos)
        for piece in white_pieces:
            if pos == piece.getPos() and self.name != piece.name:
                print("bad move")
                badMove = True
        for piece in black_pieces:
            if pos == piece.getPos() and self.name != piece.name:
                print("bad move")
                badMove = True
        if not badMove:
            self.showingMoves = True
            if pos not in (self.possibleMovesX, self.possibleMovesY):
                self.possibleMoves.append(pos)
                self.possibleMovesX = self.turtle.xcor()
                self.possibleMovesY = self.turtle.ycor()
            self.turtle.shape("circle")
            self.turtle.color("grey") 
            self.stamp = self.turtle.stamp()        
            self.turtle.shape(self.team + "_" + self.piece + ".gif")
        self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()-100)
        
        if self.firstmove:
            self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()+200)
            pos = self.turtle.xcor(), self.turtle.ycor()
            badMove = False
            print("check pos", pos)
            for piece in white_pieces:
                if pos == piece.getPos() and self.name != piece.name:
                    print("bad move")
                    badMove = True
            for piece in black_pieces:
                if pos == piece.getPos() and self.name != piece.name:
                    print("bad move")
                    badMove = True
            if not badMove:
                self.showingMoves = True
                if pos not in (self.possibleMovesX, self.possibleMovesY):
                    self.possibleMoves.append(pos)
                    self.possibleMovesX = self.turtle.xcor()
                    self.possibleMovesY = self.turtle.ycor()
                self.turtle.shape("circle")
                self.turtle.color("grey") 
                self.stamp2 = self.turtle.stamp()        
                self.turtle.shape(self.team + "_" + self.piece + ".gif")
            self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()-200)
            self.firstmove = False


def move(turtle):
    turtle.goto(turtle.xcor(), turtle.ycor()+100)

class Pawn(Piece):
    def __init__(self, turtle, shape, team, posX, posY):
        super().__init__(turtle, shape, team, posX, posY)

    def possibleMoves(self):
        self.xcor

xcor = -350
ycor = 350
row = 0
col = 0
var = 0
for r in board:
    for c in r:
        c = t.Turtle()
        c.speed(0)
        c.penup()
        c.goto(xcor, ycor)
        c.shape("square")
        c.turtlesize(5)

        xcor += 100
        if col % 2 == 0:
            c.color("burlywood")
        else:
            c.color("brown")
       
        col += 1
    ycor -= 100
    xcor = -350
    col += 1
    row += 1

x = -390
y = 360
num = 8
for i in range(8):
    if i % 2 == 0:
        color = "brown"
    else:
        color = "burlywood"
    i = t.Turtle()
    i.speed(0)
    i.penup()
    i.color(color)
    i.hideturtle()
    i.goto(x, y)
    i.write(str(num), font=font_setup)
    y -= 100
    num -= 1

x = -325
y = -400
num = 0
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
for i in range(8):
    if i % 2 == 0:
        color = "burlywood"
    else:
        color = "brown"
    i = t.Turtle()
    i.speed(0)
    i.penup()
    i.color(color)
    i.hideturtle()
    i.goto(x, y)
    i.write(letters[num], font=font_setup)
    x += 100
    num += 1


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




def click_check(x, y):
    a = False
    print(x, y)
    for piece in white_pieces or black_pieces:
        a = True
        if piece.showingMoves:
            print(piece.possibleMovesX, piece.possibleMovesY)
            
            if x in range(piece.possibleMovesX - 50, piece.possibleMovesX + 50) and y in range(piece.possibleMovesY - 50, piece.possibleMovesY + 50):
                piece.turtle.goto(piece.possibleMovesX, piece.possibleMovesY)
                piece.showingMoves = False
                piece.turtle.clearstamp(piece.stamp)
                if piece.firstmove:
                    piece.turtle.clearstamp(piece.stamp2)
            else:
                piece.possibleMovesX = 0
                piece.possibleMovesY = 0
                piece.showingMoves = False
                piece.turtle.clearstamp(piece.stamp)
                if piece.firstmove:
                    piece.turtle.clearstamp(piece.stamp2)
            a = False

    if not piece.showingMoves and a:        
        for piece in white_pieces:
           if x in range(piece.getX()-50, piece.getX()+50) and y in range(piece.getY()-50, piece.getY()+50):
               print("white peice clicked")
               piece.showMoves()
        for piece in black_pieces:
           if x in range(piece.getX()-50, piece.getX()+50) and y in range(piece.getY()-50, piece.getY()+50):
               print("black peice clicked")
               piece.showMoves()

wn.onclick(click_check)
wn.mainloop()
