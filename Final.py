"""
Author: Bauti Gallino
Credit: Vinzent
Background Image: http://img4.wikia.nocookie.net/__cb20140610025745/ravens-talon/images/a/af/Metal_floor_by_goeshadow13-d5zy027.jpg
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
import math

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinborder=LineStyle(2, red)

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
        self.Moveleft=0
    self.Moveright=0
    BrickBreaker.listenKeyEvent("keydown", "space", self.Left)
    BrickBreaker.listenKeyEvent("keyup", "space", self.Leftstop)
    BrickBreaker.listenKeyEvent("keydown", "space", self.Right)
    BrickBreaker.listenKeyEvent("keyup", "space", self.Rightstop)

    def step(self):
        if self.Moveleft==1:
            self.x-=1
        else:
            self.x=self.x
        if self.Moveright==1:
            self.x+=1
        else:
            self.x=self.x

    def Left(self, event):
        self.Moveleft=1
    def Leftstop(self, event):
        self.Moveleft=0
    def Right(self, event):
        self.Moveright=1
    def Rightstop(self, event):
        self.Moveright=0
class BrickBreaker(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(self.width//Background.width + 1):
            for y in range(self.height//Background.height + 1):
                Background((x*Background.width, y*Background.height))
        Background((0, 0))
        player1((800, 750))

app = BrickBreaker(0, 0)
app.run()