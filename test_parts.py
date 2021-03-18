from parts import Maze, Branch, Area
import pytest


@pytest.mark.parametrize("is_portal", [True, False])
def test_area_is_portal(is_portal):
    assert Area(is_portal).is_portal == is_portal


@pytest.mark.parametrize("is_portal", [True, False])
def test_area_to_dict_creates_dictionary_representation(is_portal):
    area = Area(is_portal)
    area_dict = area.to_dict()
    assert area_dict
    assert area_dict.get("id") == str(area.id)
    assert area_dict.get("is_portal") == is_portal
    assert len(area_dict.keys()) == 2


@pytest.mark.parametrize("connection_count", [1, 3, 5, 8])
def test_add_connection(connection_count):
    area = Area(False)
    for i in range(0, connection_count):
        area.add_connection(Area(False))
    assert len(area.connections) == connection_count


def test_add_connection_not_an_area_raises_error():
    area = Area(False)
    with pytest.raises(AttributeError):
        area.add_connection(Branch([]))


@pytest.mark.parametrize("is_path", [True, False])
def test_branch_is_path_with_portals_returns_true(is_path):
    assert Branch([Area(is_path)]).is_path == is_path


@pytest.mark.parametrize("is_path", [True, False])
def test_branch_to_dict_creates_dictionary_representation(is_path):
    branch = Branch([Area(is_path)])
    branch_dict = branch.to_dict()
    assert branch_dict
    assert branch_dict.get("id") == str(branch.id)
    assert branch_dict.get("is_path") == branch.is_path
    assert len(branch_dict.get("areas")) == len(branch.areas)


def test_maze_branches_returns_branch_list():
    branches = Maze([Branch([Area(False)])]).branches
    assert branches
    for branch in branches:
        assert branch.is_path is False


def test_maze_paths_with_paths_returns_path_list():
    paths = Maze([Branch([Area(True)])]).paths
    assert paths
    for path in paths:
        assert path.is_path is True


def test_maze_paths_without_paths_returns_emtpy_list():
    assert Maze([Branch([Area(False)])]).paths == []


def test_maze_branches_without_paths_returns_emtpy_list():
    assert Maze([Branch([Area(True)])]).branches == []


def test_maze_to_dict_maze_creates_dictionary_representation():
    path = [Branch([Area(True)])]
    maze = Maze(path)
    maze_dict = maze.to_dict()
    assert maze_dict
    assert maze_dict.get("id") == str(maze.id)
    assert len(maze_dict.get("branches")) == len(maze.branches)
    assert len(maze_dict.get("paths")) == len(maze.paths)
