from mc import *  # Minecraft api import

mc = Minecraft()  # initialization


class Position(object):
    """
    class for holding and manipulating object position and direction
    """

    def __init__(self, my_input=None, dx=0, dy=0, dz=0):
        # type: (Position, float, float, float) -> Position
        """
        class Position initialization
        :param my_input: Position
        :param dx: float
        :param dy: float
        :param dz: float
        :rtype: Position
        """

        if my_input is None:
            self.get_origin()

        else:
            self.x = my_input.x
            self.y = my_input.y
            self.z = my_input.z
            self.x_direction = my_input.x_direction
            self.z_direction = my_input.z_direction

        self.translate(dx, dy, dz)

    def translate(self, dx=0, dy=0, dz=0):
        """
        translate position
        """
        self.x = self.x + self.x_direction * dx - self.z_direction * dz  # x translate
        self.z = self.z + self.x_direction * dz + self.z_direction * dx  # y translate
        self.y += dy  # z translate

    def get_origin(self):
        """
        get current position and direction
        """
        current_position = mc.player.getPos()  # get coordinates

        self.x = current_position.x
        self.y = current_position.y
        self.z = current_position.z
        current_direction = mc.player.getDirection()  # get direction
        self.x_direction = 0
        self.z_direction = 0
        if abs(current_direction.x) >= abs(current_direction.z):  # find dominant direction
            self.x_direction = int(round(current_direction.x))
        else:
            self.z_direction = int(round(current_direction.z))

    def rotate_left(self):
        """
        prepare rotation to left
        :rtype: None
        """
        convert = dict()
        convert[(1, 0)] = (0, -1)  # look north
        convert[(-1, 0)] = (0, 1)  # look south
        convert[(0, 1)] = (1, 0)  # look east
        convert[(0, -1)] = (-1, 0)  # look weast
        self.rotate(convert)  # call rotation

    def rotate_right(self):
        """
        prepare rotation to right
        :rtype: None
        """
        convert = dict()
        convert[(1, 0)] = (0, 1)  # look north
        convert[(-1, 0)] = (0, -1)  # look south
        convert[(0, 1)] = (-1, 0)  # look east
        convert[(0, -1)] = (1, 0)  # look weast
        self.rotate(convert)  # call rotation

    def rotate(self, convert):
        """
        do rotation

        :param convert: dictionary
        :rtype: None
        """
        buff = convert[(self.x_direction, self.z_direction)]
        self.x_direction = buff[0]
        self.z_direction = buff[1]

    @classmethod
    def origin(cls):
        # type: () -> None
        """
        get toon position to object, easy way
        :return: Position
        """
        back = cls()
        assert isinstance(back, Position)
        return back

    @classmethod
    def relative_distance(cls, dx=0, dy=0, dz=0):
        """
        toon position + relative move
        :param dx: float
        :param dy: float
        :param dz: float
        :return: Position
        """
        back = cls(None, dx, dy, dz)
        assert isinstance(back, Position)
        return back


if __name__ == "__main__":  # direct call for testing purpose
    # self test code
    first = Position()

    b = Position(first)
    print first.x
    print first.x_direction
    print first.z_direction
    first.x = 2
    first.y = 3
    first.z = 4
    second = Position(first)
    print second.x
    third = Position(second, 2, 3, 4)
    print third.x
    where_i_am = Position.origin()
    print where_i_am.x
    where_is_house = Position.relative_distance(2, 2, 2)
    print where_is_house.x
