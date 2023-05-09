class Calculate():
    """class is created"""

    #    def __init__(self,rad):
    #       self.radius = rad

    def rectangle(self):
        """rectangle function is circle"""
        length = int(input("enter the length"))
        breadth = int(input("enter the breadth:"))
        rect_area = length * breadth
        rect_perimeter = 2 * (length + breadth)
        # if ch==1:
        print(f"the area of rectangle is{rect_area}")
        print(f"the perimeter of rectangle is{rect_perimeter}")

    def square(self):
        """square function is created"""
        side = int(input("enter the side"))
        sqt_area = side * side
        print(f"the area of square is{sqt_area}")
        sqt_perimeter = 4 * side
        print(f"the perimeter of square is{sqt_perimeter}")

    def circle(self):
        """circle function is created"""
        radius = int(input("enter the radius"))
        pi = 3.14
        circ_area = pi * radius * radius
        print(f"the area of circle is{circ_area}")
        circ_peri = 2 * pi * radius
        print(f"the perimeter of circle is{circ_peri}")

    def triangle_1(self):
        """triangle function is created"""
        base = int(input("enter the base"))
        height = int(input("enter the height"))
        side = int(input("enter the side"))
        tri_area = (1 / 2 * base * height)
        print(f"the area of triangle is{tri_area}")
        tri_perimeter = base + height + side
        print(f"the perimeter of triangle is{tri_perimeter}")


if __name__ == '__main__':
    Ch = 1
    while Ch != 0:
        """loop is created"""
        shape_name = Calculate()

        print("1:Rectangle")
        print("2:Square")
        print("3:Circle")
        print("4:Triangle")
        Ch = int(input("enter the name of the shape:"))
        print("calculate shape:")
        # shape_name.Circle()
        if Ch == 1:
            shape_name.rectangle()
        elif Ch == 2:
            shape_name.square()
        elif Ch == 3:
            shape_name.circle()
        elif Ch == 4:
            shape_name.triangle_1()
        else:
            print("invalid")
