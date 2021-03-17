from parts import Area, Branch, Maze


def create_maze(paths: int, branches: int, branching_range: list, branch_length_range: list):
    """Creates a maze based on the requested parameters.
    - paths: the number of halls with entrance and/or exit portals
    - branches: the number of additional halls in the maze
    - branching_range: min-max number of branches that can spread from a branch area
    - branch_length_range: min-max number of areas a branch can have
    """
    generated = Maze([_make_branch(1)])
    return generated


def _make_branch(length, connection: Area = None, start_portal:bool = False, end_portal: bool = False):
    """Provides a branch.
    - length: number of areas in the branch
    - connection: this area is used as the start point, great for linking branches.
    - start_portal: indicates to make the first area as a portal, ignored if the connection is a portal.
    - end_portal: indicates to make the last area as a portal.
    """
    generated = Branch([Area(True)])
    return generated
