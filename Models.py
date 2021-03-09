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
    
    def __init__(self, is_path):
        self.is_path = is_path
        self.connections = []
