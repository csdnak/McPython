from Position import *  # clas for position

mc = Minecraft()  # initialization


class Cuboid(object):
    # class for creating cuboid
    def __init__(self, start, end, material, material_modification=0):
        # type: (Position, Position, int, int) -> None
        """
        Cuboid class initialization

        :param start: Position
        :param end: Position
        :param material: int
        :param material_modification: int
        :rtype: None
        """
        mc.setBlocks(start.x, start.y, start.z, end.x, end.y, end.z, material, material_modification)


if __name__ == "__main__":  # direct call for testing purpose
    # self test code

    # od = Position.relative_distance  ( 2 , 2 , -1 )
    do = Position.relative_distance(4, 2, 1)

    Cuboid(Position.relative_distance(2, 1, -1), do, 1, 0)
    Position.origin()
    pos = Position()

    pos.rotate_left()
    Cuboid(Position(pos, 4, 1, -1), Position(pos, 7, 2, 1), 1, 0)
    pos.rotate_right()
    pos.rotate_right()
    Cuboid(Position(pos, 4, 1, -1), Position(pos, 8, 2, 1), 1, 0)
    pos.rotate_right()
    Cuboid(Position(pos, 4, 1, -1), Position(pos, 9, 2, 1), 1, 0)
