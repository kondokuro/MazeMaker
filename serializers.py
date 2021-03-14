from parts import Area, Branch, Maze


def serialize_part(part):
    if type(part) is Area:
        return {"id": str(part.id), "category": str(part.category)}
    if type(part) is Branch:
        return {"id": str(part.id), "areas": [serialize_part(area) for area in part.areas]}
    if type(part) is Maze:
        return {"id": str(part.id), "branches": [serialize_part(branch) for branch in part.branches]}
