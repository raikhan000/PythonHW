class sizer:
    def __init__(self, cls):
        from functools import update_wrapper
        self = update_wrapper(self, cls)
        self.cls = cls
        self.type = cls.__bases__[0]

    def __call__(self, *args):
        if len(args) != 0:
            self.val = (self.type)(args[0])
            self.cls.size = self.size
            return self.cls(self.val)
        else:
            self.val = ()
            self.cls.size = self.size
            return self.cls()

    @property
    def size(self):
        if "__len__" in dir(self.cls):
            return self.cls.__len__(self.val)
        elif "__abs__" in dir(self.cls):
            return self.cls.__abs__(self.val)
        else:
            return 0





