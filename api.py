import hug
import generator


@hug.get(examples='entrances=1&exits=1&length=1')
def maze(entrances: hug.types.number, exits: hug.types.number, length: hug.types.number):
    """Returns a maze object."""
    random_maze = generator.create_maze(entrances, exits, length)
    return random_maze
