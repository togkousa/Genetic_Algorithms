import pytest

from numpy_utils import *


@pytest.fixture
def arr() -> np.ndarray:
    return np.array([[1, 1], [-1, 0]])


@pytest.fixture
def arr_alt() -> np.ndarray:
    return np.array([[1, 1, 1], [-1, 0, 0], [1, 1, 1]])


@pytest.mark.incremental
class Test:

    def test_equals(self, arr):
        assert (arr | eq | arr)
        assert (arr | eq | list(arr))
        assert (arr | eq | list(arr))
        assert (tuple(arr) | eq | list(arr))
        assert equals(arr, arr)

    def test_hcat(self, arr, arr_alt):
        assert ((arr | hcat | 6) | eq | np.array([[1., 1., 6.], [-1., 0., 6.]]))
        assert ((3 | hcat | arr) | eq | np.array([[3., 1., 1.], [3., -1., 0.]]))

        assert ((arr | hcat | arr) | eq | np.array([[1., 1., 1., 1.], [-1., 0., -1., 0]]))
        assert ((arr | hcat | 9 | hcat | arr) | eq | np.array([[1., 1., 9., 1., 1.], [-1., 0., 9., -1., 0]]))

        with pytest.raises(ValueError):
            (arr | hcat | arr_alt)

    def test_vcat(self, arr, arr_alt):
        assert ((arr | vcat | 6) | eq | np.array([[1., 1.], [-1., 0.], [6., 6.]]))
        assert ((3 | vcat | arr) | eq | np.array([[3., 3.], [1., 1.], [-1., 0.]]))

        assert ((arr | vcat | arr) | eq | np.array([[1., 1.], [-1., 0.], [1., 1.], [-1., 0.]]))
        assert ((arr | vcat | 9 | vcat | arr) | eq | np.array([[1., 1.], [-1., 0.], [9., 9.], [1., 1.], [-1., 0.]]))

        with pytest.raises(ValueError):
            (arr | vcat | arr_alt)

    def test_add_dim(self, arr):
        assert (arr | add_dim | -1).shape == (2, 2, 1)
        assert (arr | add_dim | (0, 0, -1)).shape == (1, 1, 2, 2, 1)

    def test_to_type(self, arr):
        assert (arr | to_type | np.float).dtype == np.float
        assert (list(arr) | to_type | np.uint8).dtype == np.uint8

    def test_make_constant(self):
        assert make_constant(1, (3, 1)) | eq | np.array([[1.], [1.], [1.]])

    def test_make_array(self):
        assert make_array([1, 2, 3], (1, 3)) | eq | np.array([[1, 2, 3]])
        with pytest.raises(ValueError):
            make_array([1, 2, 3], (1, 4))