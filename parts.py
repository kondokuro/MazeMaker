from uuid import uuid4


class Area:
    """The representation of a room in a maze, its property is_portal indicates
    that this area has an entrance or exist point.
    """

    def __init__(self, is_portal: bool = False, connection=None):
        self.__id = uuid4()
        self.__is_portal = is_portal
        self.__connections = []
        if isinstance(connection, Area):
            self.connect(connection)

    @property
    def id(self):
        return self.__id

    @property
    def is_portal(self):
        return self.__is_portal

    @property
    def connections(self) -> list:
        return self.__connections

    def connect(self, area):
        """Sets both areas as connections, unless they where connected."""
        if not isinstance(area, Area):
            raise AttributeError("A connection must be an area")
        if area not in self.connections:
            self.__connections.append(area)
        if self not in area.connections:
            area.connect(self)

    def to_dict(self):
        return {
            "id": str(self.id),
            "is_portal": self.is_portal,
            "connections": [area.to_dict() for area in self.connections]}


class Branch:
    """A collection of areas linked to each other."""

    def __init__(self, areas: list):
        """Create a branch with the areas in the list, they need to be connected.
        If any of them are portals then this branch will be a path."""
        self.__id = uuid4()
        self.__areas = areas

    @staticmethod
    def __connect_areas(areas: list):
        if len(areas) < 2:
            return areas
        if [item for item in areas if not isinstance(item, Area)]:
            raise TypeError("unable to connect areas. Any of the argument's elements was not instance of Area.")
        for i in range(len(areas) - 1):
            area = areas[i]
            area.connect(areas[i + 1])
        return areas

    @property
    def id(self):
        return self.__id

    @property
    def areas(self):
        return self.__areas

    @property
    def portals(self):
        return [area for area in self.areas if area.is_portal]

    @property
    def is_path(self):
        """A branch is path if it has any portals."""
        return True if [area for area in self.areas if area.is_portal] else False

    @property
    def connections(self):
        """List of areas not in the branch."""
        connections = []
        for area in self.areas:
            connections.extend(area.connections)
        return [connection for connection in connections if connection not in self.areas]

    def has_connections(self):
        """True if any branch area has a connection to an area not in the branch"""
        return True if self.connections else False

    def to_dict(self):
        return {
            "id": str(self.id),
            "is_path": self.is_path,
            "areas": [area.to_dict() for area in self.areas],
            "portals": [area.to_dict() for area in self.portals]
        }


class Maze:
    """The data representation of a labyrinth."""

    def __init__(self, branches: list):
        self.__id = uuid4()
        self.__halls = branches

    @property
    def id(self): return self.__id

    @property
    def halls(self): return self.__halls

    @property
    def branches(self):
        return [branch for branch in self.__halls if not branch.is_path]

    @property
    def paths(self):
        return [branch for branch in self.__halls if branch.is_path]

    def to_dict(self):
        return {
            "id": str(self.id),
            "branches": [branch.to_dict() for branch in self.branches],
            "paths": [branch.to_dict() for branch in self.paths]
        }
