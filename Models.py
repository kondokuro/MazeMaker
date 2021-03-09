

class MazeModel:
    """The data representation of a labyrinth."""
    
    def __init__(self):
        self.branches = []
        self.areas = []
        
    
class BranchModel:
    """A collection of areas linked to each other."""
    
    def __init__(self):
        self.areas = []
        
        
class AreaModel:
    """The representation of a room in a maze."""
    
    def __init__(self, is_path):
        self.is_path = is_path
        self.connections = []
