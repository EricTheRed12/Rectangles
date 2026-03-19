import unittest
from rectangle import Rectangle
from errors import RectangleError

class TestContainment(unittest.TestCase):
    def test_validate_containment(self):
        rect1 = Rectangle(10, 10, (10, 10))
        rect2 = Rectangle(5, 5, (10, 10))

        contained = rect1.containment(rect2)

        self.assertEqual(contained, True)

    def test_validate_partial_containment(self):
        rect1 = Rectangle(5, 10, (10, 10))
        rect2 = Rectangle(10, 5, (7, 7))

        contained = rect1.containment(rect2)

        self.assertEqual(contained, False)
    
    def test_validate_non_containment(self):
        rect1 = Rectangle(10, 10, (10, 10))
        rect2 = Rectangle(5, 5, (-5, -5))

        contained = rect1.containment(rect2)

        self.assertEqual(contained, False)

    def test_invalid_rect_containment(self):
        rect1 = Rectangle(10, 10, (10, 10))
        try: 
            intersected, points = rect1.intersection('x')
        except RectangleError as e:
            self.assertEqual(str(e), 'Invalid Rectangle')