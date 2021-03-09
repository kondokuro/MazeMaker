from enum import Enum


class AreaType(Enum):
    ENTRANCE = 0
    EXIT = 1
    PATH = 2
    BRANCH = 3


class Maze:
    """The data representation of a labyrinth."""
    
    def __init__(self):
        self.branches = []
        self.areas = []
        
    
class Branch:
    """A collection of areas linked to each other."""
    
    def __init__(self):
        self.areas = []
        
        
class Area:
    """The representation of a room in a maze."""
    
    def __init__(self, area_type):
        self.type = area_type
        self.connections = []
