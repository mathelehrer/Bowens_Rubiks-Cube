class TriangleNumber:
    def __init__(self,n:int):
        """
        return the nth triangle number
        """
        self.n = n
        self._size:int = None

    @property
    def size(self)->int:
        if self._size is None:
            self._size=self.n*(self.n-1)//2
        return self._size

if __name__ == '__main__':
    for i in range(12):
        print(TriangleNumber(i).size)
