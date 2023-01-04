'''Create a method named check_angles. The sum of a triangle's three angles should return
True if the sum is equal to 180, and False otherwise. The method should print whether the
angles belong to a triangle or not.
11.1 Write methods to verify if the triangle is an acute triangle or obtuse triangle.
11.2 Create an instance of the triangle class and call all the defined methods.
11.3 Create three child classes of triangle class - isosceles_triangle, right_triangle and
equilateral_triangle.
11.4 Define methods which check for their properties.
'''


class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        print(self.is_right_triangle())

    def type_of_triangle(self):
        if self.a < 90 and self.b < 90 and self.c < 90:
            return "Acute"
        return "Obtuse"

    def is_right_triangle(self):
        if sum((self.a, self.b, self.c)) == 180:
            return True
        return False


class Isosceles_triangle(Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def check(self):
        if self.a == self.b or self.b == self.c or self.c == self.a:
            return True
        return False


class Right_triangle(Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def check(self):
        if self.a == 90 or self.b == 90 or self.c == 90:
            return True
        return False


class Equilateral_triangle(Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def check(self):
        if self.a == self.b == self.c:
            return True
        return False


# TESTS:
t1 = Isosceles_triangle(60, 60, 60)
print(t1.check())
t2 = Right_triangle(90, 30, 60)
print(t2.check())
t3 = Equilateral_triangle(60, 60, 60)
print(t3.check())
t1 = Isosceles_triangle(70, 55, 55)
print(t1.check())
t2 = Right_triangle(60, 60, 60)
print(t2.check())
t3 = Equilateral_triangle(60, 59, 61)
print(t3.check())


