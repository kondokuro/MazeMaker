from factory import create_maze, _make_path
from pytest import mark


@mark.parametrize("length", [1, 3, 5, 8, 13])
def test_make_path_one_way_returns_one_portal_path_of_set_size(length):
    path = _make_path(length, one_way=True)
    portals = [area for area in path.areas if area.is_portal]
    assert portals
    assert len(portals) == 1
    assert len(path.areas) == length


@mark.parametrize(
    "entrances, exists, branches, min_length, max_length",
    [
        (1, 1, 1, 1, 1),
        (1, 1, 3, 5, 8),
        (1, 2, 5, 5, 8),
        (2, 1, 3, 5, 8),
    ])
def test_create_maze_multiple_branches_returns_correct_maze(
        entrances, exists, branches, min_length, max_length):
    labyrinth = create_maze(entrances, exists, branches, min_length, max_length)
    assert len(labyrinth.branches) == branches
    assert len(labyrinth.paths()) == entrances
    for branch in labyrinth.branches:
        assert False if (len(branch.areas) < min_length or len(branch.areas) > max_length) else True


def test_create_maze_insufficient_branches_for_paths_returns_error_string():
    labyrinth = create_maze(3, 3, 2, 3, 3)
    assert labyrinth == "Insufficient branches for the requested entrances or exits"
