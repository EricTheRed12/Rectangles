import unittest
from rectangle import Rectangle
from errors import RectangleError

class TestAdjacent(unittest.TestCase):
    def test_validate_adjacent_top(self):
        rect1 = Rectangle(10, 5, (0, 0))
        rect2 = Rectangle(5, 5, (0, 5))

        adjacent = rect1.adjacent(rect2)

        self.assertEqual(adjacent, True)

    def test_validate_adjacent_bottom(self):
        rect1 = Rectangle(10, 5, (0, 0))
        rect2 = Rectangle(5, 5, (0, -5))

        adjacent = rect1.adjacent(rect2)

        self.assertEqual(adjacent, True)
    
    def test_validate_adjacent_left(self):
        rect1 = Rectangle(5, 10, (0, 0))
        rect2 = Rectangle(5, 5, (-5, 0))

        adjacent = rect1.adjacent(rect2)

        self.assertEqual(adjacent, True)

    def test_validate_adjacent_right(self):
        rect1 = Rectangle(5, 10, (0, 0))
        rect2 = Rectangle(5, 5, (5, 0))

        adjacent = rect1.adjacent(rect2)

        self.assertEqual(adjacent, True)
    
    def test_validate_adjacent_corner(self):
        rect1 = Rectangle(5, 5, (0, 0))
        rect2 = Rectangle(5, 5, (5, 5))

        adjacent = rect1.adjacent(rect2)

        self.assertEqual(adjacent, False)

    def test_validate_non_adjacent(self):
        rect1 = Rectangle(10, 10, (10, 10))
        rect2 = Rectangle(5, 5, (5, 5))

        adjacent = rect1.adjacent(rect2)

        self.assertEqual(adjacent, False)

    def test_invalid_rect_adjacent(self):
        rect1 = Rectangle(10, 10, (10, 10))
        try: 
            intersected, points = rect1.intersection('x')
        except RectangleError as e:
            self.assertEqual(str(e), 'Invalid Rectangle')