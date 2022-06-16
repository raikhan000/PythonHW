class DivStr(str):
    def __floordiv__(self, other):
        k = len(self)//other
        if k == 0:
            return ['']*other
        else:
            return [self[i:i+k] for i in range(0,len(self), k) if i + k <= len(self)]
    def __mod__(self, other):
        k = len(self)%other
        return type(self)(self[len(self) - k:])
    def __getitem__(self, item):
        return type(self)(str(self).__getitem__(item))
    def __add__(self, other):
        return type(self)(str(self).__add__(other))
    def __mul__(self, other):
        return type(self)(str(self).__mul__(other))
    def __rmul__(self, other):
        return type(self)(str(self).__rmul__(other))
    def lower(self) -> str:
        return type(self)(str(self).lower())
    def upper(self) -> str:
        return type(self)(str(self).upper())
    def join(self, iterable) -> str:
        return type(self)(str(self).join(iterable))
    def capitalize(self) -> str:
        return type(self)(str(self).capitalize())
    def swapcase(self) -> str:
        return type(self)(str(self).swapcase())
    def title(self):
        return type(self)(str(self).title())
    def zfill(self, width) -> str:
        return type(self)(str(self).zfill(width))
    def ljust(self, width: int, fillchar: str = ...) -> str:
        return type(self)(str(self).ljust(width, fillchar))
    def rjust(self, width: int, fillchar: str = ...) -> str:
        return type(self)(str(self).rjust(width,fillchar))
    def casefold(self) -> str:
        return type(self)(str(self).casefold())
    def replace(self, old: str, new: str, count = -1) -> str:
        return type(self)(str(self).replace(old,new, count))
    def strip(self, chars = None) -> str:
        return type(self)(str(self).strip(chars))
    def rstrip(self, chars = None) -> str:
        return type(self)(str(self).rstrip(chars))
    def lstrip(self, chars = None) -> str:
        return type(self)(str(self).lstrip(chars))
    def translate(self, table) -> str:
        return type(self)(str(self).translate(table))
    def center(self, width: int, fillchar: str = ...) -> str:
        return type(self)(str(self).center(width,fillchar))
    def removeprefix(self, string):
        return type(self)(str(self).removeprefix(string))
    def removesuffix(self,string):
        return type(self)(str(self).removesuffix(string))




