from typing import Callable


def builder(func: Callable) -> Callable:
    import copy
    def _copy(self, *args, **kwargs):
        self_copy = copy.copy(self) if getattr(self, "immutable", True) else self
        result = func(self_copy, *args, **kwargs)
        if result is None:
            return self_copy
        return result
    return _copy

def set_class_attribute(obj, key, value):
    from model.Table import Table
    from model.Column import Column
    if isinstance(obj, Table) or isinstance(obj, Column):
        setattr(obj, key, value)