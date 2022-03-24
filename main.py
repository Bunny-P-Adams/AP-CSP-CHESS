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

toMove = "white"

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
        self.alive = True
        self.possibleMovesX = []
        self.possibleMovesY = []

        if self.team == "white":
            self.allyPieces = white_pieces
            self.enemyPieces = black_pieces
            self.pawnDirection = 1
        else:
            self.allyPieces = black_pieces
            self.enemyPieces = white_pieces
            self.pawnDirection = -1

    def getPos(self):
        return self.turtle.xcor(), self.turtle.ycor()
    def getX(self):
        return self.turtle.xcor()
    def getY(self):
        return self.turtle.ycor()

    def pieceReset(self):
        self.turtle.clearstamps()
        self.possibleMovesX = []
        self.possibleMovesY = []
        self.showingMoves = False

    def stampMove(self):
        self.turtle.hideturtle()
        self.turtle.shape("circle")
        self.turtle.color("grey") 
        self.turtle.stamp()
        self.turtle.shape(self.shape)
        self.turtle.showturtle()
        self.possibleMovesX.append(self.getX())
        self.possibleMovesY.append(self.getY())
        self.showingMoves = True

    def basicMove(self, x, y):
        self.startPos = self.getPos()
        self.turtle.goto(self.getX()+100*x, self.getY()+100*y)
        if self.isMoveLegal():
            self.stampMove()
        self.turtle.goto(self.startPos)

    def axisMoves(self, x, y):
        self.startPos = self.getPos()
        for i in range(8):
            self.turtle.goto(self.getX()+100*x, self.getY()+100*y)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break
        self.turtle.goto(self.startPos)

    def isClicked(self, x, y):
        if x in range(self.turtle.xcor() - 50, self.turtle.xcor() + 50) and y in range(self.turtle.ycor() - 50, self.turtle.ycor() + 50):
            return True
        else:
            return False

    def isMoveLegal(self):
        for piece in self.allyPieces:
            if self.getPos() == piece.getPos() and self.name != piece.name:
                return False
        for piece in self.enemyPieces:
          if self.getPos() == piece.getPos() and self.name != piece.name:
              if self.piece != "pawn":
                  self.stampMove()
              return False
        if self.getX() > 350 or self.getX() < -350 or self.getY() > 350 or self.getY() < -350:
            return False
        else:
            return True

    def showLegalMoves(self):
        pass

    def move(self, x, y):
        global toMove
        for i in range(len(self.possibleMovesX)):
            if x in range(self.possibleMovesX[i] - 50, self.possibleMovesX[i] + 50) and y in range(self.possibleMovesY[i] - 50, self.possibleMovesY[i] + 50):
                self.turtle.goto(self.possibleMovesX[i], self.possibleMovesY[i])
                self.firstmove = False
                if self.team == "white":
                    toMove = "black"
                else:
                    toMove = "white"
      
        for piece in self.enemyPieces:
            if self.getPos() == piece.getPos():
                piece.alive = False
                piece.turtle.goto(-500, 0)
            else: 
                if self.getPos() == (piece.getX(), piece.getY()+100*self.pawnDirection) and self.piece == "pawn" and piece.piece == "pawn" and piece.enPassantAble:
                    piece.turtle.goto(-500, 0)
                    print(piece.getX(), piece.getY()-100)
                    print(self.getPos())
            piece.enPassantAble = False

        self.pieceReset()

class Pawn(Piece):
    def __init__(self, turtle, piece, team, posX, posY):
        super().__init__(turtle, piece, team, posX, posY)
        self.enPassantAble = False
        
    def showLegalMoves(self):
        self.startPos = self.getPos()
        
        self.turtle.goto(self.getX(), self.getY()+100*self.pawnDirection)
        
        if self.isMoveLegal():
            self.stampMove()
            if self.firstmove:
                self.turtle.goto(self.getX(), self.getY()+100*self.pawnDirection)
                if self.isMoveLegal():
                    self.stampMove()
        self.turtle.goto(self.startPos)
        self.turtle.goto(self.getX()+100*self.pawnDirection, self.getY()+100*self.pawnDirection)
        for piece in self.enemyPieces:
            if self.getPos() == piece.getPos():
                self.stampMove()
        self.turtle.goto(self.getX()-2*100*self.pawnDirection, self.getY())
        for piece in self.enemyPieces:
            if self.getPos() == piece.getPos():
                self.stampMove()
        self.turtle.goto(self.startPos)
        self.enPassantCheck()
    
    def enPassantCheck(self):
        for piece in self.enemyPieces:
            if self.getPos() == (piece.getX()+100, piece.getY()) or self.getPos() == (piece.getX()-100, piece.getY()) and self.piece == "pawn" and piece.piece == "pawn" and piece.enPassantAble and piece.firstMove: 
                self.startPos = self.getPos()
                self.turtle.goto(piece.getX(), piece.getY()+100*self.pawnDirection)
                self.stampMove()
                self.turtle.goto(self.startPos)
                
    def move(self, x, y):
        if self.firstmove:
            self.enPassantAble = True
        else:
            self.enPassantAble = False
        super().move(x, y)
    
class Bishop(Piece):
    def __init__(self, turtle, piece, team, posX, posY):
        super().__init__(turtle, piece, team, posX, posY)

    def showLegalMoves(self):
        self.axisMoves(1, 1)
        self.axisMoves(1, -1)
        self.axisMoves(-1, 1)
        self.axisMoves(-1, -1)

class Knight(Piece):
    def __init__(self, turtle, piece, team, posX, posY):
        super().__init__(turtle, piece, team, posX, posY)

    def showLegalMoves(self):
        self.basicMove(1, 2)
        self.basicMove(-1, 2)
        self.basicMove(1, -2)
        self.basicMove(-1, -2)
        self.basicMove(2, 1)
        self.basicMove(-2, 1)
        self.basicMove(2, -1)
        self.basicMove(-2, -1)
        
class Rook(Piece):
    def __init__(self, turtle, piece, team, posX, posY):
        super().__init__(turtle, piece, team, posX, posY)

    def showLegalMoves(self):
        self.axisMoves(0, 1)
        self.axisMoves(0, -1)
        self.axisMoves(1, 0)
        self.axisMoves(-1, 0)

class Queen(Piece):
    def __init__(self, turtle, piece, team, posX, posY):
        super().__init__(turtle, piece, team, posX, posY)
        
    def showLegalMoves(self):
        self.axisMoves(1, 1)
        self.axisMoves(1, -1)
        self.axisMoves(-1, 1)
        self.axisMoves(-1, -1)        
        self.axisMoves(0, 1)
        self.axisMoves(0, -1)
        self.axisMoves(1, 0)
        self.axisMoves(-1, 0)

class King(Piece):
    def __init__(self, turtle, piece, team, posX, posY):
        super().__init__(turtle, piece, team, posX, posY)
    
    def inCheck(self):
        print(self.enemyPieces)
        for piece in self.enemyPieces:
            print(1)
            piece.showLegalMoves()
            for i in range(len(piece.possibleMovesX)):
                if(self.getX == piece.possibleMovesX[i] and self.getY == piece.possibleMovesY[i]):
                    print("IN CHECK")
                    piece.pieceReset()
                    return True
        piece.pieceReset()
        return False
           
    
    def castle(self):
        x = self.getX()
        y = self.getY()
        start = (x, y)
        for piece in self.allyPieces:
            if piece.name[:5] == "arook":
                if piece.firstmove:
                    self.turtle.goto(x-100, y)
                    if self.isMoveLegal():
                        self.turtle.goto(x-200, y)
                        if self.isMoveLegal():
                            self.turtle.goto(x-300, y)
                            if self.isMoveLegal():
                                self.turtle.goto(x-200, y)
                                self.stampMove()
                self.turtle.goto(start)
            if piece.name[:5] == "hrook":
                if piece.firstmove:
                    self.turtle.goto(x+100, y)
                    if self.isMoveLegal():
                        self.turtle.goto(x+200, y)
                        if self.isMoveLegal():
                            self.stampMove()
                self.turtle.goto(start)


            
    def showLegalMoves(self):
        if (not self.inCheck()):
            self.basicMove(1, 0)
            self.basicMove(0, 1)
            self.basicMove(1, 1)
            self.basicMove(-1, 0)
            self.basicMove(0, -1)
            self.basicMove(-1, -1)
            self.basicMove(1, -1)
            self.basicMove(-1, 1)
            if self.firstmove:
                self.castle()

xcor = -350
ycor = 350
row = 0
col = 0
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
    
    if piece[1:] == "pawn":
        piece = Pawn(piece, piece[1:], "white", x, y)
    elif piece[1:] == "bishop":
        piece = Bishop(piece, piece[1:], "white", x, y)
    elif piece[1:] == "knight":
        piece = Knight(piece, piece[1:], "white", x, y)
    elif piece[1:] == "rook":
        piece = Rook(piece, piece[1:], "white", x, y)
    elif piece[1:] == "queen":
        piece = Queen(piece, piece[1:], "white", x, y)
    elif piece[1:] == "king":
        piece = King(piece, piece[1:], "white", x, y)
    
    white_pieces.append(piece)
    x += 100

x = -350
y = 250
for piece in piece_setup:
    if piece == "arook":
        y += 100
        x = -350

    if piece[1:] == "pawn":
        piece = Pawn(piece, piece[1:], "black", x, y)
    elif piece[1:] == "bishop":
        piece = Bishop(piece, piece[1:], "black", x, y)
    elif piece[1:] == "knight":
        piece = Knight(piece, piece[1:], "black", x, y)
    elif piece[1:] == "rook":
        piece = Rook(piece, piece[1:], "black", x, y)
    elif piece[1:] == "queen":
        piece = Queen(piece, piece[1:], "black", x, y)
    elif piece[1:] == "king":
        piece = King(piece, piece[1:], "black", x, y)

    black_pieces.append(piece)
    x += 100

def clickCheck(x, y):
    if toMove == "white":
        pieces = white_pieces
    else:
        pieces = black_pieces

    for piece in pieces:
        if piece.showingMoves:
            piece.move(x, y)
        else:
            if piece.isClicked(x, y):
                piece.showLegalMoves()

wn.onclick(clickCheck)
wn.mainloop()