class Dots:
    first = 0
    last = 0
    def __init__(self, _first, _last):
        self.first = _first
        self.last = _last


    def __getitem__(self, idx1):
        if isinstance(idx1, slice):
            c = [idx1.start,idx1.stop, idx1.step]
            if c[0] == None:
                c[0] = 0

            if c[2] == None:
                d = (self.last - self.first) / (c[1] - 1)
                return float(self.first + c[0] * d)
            else:
                if c[1] == None:
                    c[1] = c[2]
                d = round((self.last - self.first) / (c[2] - 1), 15)
                return (float(self.first + i*d) for i in range(c[0], c[1]))

        else:
            d = (self.last - self.first) / (idx1 - 1)
            return (float(self.first + i*d) for i in range(idx1))
