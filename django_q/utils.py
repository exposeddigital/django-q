import inspect


def get_func_repr(func):
    # convert func to string
    if inspect.isfunction(func):
        return f"{func.__module__}.{func.__name__}"
    elif inspect.ismethod(func) and hasattr(func.__self__, "__name__"):
        return (
            f"{func.__self__.__module__}." f"{func.__self__.__name__}.{func.__name__}"
        )
    else:
        return str(func) if func else None
