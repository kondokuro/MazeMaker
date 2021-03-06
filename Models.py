from uuid import uuid4


class MazeModel():
    """The representation of a labirinth."""
    
    def __init__(self):
        self.branches = []
        self.areas = []
        
    
class BranchModel():
    """A collection of areas linked to each other."""
    
    def __init__(self):
        self.areas = []
        
        
class AreaModel():
    """The representation of a room in a maze."""
    
    def __init__(self, is_path):
        self.id = uuid4()
        self.is_path = is_path
        self.doors = []
        
        
class DoorModel():
    """Connects two areas."""
    
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
