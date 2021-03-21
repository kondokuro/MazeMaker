from factory import create_maze, _make_branch, _get_connectable_areas, _get_connectable_portals
from parts import Area, Branch
import pytest


def __make_test_area(area: Area, connections: int):
    for i in range(connections):
        area.connect(Area())
    return area


def test_get_connectable_areas_returns_areas_within_limit():
    test_branches = [
        Branch([__make_test_area(Area(), 4), __make_test_area(Area(True), 2)]),
        Branch([__make_test_area(Area(), 4), __make_test_area(Area(), 2)])
    ]
    assert len(_get_connectable_areas(test_branches, 4)) == 1


def test_get_connectable_portals_returns_areas_within_limit():
    test_branches = [
        Branch([__make_test_area(Area(), 4), __make_test_area(Area(), 2)]),
        Branch([__make_test_area(Area(), 4), __make_test_area(Area(True), 2)])
    ]
    assert len(_get_connectable_portals(test_branches, 4)) == 1


def test_make_branch_returned_branch_areas_are_connected():
    branch = _make_branch(4)
    for area in branch.areas:
        assert area.connections


@pytest.mark.parametrize("length", [1, 3, 5, 8, 13])
def test_make_branch_with_start_portal_returns_one_way_path_of_set_size(length):
    path = _make_branch(length, has_start=True)
    assert path.is_path
    assert len(path.portals) == 1
    assert path.areas[0].is_portal
    assert len(path.areas) == length


@pytest.mark.parametrize("length", [1, 3, 5, 8, 13])
def test_make_branch_with_end_portal_returns_one_way_path_of_set_size(length):
    path = _make_branch(length, has_end=True)
    assert path.is_path
    assert len(path.portals) == 1
    assert path.areas[length - 1].is_portal
    assert len(path.areas) == length


def test_make_branch_one_area_two_portals_raises_error():
    with pytest.raises(ValueError):
        _make_branch(1, has_start=True, has_end=True)


@pytest.mark.parametrize("length", [2, 5, 7, 11, 16])
def test_make_branch_returns_path_of_set_size_and_paired_portals(length):
    path = _make_branch(length, has_start=True, has_end=True)
    assert path.is_path
    assert len(path.portals) == 2
    assert path.areas[0].is_portal
    assert path.areas[length - 1].is_portal
    assert len(path.areas) == length


def test_make_branch_connected_to_portal_one_area_two_portals_raises_error():
    connection = Area(is_portal=True)
    with pytest.raises(ValueError):
        _make_branch(1, link_to=connection, has_start=True, has_end=True)


def test_make_branch_connected_to_area_returns_branch_containing_connection():
    connection = Area(is_portal=False)
    connected_branch = _make_branch(4, link_to=connection)
    assert False if connected_branch.is_path else True
    assert connection in connected_branch.areas
    assert connection not in connected_branch.portals
    assert len(connected_branch.portals) == 0


@pytest.mark.parametrize("is_portal", [True, False])
def test_make_branch_connected_adds_connection_to_connected_area(is_portal):
    connected_area = Area(is_portal=is_portal)
    branch = _make_branch(3, link_to=connected_area)
    branch_areas = branch.areas
    branch_links = []
    for area in branch_areas:
        for connection in area.connections:
            branch_links.append(connection)
    assert connected_area.connections
    assert connected_area.connections[0] in branch_links


@pytest.mark.parametrize("has_start", [True, False])
def test_make_branch_connected_to_portal_ignores_start_portal_returns_path_containing_connection(has_start):
    connection = Area(is_portal=True)
    connected_path = _make_branch(3, link_to=connection, has_start=has_start)
    assert connected_path.is_path
    assert connection in connected_path.areas
    assert connection in connected_path.portals
    assert len(connected_path.portals) == 1


def test_make_branch_connected_to_portal_with_end_portal_returns_path_containing_connection():
    connection = Area(is_portal=True)
    connected_path = _make_branch(5, link_to=connection, has_end=True)
    assert connected_path.is_path
    assert connection in connected_path.areas
    assert connection in connected_path.portals
    assert len(connected_path.portals) == 2


@pytest.mark.parametrize(
    "paths, branches, branch_limit, min_length, max_length",
    [
        (1, 3, 4, 5, 8),
        (2, 3, 6, 5, 6),
        (3, 6, 9, 2, 6),
        (6, 2, 9, 6, 2),
    ])
def test_create_maze_multiple_branches_returns_correct_maze(
        paths, branches, branch_limit, min_length, max_length):
    labyrinth = create_maze(paths, branches, branch_limit, (min_length, max_length))
    assert len(labyrinth.branches) == branches
    assert len(labyrinth.paths) == paths
    assert len([hall for hall in labyrinth.halls if hall.has_connections]) == len(labyrinth.halls)
    for hall in labyrinth.halls:
        assert min_length <= len(hall.areas) <= max_length
        for area in hall.areas:
            assert len(area.connections) <= branch_limit


@pytest.mark.parametrize(
    "paths, branches, branch_limit, min_length, max_length",
    [
        (0, 3, 4, 5, 8),  # no paths
        (2, 2, 1, 5, 6),  # minimum connections allowed too low
        (3, 6, 9, 1, 4),  # min length too small
        (6, 2, 9, 1, 1),  # max length too small
    ])
def test_create_maze_bad_parameters_raises_value_error(paths, branches, branch_limit, min_length, max_length):
    with ValueError:
        create_maze(paths, branches, branch_limit, (min_length, max_length))
