from cuboid import *

class Block(Cuboid):
    # class for creating one block
    def __init__(self, block_position, material, material_modification=0):
        # type: (object, object, object) -> object
        """
        Block class initialization
        :param block_position: Position
        :param material: int
        :param material_modification: int
        :rtype: Block
        """

        super(Block, self).__init__(block_position, block_position, material, material_modification)


if __name__ == "__main__":  # direct call for testing purpose
    # self test code
    Block(Position.relative_distance(2, 1, -1), 1, 0)
    pos = Position()
    pos.rotate_left()
    Block(Position(pos, 4, 1, -1), 1, 0)
    pos.rotate_right()
    pos.rotate_right()
    Block(Position(pos, 4, 2, -1), 1, 0)
    pos.rotate_right()
    Block(Position(pos, 4, 3, -1), 1, 0)

    Block (Position(dx=15, dz=3), 1)
