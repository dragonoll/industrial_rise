from ursina import *
from random import randint



class wood(Entity):
    
    def __init__(self, add_to_scene_entities=True):
        super().__init__(add_to_scene_entities,
                         model = 'cube',
                         color = color.brown,
                         position = (randint(-10, 10), 0.5 ,randint(-10, 10)),
                         collider = 'mesh',
                         on_click = None
                         )
    
def collect():
        print('+1 wood')