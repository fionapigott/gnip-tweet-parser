from functools import wraps

def lazy_property(fn):
    """
    Decorator that makes a property lazy-evaluated whilst preserving
    docstrings.

    Args:
        fn (function): the property in question

    Returns:
        evaluated version of the property.
    """
    attr_name = '_lazy_' + fn.__name__

    @property
    @wraps(fn)
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazy_property
