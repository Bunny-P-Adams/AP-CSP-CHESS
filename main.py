import turtle as t
from xml.etree.ElementTree import PI

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

toMove = True

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

        self.possibleMovesX = []
        self.possibleMovesY = []

        if self.team == "white":
            self.allyPieces = white_pieces
            self.enemyPieces = black_pieces
            self.m = 100
        else:
            self.allyPieces = black_pieces
            self.enemyPieces = white_pieces
            self.m = -100

    def getPos(self, piece):
        return piece.turtle.xcor(), piece.turtle.ycor()
    def getX(self,):
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
        self.stamp = self.turtle.stamp()
        
        self.turtle.shape(self.shape)
        self.turtle.showturtle()

        
        self.possibleMovesX.append(self.getX())
        self.possibleMovesY.append(self.getY())


    def isClicked(self, x, y):
        if x in range(self.turtle.xcor() - 50, self.turtle.xcor() + 50) and y in range(self.turtle.ycor() - 50, self.turtle.ycor() + 50):
            return True
        else:
            return False

    def isMoveLegal(self):
        
        print("checking...")
        for piece in self.allyPieces:
            if self.getPos() == piece.getPos() and self.name != piece.name:
                print("ILLEGAL")
                return False

        if self.getX() > 350 or self.getX() < -350 or self.getY() > 350 or self.getY() < -350:
            print("ILLEGAL")
            return False

        else:
            print("legal")
            self.possibleMovesX.append(self.getX())
            self.possibleMovesY.append(self.getY())
            return True

    def showLegalMoves(self):
        pass

    # def showCaptures(self):
    #     pass

    def move(self, x, y):
        global toMove
        for i in range(len(self.possibleMovesX)):
            if x in range(self.possibleMovesX[i] - 50, self.possibleMovesX[i] + 50) and y in range(self.possibleMovesY[i] - 50, self.possibleMovesY[i] + 50):
                self.turtle.goto(self.possibleMovesX[i], self.possibleMovesY[i])
                self.firstmove = False
                toMove = not toMove
      
        for piece in self.enemyPieces:
            if self.getPos() == piece.getPos():
                piece.turtle.goto(-500, 0)
              
        self.pieceReset()

class Pawn(Piece):
    def __init__(self, turtle, piece, team, posX, posY):
        super().__init__(turtle, piece, team, posX, posY)

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
        self.stamp = self.turtle.stamp()
        
        self.turtle.shape(self.shape)
        self.turtle.showturtle()

        
        self.possibleMovesX.append(self.getX())
        self.possibleMovesY.append(self.getY())

        self.showingMoves = True

    def isClicked(self, x, y):
        if x in range(self.getX() - 50, self.getX() + 50) and y in range(self.getY() - 50, self.getY() + 50):
            return True
        else:
            return False
    def isMoveLegal(self):
        
        for piece in self.allyPieces:
            if self.getPos() == piece.getPos() and self.name != piece.name:
                print("ILLEGAL")
                return False

        for piece in self.enemyPieces:
          if self.getPos() == piece.getPos() and self.name != piece.name:
              print("ILLEGAL")
              return False

        if self.getX() > 350 or self.getX() < -350 or self.getY() > 350 or self.getY() < -350:
            print("ILLEGAL")
            return False

        else:
            print("legal")
            return True
       

    def showLegalMoves(self):
        
        print("SHOWING")
        self.turtle.goto(self.getX(), self.getY()+self.m)
        
        if self.isMoveLegal():
            self.stampMove()
            if self.firstmove:
                self.turtle.goto(self.getX(), self.getY()+self.m)
                if self.isMoveLegal():
                    self.stampMove()
                self.turtle.goto(self.getX(), self.getY()-self.m)
        
        self.turtle.goto(self.getX(), self.getY()-self.m)

        self.showPawnCaptures()

    def showPawnCaptures(self):
        self.startPos = self.getPos()

        self.turtle.goto(self.getX()+self.m, self.getY()+self.m)
        for piece in self.enemyPieces:
            if self.getPos() == piece.getPos():
                self.stampMove()
        self.turtle.goto(self.getX()-2*self.m, self.getY())
        for piece in self.enemyPieces:
            if self.getPos() == piece.getPos():
                self.stampMove()

        self.turtle.goto(self.startPos)

    def move(self, x, y):
        super().move(x, y)
    
class Bishop(Piece):
    def __init__(self, turtle, piece, team, posX, posY):
        super().__init__(turtle, piece, team, posX, posY)
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
        self.stamp = self.turtle.stamp()
        
        self.turtle.shape(self.shape)
        self.turtle.showturtle()

        
        self.possibleMovesX.append(self.getX())
        self.possibleMovesY.append(self.getY())

        self.showingMoves = True


    def isClicked(self, x, y):
        if x in range(self.turtle.xcor() - 50, self.turtle.xcor() + 50) and y in range(self.turtle.ycor() - 50, self.turtle.ycor() + 50):
            return True
        else:
            return False

    def isMoveLegal(self):
        
        print("checking...")
        for piece in self.allyPieces:
            if self.getPos() == piece.getPos() and self.name != piece.name:
                print("ILLEGAL")
                return False
        
        for piece in self.enemyPieces:
          if self.getPos() == piece.getPos() and self.name != piece.name:
              print("CAPTURE")
              self.stampMove()
              return False

        if self.getX() > 350 or self.getX() < -350 or self.getY() > 350 or self.getY() < -350:
            print("ILLEGAL")
            return False

        else:
            print("legal")
            return True
    def showLegalMoves(self):

        self.startPos = self.getPos()

        for i in range(8):
            self.turtle.goto(self.getX()+100, self.getY()+100)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break

        self.turtle.goto(self.startPos)

        for i in range(8):
            self.turtle.goto(self.getX()+100, self.getY()-100)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break

        self.turtle.goto(self.startPos)

        for i in range(8):
            self.turtle.goto(self.getX()-100, self.getY()+100)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break

        self.turtle.goto(self.startPos)

        for i in range(8):
            self.turtle.goto(self.getX()-100, self.getY()-100)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break


        self.turtle.goto(self.startPos)

    def move(self, x, y):
        super().move(x, y)

class Knight(Piece):
    def __init__(self, turtle, piece, team, posX, posY):
        super().__init__(turtle, piece, team, posX, posY)
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
        self.stamp = self.turtle.stamp()
        
        self.turtle.shape(self.shape)
        self.turtle.showturtle()

        
        self.possibleMovesX.append(self.getX())
        self.possibleMovesY.append(self.getY())

        self.showingMoves = True


    def isClicked(self, x, y):
        if x in range(self.turtle.xcor() - 50, self.turtle.xcor() + 50) and y in range(self.turtle.ycor() - 50, self.turtle.ycor() + 50):
            return True
        else:
            return False

    def isMoveLegal(self):
        
        print("checking...")
        for piece in self.allyPieces:
            if self.getPos() == piece.getPos() and self.name != piece.name:
                print("ILLEGAL")
                return False

        if self.getX() > 350 or self.getX() < -350 or self.getY() > 350 or self.getY() < -350:
            print("ILLEGAL")
            return False

        else:
            print("legal")
            return True
    def showLegalMoves(self):

        self.startPos = self.getPos()

        self.turtle.goto(self.getX()+100, self.getY()+200)
        if self.isMoveLegal():
            self.stampMove()
        self.turtle.goto(self.startPos)
        self.turtle.goto(self.getX()-100, self.getY()+200)
        if self.isMoveLegal():
            self.stampMove()
        self.turtle.goto(self.startPos)
        self.turtle.goto(self.getX()+100, self.getY()-200)
        if self.isMoveLegal():
            self.stampMove()
        self.turtle.goto(self.startPos)
        self.turtle.goto(self.getX()-100, self.getY()-200)
        if self.isMoveLegal():
            self.stampMove()
        self.turtle.goto(self.startPos)
        self.turtle.goto(self.getX()+200, self.getY()+100)
        if self.isMoveLegal():
            self.stampMove()
        self.turtle.goto(self.startPos)
        self.turtle.goto(self.getX()+200, self.getY()-100)
        if self.isMoveLegal():
            self.stampMove()
        self.turtle.goto(self.startPos)
        self.turtle.goto(self.getX()-200, self.getY()+100)
        if self.isMoveLegal():
            self.stampMove()
        self.turtle.goto(self.startPos)
        self.turtle.goto(self.getX()-200, self.getY()-100)
        if self.isMoveLegal():
            self.stampMove()
        self.turtle.goto(self.startPos)
        
    def move(self, x, y):
        super().move(x, y)

class Rook(Piece):
    def __init__(self, turtle, piece, team, posX, posY):
        super().__init__(turtle, piece, team, posX, posY)
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
        self.stamp = self.turtle.stamp()
        
        self.turtle.shape(self.shape)
        self.turtle.showturtle()

        
        self.possibleMovesX.append(self.getX())
        self.possibleMovesY.append(self.getY())

        self.showingMoves = True


    def isClicked(self, x, y):
        if x in range(self.turtle.xcor() - 50, self.turtle.xcor() + 50) and y in range(self.turtle.ycor() - 50, self.turtle.ycor() + 50):
            return True
        else:
            return False

    def isMoveLegal(self):
        
        print("checking...")
        for piece in self.allyPieces:
            if self.getPos() == piece.getPos() and self.name != piece.name:
                print("ILLEGAL")
                return False
        
        for piece in self.enemyPieces:
          if self.getPos() == piece.getPos() and self.name != piece.name:
              print("CAPTURE")
              self.stampMove()
              return False

        if self.getX() > 350 or self.getX() < -350 or self.getY() > 350 or self.getY() < -350:
            print("ILLEGAL")
            return False

        else:
            print("legal")
            return True
    def showLegalMoves(self):

        self.startPos = self.getPos()

        for i in range(8):
            self.turtle.goto(self.getX(), self.getY()+100)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break
        self.turtle.goto(self.startPos)
        for i in range(8):
            self.turtle.goto(self.getX(), self.getY()-100)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break
        self.turtle.goto(self.startPos)
        for i in range(8):
            self.turtle.goto(self.getX()+100, self.getY())
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break
        self.turtle.goto(self.startPos)
        for i in range(8):
            self.turtle.goto(self.getX()-100, self.getY())
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break
        self.turtle.goto(self.startPos)

    def move(self, x, y):
        super().move(x, y)

class Queen(Piece):
    def __init__(self, turtle, piece, team, posX, posY):
        super().__init__(turtle, piece, team, posX, posY)
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
        self.stamp = self.turtle.stamp()
        
        self.turtle.shape(self.shape)
        self.turtle.showturtle()

        
        self.possibleMovesX.append(self.getX())
        self.possibleMovesY.append(self.getY())

        self.showingMoves = True


    def isClicked(self, x, y):
        if x in range(self.turtle.xcor() - 50, self.turtle.xcor() + 50) and y in range(self.turtle.ycor() - 50, self.turtle.ycor() + 50):
            return True
        else:
            return False

    def isMoveLegal(self):
        
        print("checking...")
        for piece in self.allyPieces:
            if self.getPos() == piece.getPos() and self.name != piece.name:
                print("ILLEGAL")
                return False
        
        for piece in self.enemyPieces:
          if self.getPos() == piece.getPos() and self.name != piece.name:
              print("CAPTURE")
              self.stampMove()
              return False

        if self.getX() > 350 or self.getX() < -350 or self.getY() > 350 or self.getY() < -350:
            print("ILLEGAL")
            return False

        else:
            print("legal")
            return True
    def showLegalMoves(self):
        self.startPos = self.getPos()

        for i in range(8):
            self.turtle.goto(self.getX(), self.getY()+100)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break
        self.turtle.goto(self.startPos)
        for i in range(8):
            self.turtle.goto(self.getX(), self.getY()-100)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break
        self.turtle.goto(self.startPos)
        for i in range(8):
            self.turtle.goto(self.getX()+100, self.getY())
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break
        self.turtle.goto(self.startPos)
        for i in range(8):
            self.turtle.goto(self.getX()-100, self.getY())
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break
        self.turtle.goto(self.startPos)

        
        for i in range(8):
            self.turtle.goto(self.getX()+100, self.getY()+100)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break

        self.turtle.goto(self.startPos)

        for i in range(8):
            self.turtle.goto(self.getX()-100, self.getY()+100)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break
        
        self.turtle.goto(self.startPos)

        for i in range(8):
            self.turtle.goto(self.getX()+100, self.getY()-100)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break

        self.turtle.goto(self.startPos)
        
        for i in range(8):
            self.turtle.goto(self.getX()-100, self.getY()-100)
            if self.isMoveLegal():
                self.stampMove()
            if not self.isMoveLegal():
                break
        
        self.turtle.goto(self.startPos)

    def move(self, x, y):
        super().move(x, y)

class King(Piece):
    def __init__(self, turtle, piece, team, posX, posY):
        super().__init__(turtle, piece, team, posX, posY)
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
        self.stamp = self.turtle.stamp()
        
        self.turtle.shape(self.shape)
        self.turtle.showturtle()

        
        self.possibleMovesX.append(self.getX())
        self.possibleMovesY.append(self.getY())

        self.showingMoves = True


    def isClicked(self, x, y):
        if x in range(self.turtle.xcor() - 50, self.turtle.xcor() + 50) and y in range(self.turtle.ycor() - 50, self.turtle.ycor() + 50):
            return True
        else:
            return False

    def isMoveLegal(self):
        
        print("checking...")
        for piece in self.allyPieces:
            if self.getPos() == piece.getPos() and self.name != piece.name:
                print("ILLEGAL")
                return False
        
        for piece in self.enemyPieces:
          if self.getPos() == piece.getPos() and self.name != piece.name:
              print("CAPTURE")
              self.stampMove()
              return False

        if self.getX() > 350 or self.getX() < -350 or self.getY() > 350 or self.getY() < -350:
            print("ILLEGAL")
            return False
        else:
            print("legal")
            return True
    def showLegalMoves(self):
        self.startPos = self.getPos()

    def move(self, x, y):
        super().move(x, y)
    
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
    if toMove:
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
