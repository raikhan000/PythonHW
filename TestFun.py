class Tester:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, suite, allowed = []):
        flag = 0
        allowed = [allowed[i].__name__ for i in range(len(allowed))]
        for i in suite:
            try:
                self.fun(*i)
            except Exception as e:
                if type(e).__name__ in allowed or 'Exception' in allowed:
                    flag = -1
                else:
                    return 1
        return flag

