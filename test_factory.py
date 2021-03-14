from factory import create_maze
from parts import Area, AreaCategory, Branch, Maze


# def __verify_path__(branch: Branch):
#     """Validates the branch to path standards:
#     - Has one entrance
#     - Has one exit
#     """
#
#     start = [area for area in branch.areas if area.category is AreaCategory.ENTRANCE]
#     if not start:
#         raise AttributeError("Branch is missing an entrance")
#     if len(start) > 1:
#         raise AttributeError("Branch has to many entrances")
#
#     end = [area for area in branch.areas if area.category is AreaCategory.EXIT]
#     if not end:
#         raise AttributeError("Branch is missing an exit")
#     if len(end) > 1:
#         raise AttributeError("Branch has to many exits")


minimal_path = Branch({Area(AreaCategory.ENTRANCE), Area(AreaCategory.EXIT)})
minimal_maze = Maze(minimal_path)


def test_create_maze_one_entrance_one_exit_returns_minimal_maze():
    labyrinth = create_maze(1, 1, 1, 1, 1)
    assert len(labyrinth.branches) == 1
    assert len(labyrinth.branches.areas) == 2
    assert [area for area in labyrinth.branches if area.category == AreaCategory.ENTRANCE]
    assert [area for area in labyrinth.branches if area.category == AreaCategory.EXIT]


# @pytest.mark.parametrize(
#     "entrances, exists, branches, min_length, max_length, expected",
#     [
#         (1, 1, 1, 1, 1, minimal_maze),
#         ("2+4", 6),
#         ("6*9", 42),
#     ])
# def test_create_maze_more_exits_than_branches_raises_error():
#     assert False
