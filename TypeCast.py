from functools import wraps
def cast(typeC):
    def decorator(f):
        @wraps(f)
        def newfun(*args):
            return typeC(f(*args))
        return newfun
    return decorator
