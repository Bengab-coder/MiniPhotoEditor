class MouseEvent:
    def __init__(self, _id, x, y):
        self._id = _id
        self.x = x
        self.y = y

    def __repr__(self):
        return f"MouseEvent<id={self._id}|x={self.x}|y={self.y}>"
