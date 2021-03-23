from parts import Area, Hall, Maze
import random


def create_maze(paths: int = 1, branches: int = 0, branch_limit: int = 4, hall_length_range: tuple = (1, 1)):
    """Creates a maze of paths plus halls size based on the requested parameters.
    It defaults to a single room.
    - paths: the number of halls with entrance and/or exit portals
    - halls: the number of additional halls in the maze
    - branch_limit: max number of connecting halls that can spread from an area, where:
      - the minimum value is 1 for mazes of one room
      - the minimum value is 2 for mazes of one hall
    - hall_length_range: min-max number of areas a hall can have
    """
    if paths < 1:
        raise ValueError("A maze needs at least one path.")
    if branch_limit < 1:
        raise ValueError("Invalid parameter branch_limit must be at least 1")
    if len(hall_length_range) != 2:
        raise ValueError("hall_length_range must contain 2 elements")
    for i in hall_length_range:
        if i < 1:
            raise ValueError(f"Length of halls must be more than {i}")
    if hall_length_range[0] > hall_length_range[1]:
        hall_length_range = (hall_length_range[1], hall_length_range[0])
    halls_to_build = branches + paths
    if hall_length_range[1] == 1 and halls_to_build > 1:
        raise ValueError("Requested number of hall is incompatible with the requested length")
    if branch_limit < 3 and branch_limit < halls_to_build:
        raise ValueError("Branching limit is too low for the requested halls")

    maze_halls = []
    main_path = _make_hall(
        required_length=random.randint(hall_length_range[0], hall_length_range[1]),
        max_area_links=branch_limit,
        joint_by=None,
        has_start=True,
        has_end=True
    )
    maze_halls.append(main_path)
    if halls_to_build == 1:
        return Maze(maze_halls)

    halls_to_build -=1
    paths_built = paths - 1
    # while built_paths:
    for i in range(halls_to_build):
        link_hall = random.choice(maze_halls)
        connections = _get_branch_open_areas(link_hall, branch_limit)
        new_branch = _make_hall(
            required_length=random.randint(hall_length_range[0], hall_length_range[1]),
            max_area_links=branch_limit,
            joint_by=random.choice(connections),
            has_start=False if paths_built < 1 else bool(random.getrandbits(1)),
            has_end=False if paths_built < 1 else bool(random.getrandbits(1))
        )
        maze_halls.append(new_branch)
        paths_built = paths_built - len([branch for branch in maze_halls if branch.is_path])
    generated = Maze(maze_halls)
    return generated


def _connect_areas(area_one: Area, area_two: Area) -> None:
    """Sets both areas as links, unless they where connected."""
    if area_two not in area_one.links:
        area_one.links.append(area_two)
    if area_one not in area_two.links:
        area_two.links.append(area_one)


def _create_area(with_portal: bool = False, connected_to: Area = None) -> Area:
    """Quick way to get a new area."""
    new_area = Area(with_portal)
    if connected_to:
        _connect_areas(new_area, connected_to)
    return new_area


def _make_hall(required_length, joint_by: Area = None, has_start: bool = False, has_end: bool = False) -> Hall:
    """Provides a proper hall, where all its areas are connected in order.
    - required_length: number of areas in the hall
    - joint_by: an area from another hall.
    - has_start: indicates that the first area as a portal.
    - has_end: indicates that the last area is a portal.
    """
    if required_length == 1:
        return Hall([Area(True)])

    new_hall = Hall()

    start = _create_area(has_start, joint_by)
    new_hall.areas.append(start)

    for i in range(required_length - 2):
        new_area = _create_area(connected_to=new_hall.areas[i])
        new_hall.areas.append(new_area)

    end = _create_area(has_end, new_hall.areas[-1])
    new_hall.areas.append(end)

    return new_hall


def _areas_to_link(halls: list, connection_limit: int) -> list:
    """Returns a list why any areas in the hall that have less than limit links."""
    areas = []
    for hall in halls:
        available = _get_branch_open_areas(hall, connection_limit)
        areas.extend([area for area in available])
    return areas


def _portals_to_link(halls: list, connection_limit: int) -> list:
    """Returns a list of portal areas that have less than limit links."""
    areas = _areas_to_link(halls, connection_limit)
    return [area for area in areas if area.is_portal]


def _get_branch_open_areas(hall: Hall, limit: int) -> list:
    return [area for area in hall.areas if len(area.links) < limit]
