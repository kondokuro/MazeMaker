from parts import Area, Branch, Maze


def create_maze(paths: int, branches: int, branch_limit: int, branch_length_range: tuple):
    """Creates a maze based on the requested parameters.
    - paths: the number of halls with entrance and/or exit portals
    - branches: the number of additional halls in the maze
    - branch_limit: max number of connecting branches that can spread from an area,
      where the minimum coherent value is 2
    - branch_length_range: min-max number of areas a branch can have
    """
    generated = Maze([_make_branch(1)])
    return generated


def _make_branch(length,  max_connections: int = 4, connection: Area = None, start:bool = False, end: bool = False):
    """Provides a branch.
    - length: number of areas in the branch
    - max_connections: limit on how many connections any area in the branch can have, defaults to 4, minimum 1.
    - connection: this area is used as the start point, great for linking branches.
    - start: indicates that the first area as a portal, ignored if the connection is a portal.
    - end: indicates that the last area as a portal.
    """
    generated = Branch([Area(True)])
    return generated


def _get_connectable_areas(branches: list, connection_limit: int):
    """Returns a list of areas that have less than limit connections."""
    return []


def _get_connectable_portals(branches: list, connection_limit: int):
    """Returns a list of portal areas that have less than limit connections."""
    return []
