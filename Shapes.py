'''import thr math library'''
import math


class Shape:
    """ it is a method 
    """
    # def area(self):
    # """Creating a area function"""
    #     pass
    # def perimeter(self):
    #     """ creating a perimter function
    #     """
    #     pass

    # def volume(self):
    #     """ creating a volume function
    #     """
    #     pass


class Square(Shape):
    """Class is created for square 

    Args:
        Shape (int): calling a fuction 
    """

    def __init__(self, size):
        """Main function 

        Args:
            size (int): value is passed in size 
        """
        self.size = size

    def area(self):
        """ returns the value 

        Returns:
            int : size value is calculated 
        """
        return self.size ** 2

    def perimeter(self):
        """_summary_

        Returns:
            int : perimeter value is calculated
        """
        return 4**self.size

    def volume(self):
        """_summary_

        Returns:
            int : 
        """
        return 0


class Rectangle(Shape):
    """ Rectangle class is created 

    Args:
        Shape (int): class is created _
    """

    def __init__(self, length, width):
        """

        Args:
            length (int):  length value is called
            width (int):  width value is called
        """
        self.length = length
        self.width = width

    def area(self):
        """_summary_

        Returns:
            int : area is calculated
        """
        return self.length * self.width

    def perimeter(self):
        """
        Returns:
            int : perimeter value is calculated
        """
        return 2*(self.length + self.width)

    def volume(self):
        """
        Returns:
            int : volume is calculated 
        """
        return (2)*(self.length + self.width)


class TriangleShape(Shape):
    '''create the class as triangle shape'''

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """_summary_

        Returns:
            float : area value is calculated
        """
        return 1/2 * self.base * self.height

    def perimeter(self):
        """_summary_

        Returns:
            float : Perimeter value is calculated
        """
        return self.base + self.height


class CricleShape(Shape):
    '''Create the class as circle shape'''

    def __init__(self, radius):
        """_summary_

        Args:
            radius (int): radius value is called
        """
        self.radius = radius

    def area(self):
        """
        Args:
            radius (int): area is calculated

        """

        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Args:
        radius (int) : perimeter is called
        """
        return 2*math.pi * self.radius

    def volume(self):
        '''Function is created '''
        return 0


class Cube(Shape):
    '''Class is created for cube '''

    def __init__(self, sizes3):
        '''Main function of cube is created '''
        self.sizes = sizes3

    def area(self):
        '''No area'''
        return 0

    def perimeter(self):
        '''No perimeter'''
        return 0

    def volume(self):
        '''volume is defined in function'''
        return self.sizes*3
class Prism(Shape):
    '''Class is created for cube '''

    def __init__(self, bases_1, height_1):
        '''Main function of cube is created '''
        self.area_base_1 = bases_1
        self.height_1 = height_1

    def area(self):
        '''No area'''
        return 0

    def perimeter(self):
        '''No perimeter'''
        return 0

    def volume(self):
        '''volume is defined in function'''
        return self.area_base_1*self.height_1


print("""Select the Shapes name:
1.Square                                 
2.Rectangle
3.Triangle
4.Cricle
5.Cube
6.Prism """)
user_variable = int(input("Enter the shape number :"))
if user_variable == 1:
    size_1 = int(input("enter the values"))
    obj1 = Square(size_1)
    obj2 = Square(size_1)
elif user_variable == 2:
    length_1 = input("Enter the length")
    width_1 = input("Enter the width")
    obj1 = Rectangle(length_1, width_1)
    obj2 = Rectangle(length_1, width_1)
elif user_variable == 3:
    base_1 = int(input("Enter the value : "))
    heigth = int(input("Enter the value : "))
    obj1 = TriangleShape(base_1, heigth)
    obj2 = TriangleShape(base_1, heigth)
elif user_variable == 4:
    radius_1 = float(input("Enter the value: "))
    obj1 = CricleShape(radius_1)
    obj2 = CricleShape(radius_1)
    obj3 = CricleShape(radius_1)
elif user_variable == 5:
    size2 = int(input("Enter the value: "))
    obj1 = Cube(size2)
    obj2 = Cube(size2)
    obj3 = Cube(size2)
elif user_variable == 6:
    Area_of_bases = int(input("Enter the value: "))
    Heights = int(input("Enter the value"))
    obj1 = Prism(Area_of_bases,Heights)
    obj2 = Prism(Area_of_bases,Heights)
    obj3 = Prism(Area_of_bases,Heights)
else:
    print("Not identified")

print("Area of shape:", obj1.area())
print("Perimeter of shape", obj2.perimeter())
print("volume of shape", obj3.volume())
