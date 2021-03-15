from uuid import uuid4


class Area:
    """The representation of a room in a maze, its property is_portal indicates
    that this area has an entrance or exist point.
    """

    def __init__(self, is_portal: bool):
        self._id = uuid4().hex
        self._is_portal = is_portal

    @property
    def id(self): return self._id

    @property
    def is_portal(self): return self._is_portal

    def to_dict(self):
        return {"id": self.id, "is_portal": self.is_portal}


class Branch:
    """A collection of areas linked to each other."""

    def __init__(self, areas=None):
        self._id = uuid4().hex
        self._areas = areas if areas is not None and areas is list else []

    @property
    def id(self): return self._id

    @property
    def areas(self): return self._areas

    def add(self, area: Area):
        self._areas.append(area)

    @property
    def is_path(self):
        return True if [area for area in self.areas if area.is_portal] else False

    def to_dict(self):
        return {"id": self.id, "areas": [area.to_dict() for area in self.areas]}


class Maze:
    """The data representation of a labyrinth."""

    def __init__(self, branches=None):
        self._id = uuid4().hex
        self.branches = branches if branches is not None and branches is list else []

    @property
    def id(self): return self._id

    @property
    def paths(self):
        return [branch for branch in self.branches if [area for area in branch.areas if area.is_portal]]

    def add(self, branch: Branch):
        self.branches.append(branch)

    def to_dict(self):
        return {"id": self.id, "branches": [branch.to_dict() for branch in self.branches]}
