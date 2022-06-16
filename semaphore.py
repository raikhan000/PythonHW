a = 0
class Lock:
    c = 0
    name_current = {}
    name_future = {}
    @property
    def lock(self):
        #print(str(self))
        if str(self) not in Lock.name_current:
            if str(self) in Lock.name_future:
                a = Lock.name_future[str(self)]
                if a not in Lock.name_current.values():
                    Lock.name_current[str(self)] = Lock.name_future[str(self)]
                    Lock.name_future.pop(str(self))
                    return Lock.name_current[str(self)]
                else:
                    try:
                        b = Lock.name_current[str(self)]
                    except KeyError:
                        return
                    else:
                        return b
            else:
                return
        else:
            return Lock.name_current[str(self)]

    @lock.setter
    def lock(self,val):

        if str(self) in Lock.name_current:
            Lock.name_future[str(self)] = val
            Lock.name_current.pop(str(self))
        else:
            Lock.name_future[str(self)] = val


    @lock.deleter
    def lock(self):
        try:
            a = Lock.name_current[str(self)]
        except KeyError:
            pass
        else:
            for i in Lock.name_future:
                if Lock.name_future[i] == a:
                    Lock.name_current[i] = a
                    break
            Lock.name_current[str(self)] = None
    def __del__(self):
        if str(self) in Lock.name_current:
            del self.lock

    def locked(self):
        def inner(arg):
            type(self(arg)).__del__ = Lock.__del__
            #type(self(arg)).deleted_item = 0
            self.lock = Lock.lock

            return self(arg)
        return inner


