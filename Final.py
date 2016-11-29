"""
Author: Bauti Gallino
Credit: Vinzent
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

thinborder=LineStyle(1, black)

class Background(Sprite):
    asset = ImageAsset("images/starfield.jpg")
    height= 512
    width= 512
    
    def __init__(self, position):
        super().__init__(Background.asset, position)

class player1(Sprite):
    asset = RectangleAsset(100, 50, thinborder, blue)

    def __init__(self, position):
        super().__init__(player1.asset, position)
class BrickBreaker(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Backround((0, 0))
        player1((500, 500))

app = BrickBreaker(1897, 935)
app.run()