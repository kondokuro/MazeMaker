from parts import Area, Branch, Maze


def create_maze(paths: int, branches: int, branching_range: list, branch_length_range: list):
    """Creates a maze based on the requested parameters.
    - paths: the number of branches that have a portal (entrance or exit)
    - branches: the total number of branches in the maze
    - branching_range: min-max number of branches that can spread from a branch
    - branch_length_range: min-max number of areas a branch can have
    """
    generated = Maze([_make_path(1)])
    return generated


def _make_path(length, connection: Area = None, one_way: bool = False):
    """Provides a branch of defined length areas with portals, limited only by its length.
    Provide a connection area to link branches
    """
    generated = Branch([Area(True)])
    return generated


def _make_branch(length, starting_area: Area):
    """Provides a branch of defined length from a starting area."""
    return Branch([])
