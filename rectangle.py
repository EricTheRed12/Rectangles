from errors import RectangleError

class Rectangle():
    """
    initalizes Rectangle
    args 
    width int or float
    height int or float
    center list of two (int or float)
    throws 
    invalid rectangle error
    """
    def __init__(self, width, height, center):
        if not isinstance(center, list) and len(center) != 2: 
            raise RectangleError("Invalid Center")
        elif not isinstance(center[0], (int, float)) or not isinstance(center[1], (int, float)):
            raise RectangleError("Invalid Center")
        elif not isinstance(width, (int, float)):
            raise RectangleError("Invalid Width")
        elif not isinstance(height, (int, float)):
            raise RectangleError("Invalid Height")
        self.center = center
        # calculates hight from the center
        halfH = abs(height/2)
        # calculates width from the center
        halfW = abs(width/2)

        # calculates position og the edges in relation to the center
        self.left = center[0] - halfW
        self.right = center[0] + halfW
        self.bottom = center[1] - halfH
        self.top = center[1] + halfH

    """ 
    calculates if the currecnt rectangle intersects a given rectangle 
    args 
    rectangle
    returns 
    intersection boolean
    list of intersection points (int or float)
    throws 
    invalid rectangle error
    """
    def intersection(self, rectangle):
        if not isinstance(rectangle, Rectangle):
            raise RectangleError("Invalid Rectangle") 
        # checks if any given edge of the rectangle overlaps
        if (self.right <= rectangle.left or self.left >= rectangle.right 
            or self.top <= rectangle.bottom or self.bottom >= rectangle.top):
            return False, None

        # calculate the intersection of the rectangle edges
        intersection_left = max(self.left, rectangle.left)
        intersection_right = min(self.right, rectangle.right)
        intersection_bottom = max(self.bottom, rectangle.bottom)
        intersection_top = min(self.top, rectangle.top)

        # initalize the points of intersection
        points_of_intersection = [
            (intersection_left, intersection_bottom),
            (intersection_right, intersection_bottom),
            (intersection_right, intersection_top),
            (intersection_left, intersection_top)
        ]
        return True, points_of_intersection

    """ 
    calculates if the current rectangle is contained within a given rectangle
    args 
    rectangle
    returns 
    containment boolean
    throws 
    invalid rectangle error
    """
    def containment(self, rectangle):
        if not isinstance(rectangle, Rectangle):
            raise RectangleError("Invalid Rectangle") 
        # contained any negative edge is greater than or any positive edge is less than the given rectangle
        return (self.left <= rectangle.left and
        rectangle.right <= self.right and
        self.bottom <= rectangle.bottom and
        rectangle.top <= self.top)

    """ 
    calculates if the current rectangle is adjacent to a given rectangle
    args 
    rectangle
    returns 
    adjacent boolean
    throws 
    invalid rectangle error
    """
    def adjacent(self, rectangle):
        if not isinstance(rectangle, Rectangle):
            raise RectangleError("Invalid Rectangle") 
        # calculates adjacency of veriticle edge, by checking horizontal position and vertical lengths overlap
        if ((self.left == rectangle.right or self.right == rectangle.left) and
            max(self.bottom, rectangle.bottom) < min(self.top, rectangle.top)):
            return True

        # calculates adjacency of horizontal edge, by checking horizovertical position and horizontal lengths overlap
        if ((self.bottom == rectangle.top or self.top == rectangle.bottom) and
            max(self.left, rectangle.left) < min(self.right, rectangle.right)):
            return True

        return False
    
    """
    String representation of rectangle
    """
    def __str__(self):
        # returns a string representation of the rectangle object
        return f'| Center: {self.center} | Left: {self.left} | Right: {self.right} | Top: {self.top} | Bottom: {self.bottom} |'