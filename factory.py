from parts import Area, AreaCategory, Branch, Maze


def create_maze(entrances, exits, branches, branch_min_length, branch_max_length):
    """Creates a maze based on the requested parameters."""
    raise NotImplemented("Create maze has not been implemented")


def _make_path(connection: Area = None):
    """Provides a branch with an entrance and exit.
    If provided with a connection area, the path can have
    - a predefined entrance
    - a predefined exit
    - be connected to another branch of the maze
    """
    raise NotImplemented()


def _make_branch(starting_area: Area):
    """Provides a branch from a starting area."""
    raise NotImplemented()