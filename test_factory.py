from factory import create_maze
import pytest


@pytest.mark.parametrize(
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


def test_create_maze_insufficient_branches_for_paths_returns_error_string():
    labyrinth = create_maze(3, 3, 2, 3, 3)
    assert labyrinth == "Insufficient branches for the requested entrances or exits"
