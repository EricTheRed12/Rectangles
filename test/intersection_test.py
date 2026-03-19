import unittest
from rectangle import Rectangle
from errors import RectangleError

class TestIntersection(unittest.TestCase):
    def test_validate_intersection(self):
        rect1 = Rectangle(10, 10, (10, 10))
        rect2 = Rectangle(5, 5, (5, 5))

        intersected, points = rect1.intersection(rect2)

        self.assertEqual(intersected, True)
        self.assertEqual(points, [(5.0, 5.0), (7.5, 5.0), (7.5, 7.5), (5.0, 7.5)])

    def test_validate_offset_intersection(self):
        rect1 = Rectangle(5, 10, (10, 10))
        rect2 = Rectangle(10, 5, (7, 7))

        intersected, points = rect1.intersection(rect2)

        self.assertEqual(intersected, True)
        self.assertEqual(points, [(7.5, 5.0), (12.0, 5.0), (12.0, 9.5), (7.5, 9.5)])
    
    def test_validate_non_intersection(self):
        rect1 = Rectangle(10, 10, (10, 10))
        rect2 = Rectangle(5, 5, (-5, -5))

        intersected, points = rect1.intersection(rect2)

        self.assertEqual(intersected, False)
        self.assertEqual(points, None)

    def test_invalid_rect_intersection(self):
        rect1 = Rectangle(10, 10, (10, 10))
        try: 
            intersected, points = rect1.intersection('x')
        except RectangleError as e:
            self.assertEqual(str(e), 'Invalid Rectangle')
