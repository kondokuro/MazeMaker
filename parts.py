from enum import Enum
from uuid import uuid4


class AreaCategory(Enum):
    ENTRANCE = 0
    EXIT = 1
    PATH = 2
    BRANCH = 3


class Area:
    """The representation of a room in a maze."""

    def __init__(self, category: AreaCategory):
        self._id = uuid4()
        self.category = category

    @property
    def id(self): return self._id


class Branch:
    """A collection of areas linked to each other."""

    def __init__(self, areas=None):
        self._id = uuid4()
        self._areas = areas if areas is not None and areas is list else []

    @property
    def id(self): return self._id

    @property
    def areas(self): return self._areas

    def add(self, area: Area):
        self._areas.append(area)


class Maze:
    """The data representation of a labyrinth."""

    def __init__(self, branches=None):
        self._id = uuid4()
        self.branches = branches if branches is not None and branches is list else []

    @property
    def id(self): return self._id

    def add(self, branch: Branch):
        self.branches.append(branch)
