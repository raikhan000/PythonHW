def BinPow(pyObj,N, func):
    if (type(pyObj) == str or type(pyObj) == list or type(pyObj) == tuple) and func == type(pyObj).__add__:
        #for i in range(N):
        return pyObj*N
    else:
        result = func(pyObj, pyObj)
        for i in range(2, N):
            result = func(result,pyObj)

        return result




