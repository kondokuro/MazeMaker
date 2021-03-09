import hug


@hug.get(examples='name=Dario&age=40')
def maze(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """Returns a maze object."""
    return {'message': 'Happy {0} Birthday {1}!'.format(age, name),
            'took': float(hug_timer)}
