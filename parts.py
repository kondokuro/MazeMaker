from uuid import uuid4


class Area:
    """The representation of a room in a maze, its property is_portal indicates
    that this area has an entrance or exist point while is_path identifies this
    area as part of a path branch of the maze.
    """

    def __init__(self, is_portal: bool):
        self.__id = uuid4()
        self.__is_portal = is_portal

    @property
    def id(self): return self.__id

    @property
    def is_portal(self): return self.__is_portal

    def to_dict(self):
        return {"id": str(self.id), "is_portal": self.is_portal}


class Branch:
    """A collection of areas linked to each other, if all areas in the branch
    are paths this branch has an entrance that leads to an exit, otherwise
    it is just a dead end branch."""

    def __init__(self, areas: list):
        self.__id = uuid4()
        self.__areas = areas

    @property
    def id(self): return self.__id

    @property
    def areas(self): return self.__areas

    @property
    def is_path(self):
        """A branch is path if it has any portals."""
        return True if [area for area in self.areas if area.is_portal] else False

    def to_dict(self):
        return {
            "id": str(self.id),
            "areas": [area.to_dict() for area in self.areas],
            "is_path": self.is_path
        }


class Maze:
    """The data representation of a labyrinth."""

    def __init__(self, branches: list):
        self.__id = uuid4()
        self.__branches = branches

    @property
    def id(self): return self.__id

    @property
    def branches(self):
        return [branch for branch in self.__branches if not branch.is_path]

    @property
    def paths(self):
        return [branch for branch in self.__branches if branch.is_path]

    def to_dict(self):
        return {
            "id": str(self.id),
            "branches": [branch.to_dict() for branch in self.branches],
            "paths": [branch.to_dict() for branch in self.paths]
        }