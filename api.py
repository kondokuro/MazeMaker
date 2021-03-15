import hug
import factory
import json
from parts import to_dict


@hug.get(examples='paths=1&branches=1&branching_min=1&branching_max=1&branch_length_min=1&branch_length_max=1')
def maze(
        paths: hug.types.greater_than(0),
        branches: hug.types.greater_than(0),
        branching_min: hug.types.greater_than(0),
        branching_max: hug.types.greater_than(0),
        branch_length_min: hug.types.greater_than(0),
        branch_length_max: hug.types.greater_than(0)):
    """Returns the JSON representation of a maze object."""
    branching_range = [branching_min, branching_max]
    branch_length_range = [branch_length_min, branch_length_max]
    random_maze = factory.create_maze(paths, branches, branching_range, branch_length_range)
    return json.dumps(to_dict(random_maze))
