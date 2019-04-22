from functools import singledispatch
from typing import Union
import numpy as np

# ------------------------------------------- Base Infix Class Creation -------------------------------------------


def __l_name(op):
    """The left name of an op https://github.com/borntyping/python-infix"""
    return '__' + op + '__'


def __r_name(op):
    """The right name of an op, switches shifts https://github.com/borntyping/python-infix"""
    shifts = {'lshift', 'rshift'}
    if op in shifts:
        op = list(shifts - {op})[0]
    return '__r' + op + '__'


class _Infix(np.ndarray):
    """
    Base Infix class for numpy arrays.
    Possible combinations are: |op|
    Based on stack overflow post:
        http://code.activestate.com/recipes/577201-infix-operators-for-numpy-arrays/
    """
    def __new__(cls, function):
        obj = np.ndarray.__new__(cls, 0)
        obj.function = function
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return
        self.function = getattr(obj, 'function', None)

    def __call__(self, value1, value2):
        return self.function(value1, value2)

    def right(self, other):
        return _Infix(lambda x, self=self, other=other: self.function(other, x))

    def left(self, other):
        return self.function(other)


__ops = ['or']    # only use OR, but can extend to use any operations
__d = {**{__l_name(op): _Infix.left for op in __ops}, **{__r_name(op): _Infix.right for op in __ops}}  # define op functions
[setattr(_Infix, op, __d[op]) for op in __d]  # set Infix's ops to the corresponding functions we defined above


# ----------------------------------- Sub-Utilities to Create the Main Utilities -----------------------------------


@singledispatch
def __hconcat(*_) -> np.ndarray: pass


@singledispatch
def __vconcat(*_) -> np.ndarray: pass


@__hconcat.register(int)
def __hconcat_scalar_back(x, y) -> np.ndarray: return np.hstack((np.ones((y.shape[0], 1)) * x, y))


@__hconcat.register(np.ndarray)
def __hconcat_scalar_front(x, y) -> np.ndarray: return np.hstack((x, np.ones((x.shape[0], 1)) * y))


@__vconcat.register(int)
def __vconcat_scalar_top(x, y) -> np.ndarray: return np.vstack((np.ones((1, y.shape[0])) * x, y))


@__vconcat.register(np.ndarray)
def __vconcat_scalar_bottom(x, y) -> np.ndarray: return np.vstack((x, np.ones((1, x.shape[0])) * y))


@singledispatch
def __add_dim(*_) -> np.ndarray: pass


@__add_dim.register(int)
def __add_dim_int(axis, x) -> np.ndarray: return np.expand_dims(x, axis=axis)


@__add_dim.register(tuple)
def __add_dim_tuple(axes, x) -> np.ndarray:
    x_ = x.copy()
    for axis in axes:
        x_ = __add_dim_int(axis, x_)
    return x_


# ---------------------------------------------- Main Utilities ----------------------------------------------


@_Infix
def hcat(x: Union[int, np.ndarray], y: Union[int, np.ndarray]) -> np.ndarray:
    """
    Horizontal concatenation of np.ndarrays or np.ndarrays and scalars.
    Usage: array |hcat| 1, 1 |hcat| array, or array |hcat| array
    """
    return __hconcat(x, y) if not (isinstance(x, np.ndarray) and isinstance(y, np.ndarray)) else np.hstack((x, y))


@_Infix
def vcat(x: Union[int, np.ndarray], y: Union[int, np.ndarray]) -> np.ndarray:
    """
    Vertical concatenation of np.ndarrays or np.ndarrays and scalars.
    Usage: array |vcat| 1, 1 |vcat| array, or array |vcat| array
    """
    return __vconcat(x, y) if not (isinstance(x, np.ndarray) and isinstance(y, np.ndarray)) else np.vstack((x, y))


@_Infix
def add_dim(x: np.ndarray, axis: Union[int, tuple]) -> np.ndarray:
    """
    Adds a dimension to x along axis. Sequentially adds dimensions if axis is tuple.
    Usage: array |add_dim| -1, array |add_dim| (0, 0, -1)
    """
    return __add_dim(axis, x)


@_Infix
def to_type(x: Union[np.ndarray, list], dtype: np.dtype) -> np.ndarray:
    """
    Converts x to given dtype if x is an array. If x is a list, will convert x to array and then convert to dtype.
    Usage: array |to_type| np.int, list |to_type| np.float
    """
    return x.astype(dtype) if isinstance(x, np.ndarray) else np.array(x).astype(dtype)


@_Infix
def eq(x: Union[np.ndarray, list, tuple], y: Union[np.ndarray, list, tuple]) -> bool:
    """
    Determines whether (x == y).all(). If x or y is a list or tuple, we convert to numpy arrays.
    """
    return np.equal(np.array(x), np.array(y)).all()


def equals(x: Union[np.ndarray, list, tuple], y: Union[np.ndarray, list, tuple]) -> bool:
    """
    Functional equivalent to eq without infix.
    """
    return np.equal(np.array(x), np.array(y)).all()


def make_constant(value: float, shape: tuple, **kwargs) -> np.ndarray:
    """
    Makes an array of the given shape filled with the given value.
    """
    return np.ones(shape, **kwargs) * value


def make_array(x: Union[np.ndarray, list, tuple], shape: tuple, **kwargs) -> np.ndarray:
    """
    Makes an array with values x and reshapes to shape.
    """
    return np.array(x, **kwargs).reshape(shape)
