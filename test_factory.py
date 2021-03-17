from factory import create_maze, _make_branch
from parts import Area, Branch
import pytest


def __is_branch_connected(branch: Branch):
    return True if [area for area in branch.areas if area.connections] else False


@pytest.mark.parametrize("length", [1, 3, 5, 8, 13])
def test_make_branch_with_start_portal_returns_one_way_path_of_set_size(length):
    path = _make_branch(length, start_portal=True)
    assert path.is_path
    assert len(path.portals) == 1
    assert path.areas[0].is_portal
    assert len(path.areas) == length


@pytest.mark.parametrize("length", [1, 3, 5, 8, 13])
def test_make_branch_with_end_portal_returns_one_way_path_of_set_size(length):
    path = _make_branch(length, end_portal=True)
    assert path.is_path
    assert len(path.portals) == 1
    assert path.areas[length - 1].is_portal
    assert len(path.areas) == length


def test_make_branch_one_area_two_portals_raises_error():
    with pytest.raises(AttributeError):
        _make_branch(1, start_portal=True, end_portal=True)


@pytest.mark.parametrize("length", [2, 5, 7, 11, 16])
def test_make_branch_returns_path_of_set_size_and_paired_portals(length):
    path = _make_branch(length, start_portal=True, end_portal=True)
    assert path.is_path
    assert len(path.portals) == 2
    assert path.areas[0].is_portal
    assert path.areas[length - 1].is_portal
    assert len(path.areas) == length


def test_make_branch_connected_to_portal_one_area_two_portals_raises_error():
    connection = Area(is_portal=True)
    with pytest.raises(AttributeError):
        _make_branch(1, connection, start_portal=True, end_portal=True)


def test_make_branch_connected_to_area_returns_branch_containing_connection():
    connection = Area(is_portal=False)
    connected_branch = _make_branch(4, connection)
    assert False if connected_branch.is_path else True
    assert connection in connected_branch.areas
    assert connection not in connected_branch.portals
    assert len(connected_branch.portals) == 0


@pytest.mark.parametrize("has_start", [True, False])
def test_make_branch_connected_to_portal_ignores_start_portal_returns_path_containing_connection(has_start):
    connection = Area(is_portal=True)
    connected_path = _make_branch(3, connection, start_portal=has_start)
    assert connected_path.is_path
    assert connection in connected_path.areas
    assert connection in connected_path.portals
    assert len(connected_path.portals) == 1


def test_make_branch_connected_to_portal_with_end_portal_returns_path_containing_connection():
    connection = Area(is_portal=True)
    connected_path = _make_branch(5, connection, end_portal=True)
    assert connected_path.is_path
    assert connection in connected_path.areas
    assert connection in connected_path.portals
    assert len(connected_path.portals) == 2


@pytest.mark.parametrize(
    "paths, branches, branching_range, min_length, max_length",
    [
        (1, 3, [0, 2], 5, 6),
        (2, 3, [2, 2], 5, 6),
        (3, 6, [3, 5], 2, 6),
    ])
def test_create_maze_multiple_branches_returns_correct_maze(
        paths, branches, branching_range, min_length, max_length):
    labyrinth = create_maze(paths, branches, branching_range, [min_length, max_length])
    assert len(labyrinth.branches) == branches
    assert len(labyrinth.paths) == paths
    for hall in labyrinth.halls:
        assert False if (len(hall.areas) < min_length or len(hall.areas) > max_length) else True
        assert __is_branch_connected(hall)
