class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message= message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message= message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity=capacity
        self.element=[]
        self.index=0

    def read(self):
        if len(self.element)==0:
            raise BufferEmptyException('Circular buffer is empty')
        readed=self.element.pop(0)
        return readed

    def write(self, data):
        if len(self.element) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.element.append(data)  

    def overwrite(self, data):
        if len(self.element) < self.capacity:
            return self.element.append(data)
        self.element.pop(0)
        self.element=self.element + [data]
        return self.element

    def clear(self):
        self.element=[]
        self.index=0
