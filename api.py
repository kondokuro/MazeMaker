import hug
import generator



@hug.get(examples='name=Dario&age=40')
def maze(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """Returns a maze object."""
    random_maze = generator.create_maze()
    return random_maze
