import functools
class counter:
    cnt = 0
    def __init__(self,fun):
        functools.update_wrapper(self, fun)
        self._fun = fun
    def __call__(self, *args):
        self.cnt += 1
        return self._fun(*args)
    def counter(self):
        return self.cnt


