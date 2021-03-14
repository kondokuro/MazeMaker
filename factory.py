from parts import Area, AreaCategory, Branch, Maze


def create_maze(entrances: int, exits: int, branches: int, branch_min_length: int, branch_max_length: int):
    """Creates a maze based on the requested parameters."""
    generated = Maze()
    generated.add(_make_path(1))
    return generated


def _make_path(length, connection: Area = None):
    """Provides a branch of defined length areas with an entrance and exit.
    If provided with a connection area, the path can have:
    - a predefined entrance
    - a predefined exit
    - be connected to another branch of the maze
    """
    generated = Branch()
    generated.add(Area(AreaCategory.ENTRANCE))
    generated.add(Area(AreaCategory.EXIT))
    return generated


def _make_branch(length, starting_area: Area):
    """Provides a branch of defined length from a starting area."""
    return Branch()
