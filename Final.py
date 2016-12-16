"""
Author: Bauti Gallino
Credit: Vinzent, Liam S
Background Image: http://img4.wikia.nocookie.net/__cb20140610025745/ravens-talon/images/a/af/Metal_floor_by_goeshadow13-d5zy027.jpg
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
import math
import random

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinborder=LineStyle(2, red)
skinnyborder=LineStyle(2, blue)
brickborder=LineStyle(2, black)
whatgame=input("1 for pong, 2 for brick breaker:")

while whatgame!=1 or whatgame!=2:
    if whatgame!=1 or whatgame!=2:
        input("1 for pong, 2 for brick breaker")
if whatgame==1:
    print(pong)
    
"""
def crazy(digit, decimal):
    randomout = round((random.random())*(10**digit), decimal)
    return randomout

class Background(Sprite):
    asset = ImageAsset("images/Metal_floor_by_goeshadow13-d5zy027.jpg")
    height= 100
    width= 100
    
    def __init__(self, position):
        super().__init__(Background.asset, position)

class player1(Sprite):
    asset = RectangleAsset(130, 20, thinborder, blue)

    def __init__(self, position):
        super().__init__(player1.asset, position)
        self.Movex=0
        self.rectangularCollisionModel()
        BrickBreaker.listenKeyEvent("keydown", "left arrow", self.Left)
        BrickBreaker.listenKeyEvent("keyup", "left arrow", self.Leftstop)
        BrickBreaker.listenKeyEvent("keydown", "right arrow", self.Right)
        BrickBreaker.listenKeyEvent("keyup", "right arrow", self.Rightstop)

    def step(self):
        self.x += self.Movex
        if self.x<30:
            self.x=30
        if self.x>1580:
            self.x=1580
        

    def Left(self, event):
        self.Movex=-12
    def Leftstop(self, event):
        self.Movex=0
    def Right(self, event):
        self.Movex=12
    def Rightstop(self, event):
        self.Movex=0
        
class ball(Sprite):
    asset = CircleAsset(10, skinnyborder, green)
    
    def __init__(self, position):
        super().__init__(ball.asset, position)
        self.avy = 0
        self.avx = 0
        self.circularCollisionModel()
        self.randomx = 0
        self.randomy = 0
        self.fxcenter = self.fycenter = 0.5
        self.randomx = crazy(0, 3)*-6
        if self.randomx<6:
            self.randomx=6
        self.randomy = (crazy(0, 3)*-1)*6
        if self.randomy<4:
            self.randomy=4
        if self.randomy>6:
            self.randomy=6
        self.avx = self.randomx
        self.avy = self.randomy

    def step(self):
        if self.collidingWithSprites(Brick):
            self.avy = self.avy*-1
        if self.collidingWithSprites(player1):
            self.avy = self.avy*-1
        if self.x>1710:
            self.avx = self.avx*-1
        if self.x<30:
            self.avx = self.avx*-1
        if self.y<30:
            self.avy = self.avy*-1
        if self.y>840:
            self.visible=False
        self.x += self.avx
        self.y += self.avy
class Brick(Sprite):
    asset = RectangleAsset(1000, 400, brickborder, red)
    
    def __init__(self, position):
        super().__init__(Brick.asset, position)
        self.rectangularCollisionModel()
    def step(self):
        if self.collidingWithSprites(ball):
            self.visible=False
            self.x=2000

class BrickBreaker(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(self.width//Background.width + 1):
            for y in range(self.height//Background.height + 1):
                Background((x*Background.width, y*Background.height))
        Background((0, 0))
        player1((800, 820))
        ball((860, 410))
        Brick((0,0))
    def step(self):
        for ship in self.getSpritesbyClass(player1):
            ship.step()
        for ship in self.getSpritesbyClass(ball):
            ship.step()
        for ship in self.getSpritesbyClass(Brick):
            ship.step()

app = BrickBreaker(0, 0)
app.run()
"""