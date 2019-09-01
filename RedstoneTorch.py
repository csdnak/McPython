from torch import *


class RedstoneTorch(Torch):

    element = 76  # minecraft code of redstone torch

    def __init__(self, element_position_from, element_position_to, anchored_to="down"):
        # type: (Position, Position, string) -> Torch
        """
        create Torch blocks
        :param element_position_from: Torch position from
        :param element_position_to: Torch position to
        :param anchored_to: relative anchor positioning
        :rtype: Torch
        """

        super(Torch, self).__init__(element_position_from, element_position_to, anchored_to)

    @classmethod
    def one(cls, element_position, anchored_to="up"):
        # type: (Position, string) -> Torch
        """
        create one Torch
        :param element_position: Torch position
        :param anchored_to: relative anchor positioning
        :return: Torch
        :rtype: Torch
        """

        return cls(element_position, element_position, anchored_to)


if __name__ == "__main__":  # direct call for testing purpose
    # self test code

    pos = Position()

    # test anchor orientation
    for counter in ("from_me", "right", "to_me", "left"):
        Cuboid(Position(pos, dx=5, dz=-1), Position(pos, dx=7, dz=1), 1, 0)
        RedstoneTorch.one(Position(pos, dx=6), anchored_to=counter)
        pos.rotate_left()

    # test creation of many elements
    RedstoneTorch(Position(pos, dx=9, dz=-2), Position(pos, dx=19, dz=2), anchored_to="down")

    # test array of elements creation
    pos.rotate_left()
    for br in range(1, 10, 2):
        RedstoneTorch.one(Position(pos, dx=6 + br, dz=br), anchored_to="down")
