import math

class Cube:
    """
    A class that represents a cube.

    Attributes:
        dimensions : The dimensions of the cube
    """

    def __init__(self, *dimensions):
        """
        Constructs all the necessary attributes for the cube object.

        Args:
            dimensions : The dimensions of the cube
        """
        self.dimensions = dimensions

    def printResults(self):
        """
        Prints the results of the surface area, volume, and the diagonal space of the cube.
        """

        if len(self.dimensions) != 12 or len(set(self.dimensions)) != 1:
            print('Cube Shape Error!')
            return

        a = self.dimensions[0]

        # calculate surface area
        surface_area = 6 * math.pow(a, 2)

        # calculate volume
        volume = math.pow(a, 3)

        # calculate diagonal space
        diagonal_space = math.sqrt(3) * a

        print(f'SA: {surface_area:.1f} Vol: {volume:.1f} DS: {diagonal_space:.1f}')
