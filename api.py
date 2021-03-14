import hug
import factory
import json
from serializers import serialize_part


@hug.get(examples='entrances=1&exits=1&length=1')
def maze(
        entrances: hug.types.number,
        exits: hug.types.number,
        branches: hug.types.number,
        min_length: hug.types.number,
        max_length: hug.types.number):
    """Returns a maze object."""
    random_maze = factory.create_maze(entrances, exits, branches, min_length, max_length)
    return json.dumps(serialize_part(random_maze))
