from parts import Area, Branch, Maze
import random


def create_maze(paths: int = 1, branches: int = 0, branch_limit: int = 4, hall_length_range: tuple = (1, 1)):
    """Creates a maze of paths plus branches size based on the requested parameters.
    It defaults to a single room.
    - paths: the number of halls with entrance and/or exit portals
    - branches: the number of additional halls in the maze
    - branch_limit: max number of connecting branches that can spread from an area, where:
      - the minimum value is 1 for mazes of one room
      - the minimum value is 2 for mazes of one hall
    - hall_length_range: min-max number of areas a branch can have
    """
    if paths < 1:
        raise ValueError("A maze needs at least one path.")
    if branch_limit < 1:
        raise ValueError("Invalid parameter branch_limit must be at least 1")
    if len(hall_length_range) != 2:
        raise ValueError("hall_length_range must contain 2 elements")
    for i in hall_length_range:
        if i < 1: raise ValueError(f"Length of halls must be more than {i}")
    if hall_length_range[0] < hall_length_range[1]:
        hall_length_range = (hall_length_range[1], hall_length_range[0])
    halls = branches + paths
    if hall_length_range[1] == 1 and halls > 1:
        raise ValueError("Requested number of hall is incompatible with the requested length")
    if branch_limit < 3 and branch_limit < halls:
        raise ValueError("Branching limit is too low for the requested halls")

    maze_halls = []
    main_path = _make_branch(
        length=random.randint(hall_length_range[0], hall_length_range[1]),
        max_links=branch_limit,
        link_to=None,
        has_start=True,
        has_end=random.randint(0, 1)
    )
    maze_halls.append(main_path)
    if halls == 1:
        return Maze(maze_halls)

    built_paths = paths - 1
    for i in halls:
        link_hall = random.choice(maze_halls)
        connection = __get_branch_open_areas(random.choice(link_hall.areas))
        maze_halls.append(_make_branch(
            length=random.randint(hall_length_range[0], hall_length_range[1]),
            max_links=branch_limit,
            link_to=connection,
            has_start=random.randint(0, 1) if built_paths else False,
            has_end=random.randint(0, 1) if built_paths else False
        ))
        built_paths = built_paths - len([branch for branch in maze_halls if branch.is_path])
    generated = Maze(maze_halls)
    return generated


# NOTE max_links is not used
def _make_branch(length, max_links: int = 4, link_to: Area = None, has_start: bool = False, has_end: bool = False):
    """Provides a branch.
    - length: number of areas in the branch
    - max_links: limit on how many connections any area in the branch can have, defaults to 4, minimum 1.
    - link_to: this area is used as the start point.
    - has_start: indicates that the first area as a portal, ignored if the connection is a portal.
    - has_end: indicates that the last area as a portal.
    """
    if length == 1:
        if has_start == has_end:
            raise ValueError(f"Invalid parameters for this branch "
                             f"length: {length}, has_start: {has_start}, has_end: {has_end}")
        if link_to:
            raise ValueError(f"Invalid parameter, a linked branch length has to be more than {length}")
    if length < 1:
        raise ValueError(f"Invalid parameter, length has to be more than {length}")

    if length == 1:
        return Branch([Area(True)])

    areas = []
    if link_to:
        areas.append(link_to)
    else:
        areas.append(Area(has_start))
    additional_areas = len(areas)
    if has_end:
        additional_areas = additional_areas + 1
    inner_branch_length = length - additional_areas
    for i in range(inner_branch_length):
        areas.append(Area(connection=areas[i]))
    if has_end:
        areas.append(Area(has_end, areas[length - additional_areas]))
    return Branch(areas)


def _get_connectable_areas(branches: list, connection_limit: int):
    """Returns a list why any areas in the branch that have less than limit connections."""
    connectable = []
    for branch in branches:
        available = __get_branch_open_areas(branch, connection_limit)
        connectable.extend([area for area in available])
    return connectable


def _get_connectable_portals(branches: list, connection_limit: int):
    """Returns a list of branch portal areas that have less than limit connections."""
    connectable = []
    for branch in branches:
        available = __get_branch_open_areas(branch, connection_limit)
        connectable.extend([area for area in available if area.is_portal])
    return connectable


def __get_branch_open_areas(branch: Branch, limit: int):
    return [area for area in branch.areas if len(area.connections) < limit]
