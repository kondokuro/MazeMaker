from parts import Area, Hall, Maze
import random


def _make_area(with_portal: bool = False, connected_to: Area = None) -> Area:
    """Quick way to get a new area."""
    new_area = Area(with_portal)
    if connected_to:
        _connect_areas(new_area, connected_to)
    return new_area


def _connect_areas(area_one: Area, area_two: Area) -> None:
    """Sets both areas as links, unless they where connected."""
    if area_two not in area_one.links:
        area_one.links.append(area_two)
    if area_one not in area_two.links:
        area_two.links.append(area_one)


def _make_hall(required_length, branching_from: Area = None, has_start: bool = False, has_end: bool = False) -> Hall:
    """Provides a proper hall, where all its areas are connected in order.
    - required_length: number of areas in the hall
    - branching_from: an area from another hall.
    - has_start: indicates that the first area as a portal.
    - has_end: indicates that the last area is a portal.
    """
    if required_length == 1:
        return Hall([Area(True)])

    new_hall = Hall()

    start = _make_area(has_start, branching_from)
    new_hall.areas.append(start)

    for i in range(required_length - 2):
        new_area = _make_area(connected_to=new_hall.areas[i])
        new_hall.areas.append(new_area)

    end = _make_area(has_end, new_hall.areas[-1])
    new_hall.areas.append(end)

    return new_hall


def _get_open_joints(halls: list, link_limit: int) -> list:
    """Returns a list of any areas from the halls that have less than link_limit links."""
    areas = []
    for hall in halls:
        available = [area for area in hall.areas if len(area.links) < link_limit]
        areas.extend([area for area in available])
    return areas


def create_maze(portals: int = 1, halls: int = 1, branching_limit: int = 4, hall_length_range: tuple = (1, 1)):
    """Creates a maze of portals plus halls size based on the requested parameters.
    It defaults to a single room.
    - portals: the number of portals in the maze
    - halls: the number halls in the maze
    - branching_limit: max number of branches that can spread from an area, where:
      - the minimum value is 1 for mazes of one room and same portal for entrance and exit
      - the minimum value is 2 for mazes of one hall, one area as entrance and the other as exit
    - hall_length_range: min-max number of areas a hall can have
    """
    halls_to_build = halls
    length_min = hall_length_range[0]
    length_max = hall_length_range[1]
    new_maze = Maze()

    main_path = _make_hall(
        required_length=random.randint(length_min, length_max),
        branching_from=None,
        has_start=True,
        has_end=bool(random.getrandbits(1)) if portals > 1 and length_max > 1 else False
    )
    new_maze.halls.append(main_path)
    if halls == 1:
        return new_maze

    halls_to_build -= 1
    portals_to_build = portals - len(main_path.portals)

    for i in range(halls_to_build):
        connections = _get_open_joints(new_maze.halls, branching_limit)
        new_branch = _make_hall(
            required_length=random.randint(hall_length_range[0], hall_length_range[1]),
            branching_from=random.choice(connections) if connections else None,
            has_start=bool(random.getrandbits(1)) if portals_to_build else False,
            has_end=bool(random.getrandbits(1)) if portals_to_build else False
        )
        new_maze.halls.append(new_branch)
        portals_to_build -= len(new_branch.portals)

    return new_maze
