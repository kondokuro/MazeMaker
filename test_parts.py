from parts import to_dict, Maze, Branch, Area


def test_to_dict_area_does_not_raise():
    to_dict(Area(True))


def test_to_dict_branch_does_not_raise():
    to_dict(Branch(Area(True)))


def test_to_dict_emtpy_maze_does_not_raise():
    to_dict(Maze())


def test_to_dict_maze_with_branch_does_not_raise():
    to_dict(Maze(Branch([Area(True)])))


def test_branch_with_portals_is_path():
    path = Branch([Area(True)])


def test_maze_with_paths_returns_path_list():
    maze = Maze([Branch([Area(True)])])
