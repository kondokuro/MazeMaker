from parts import Maze, Branch, Area


def test_to_dict_area_does_not_raise():
    Area(True).to_dict()


def test_to_dict_branch_does_not_raise():
    Branch(Area(True)).to_dict()


def test_to_dict_emtpy_maze_does_not_raise():
    Maze().to_dict()


def test_to_dict_maze_with_branch_does_not_raise():
    Maze(Branch([Area(True)])).to_dict()


def test_branch_with_portals_is_path():
    path = Branch([Area(True)])


def test_maze_with_paths_returns_path_list():
    maze = Maze([Branch([Area(True)])])
