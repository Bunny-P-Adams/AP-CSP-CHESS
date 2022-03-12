import turtle as t

t.tracer(1, 0)

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
        self.shape = self.team + "_" + self.piece + ".gif"
        self.turtle.shape(self.shape)
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(self.posX, self.posY)

        self.firstmove = True
        self.showingMoves = False
        self.possibleMoves = []
        self.possibleMovesX = []
        self.possibleMovesY = []

    def getPos(self):
        return self.turtle.xcor(), self.turtle.ycor()
    def getX(self):
        return self.turtle.xcor()
    def getY(self):
        return self.turtle.ycor()

    def stampMove(self):
        self.turtle.hideturtle()
        self.turtle.shape("circle")
        self.turtle.color("grey") 
        self.stamp = self.turtle.stamp()
        
        self.turtle.shape(self.shape)
        self.turtle.showturtle()

        
        self.possibleMovesX.append(self.getX())
        self.possibleMovesY.append(self.getY())

    def isMoveLegal(self):
        #pass
        for piece in white_pieces:
            print(self.getPos(), "\n", piece.getPos())
            if self.getPos() == piece.getPos() and self.name != piece.name:
                print("ILLEGAL")
                return False
            else:
                print("legal")
                self.possibleMovesX.append(self.getX())
                self.possibleMovesY.append(self.getY())
                return True
                

    def showLegalMoves(self):
        #pass
                
        self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()+100)
        if self.isMoveLegal():
            self.stampMove()
            self.showingMoves = True
            if self.firstmove:
                if self.isMoveLegal():
                    self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()+100)
                    self.stampMove()
                    self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()-100)
        
        self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()-100)

    def pieceReset(self):
        self.turtle.clearstamps()
        self.possibleMovesX = []
        self.possibleMovesY = []
        self.possibleMoves = []
        self.showingMoves = False
    
    def isClicked(self, x, y):
        if x in range(self.getX() - 50, self.getX() + 50) and y in range(self.getY() - 50, self.getY() + 50):
            return True
        else:
            return False

    def move(self, x, y):
        for i in range(len(self.possibleMovesX)):
            if x in range(self.possibleMovesX[i] - 50, self.possibleMovesX[i] + 50) and y in range(self.possibleMovesY[i] - 50, self.possibleMovesY[i] + 50):
                self.turtle.goto(self.possibleMovesX[i], self.possibleMovesY[i])
                self.firstmove = False
        self.pieceReset()

    '''def showMoves(self):
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
                self.possibleMovesX.append(self.turtle.xcor())
                self.possibleMovesY.append(self.turtle.ycor())
            self.turtle.shape("circle")
            self.turtle.color("grey") 
            self.stamp = self.turtle.stamp()        
            self.turtle.shape(self.team + "_" + self.piece + ".gif")
        self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()-100)
        
        if self.firstmove:
            self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()+200)
            pos = self.turtle.xcor(), self.turtle.ycor()
            badMove = False
            
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
                    self.possibleMovesX.append(self.turtle.xcor())
                    self.possibleMovesY.append(self.turtle.ycor())
                self.turtle.shape("circle")
                self.turtle.color("grey") 
                self.stamp2 = self.turtle.stamp()        
                self.turtle.shape(self.team + "_" + self.piece + ".gif")
            self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()-200)
        '''    

class Pawn(Piece):
    def __init__(self, turtle, shape, team, posX, posY):
        super().__init__(turtle, shape, team, posX, posY)

    def getPos(self):
        return super().getPos()

    def stampMove(self):
        return super().stampMove()
    
    def checkMove(self):
        for piece in white_pieces:
            if self.getPos() == piece.getPos() and self.name != piece.name:
                print("illegal move")
        for piece in black_pieces:
            if self.getPos() == piece.getPos() and self.name != piece.name:
                print("illegal move")

    def showLegalMoves(self):
        self.turtle.goto(self.turtle.xcor(), self.turtle.ycor()+100)
        self.stampMove()

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
# white_pawn = Piece("pawn", "pawn", "white", x, y)
# white_pieces.append(white_pawn)
# x = -350
# y = 250
# black_pawn = Piece("pawn", "pawn", "black", x, y)
# black_pieces.append(black_pawn)
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




def clickCheck(x, y):
    '''
    for piece in white_pieces or black_pieces:
        a = True
        if piece.showingMoves:
            print(piece.possibleMovesX, piece.possibleMovesY)
            for i in range(len(piece.possibleMoves)):
                print(piece.possibleMoves)
                print(i, piece.possibleMovesX)
                if x in range(piece.possibleMovesX[i] - 50, piece.possibleMovesX[i] + 50) and y in range(piece.possibleMovesY[i] - 50, piece.possibleMovesY[i] + 50):
                    piece.turtle.goto(piece.possibleMovesX[i], piece.possibleMovesY[i])
                    piece.showingMoves = False
                    piece.firstmove = False
                    piece.turtle.clearstamp(piece.stamp)
                    piece.turtle.clearstamp(piece.stamp2)
                    piece.possibleMovesX = []
                    piece.possibleMovesY = []
                else:
                    piece.possibleMovesX = []
                    piece.possibleMovesY = []
                    piece.showingMoves = False
                    piece.turtle.clearstamp(piece.stamp)
                    piece.turtle.clearstamp(piece.stamp2)
            a = False
    '''
    
    for piece in white_pieces:
        if piece.showingMoves:
            piece.move(x, y)
        else:
            if piece.isClicked(x, y):
                piece.showLegalMoves()


wn.onclick(clickCheck)
wn.mainloop()
