from one import *


class OrientedElement(object):
    def __init__(self, element_position_from, element_position_to, anchored_to=None
                 ):
        # type: (Position, Position, string) ->  OrientedElement
        """
        create oriented element blocks
        :param element_position_from: block position from
        :param element_position_to: block position to
        :param anchored_to: relative anchor positioning
        :rtype: OrientedElement
        """

        numeric_direction = self.anchored_to_list.index(anchored_to)
        buff = self.direction_table[(element_position_from.x_direction, element_position_from.z_direction)]
        real_direction = buff[numeric_direction]
        Cuboid(element_position_from, element_position_to, self.element, real_direction)

    @classmethod
    def one(cls, element_position, anchored_to="up"):
        # type: (Position, string) -> OrientedElement
        """
        create one oriented element
        :param element_position: one element position
        :param anchored_to: relative anchor positioning
        :return: OrientedElement
        :rtype: OrientedElement
        """

        return cls(element_position, element_position, anchored_to)


if __name__ == "__main__":  # direct call for testing purpose
    # self test code

    pass
