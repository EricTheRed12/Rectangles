import unittest
from rectangle import Rectangle
from errors import RectangleError

class TestRectangle(unittest.TestCase):
    def test_verify_rectangle(self):
        rect1 = Rectangle(10, 10, (10, 10))
        
        self.assertEqual(rect1.center, (10, 10))
        self.assertEqual(rect1.left, 5)
        self.assertEqual(rect1.right, 15)
        self.assertEqual(rect1.bottom, 5)
        self.assertEqual(rect1.top, 15)

    def test_odd_rectangle(self):
        rect1 = Rectangle(9, 9, (9, 9))
        
        self.assertEqual(rect1.center, (9, 9))
        self.assertEqual(rect1.left, 4.5)
        self.assertEqual(rect1.right, 13.5)
        self.assertEqual(rect1.bottom, 4.5)
        self.assertEqual(rect1.top, 13.5)

    def test_negative_rectangle(self):
        rect1 = Rectangle(10, 10, (-10, -10))
        
        self.assertEqual(rect1.center, (-10, -10))
        self.assertEqual(rect1.left, -15)
        self.assertEqual(rect1.right, -5)
        self.assertEqual(rect1.bottom, -15)
        self.assertEqual(rect1.top, -5)

    def test_invalid_center(self):
        try: 
            rect1 = Rectangle(10, 10, 'x')
        except RectangleError as e:
            self.assertEqual(str(e), 'Invalid Center')

    def test_invalid_center_2(self):
        try: 
            rect1 = Rectangle(10, 10, (0, 'x'))
        except RectangleError as e:
            self.assertEqual(str(e), 'Invalid Center')

    def test_invalid_height(self):
        try: 
            rect1 = Rectangle(10, 'x',  (10, 10))
        except RectangleError as e:
            self.assertEqual(str(e), 'Invalid Height')

    def test_invalid_width(self):
        try: 
            rect1 = Rectangle('x', 10, (10, 10))
        except RectangleError as e:
            self.assertEqual(str(e), 'Invalid Width')
