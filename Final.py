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
        if self.randomx<4:
            self.randomx=4
        self.randomy = (crazy(0, 3)*-1)*6
        if self.randomy<1.6:
            self.randomy=1.6
        if self.randomy>4:
            self.randomy=4
        self.avx = self.randomx
        self.avy = self.randomy

    def step(self):
        if self.collidingWithSprites(player1):
            self.avy = self.avy*-1
        if self.x>1730:
            self.avx = self.avx*-1
        self.x += self.avx
        self.y += self.avy
"""
        if self.y > 0:
            self.avy = self.avy*-1
        if self.collidingWithSprites(ball):
            self.avy = self.avy*-1
        if self.x<0:
            self.avx = self.avx*-1
"""

class BrickBreaker(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(self.width//Background.width + 1):
            for y in range(self.height//Background.height + 1):
                Background((x*Background.width, y*Background.height))
        Background((0, 0))
        player1((800, 820))
        ball((860, 410))
    def step(self):
        for ship in self.getSpritesbyClass(player1):
            ship.step()
        for ship in self.getSpritesbyClass(ball):
            ship.step()

app = BrickBreaker(0, 0)
app.run()