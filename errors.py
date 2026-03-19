class RectangleError(Exception):
    """
    Rectangle Error Class
    args 
    string message
    """
    def __init__(self, message="General Rectangle Error"):
        super().__init__(message) 

    """
    String representation of error
    """
    def __repr__(self):
        return f'Rectangle Error: {self.args[0]}'