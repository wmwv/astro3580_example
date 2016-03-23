from nose.tools import assert_equal, assert_sequence_equal
from numpy.testing import assert_almost_equal, assert_array_almost_equal, assert_array_almost_equal_nulp

def sin_in_degrees(x):
    """Return the sine of the argument.

    Input
    -----
    x - degrees.  scalar.
    """
    import math
    import numpy as np
    x_in_degrees = np.deg2rad(x)
    return math.sin(x_in_degrees)

def test_sin_in_degrees_0():
    """Test that our sin_in_degrees function passes obvious cases."""
    x = 0
    expected = 0
    observed = sin_in_degrees(x)
    assert_almost_equal(observed, expected)

def test_sin_in_degrees_90():
    """Test that our sin_in_degrees function passes obvious cases."""
    x = 90
    expected = 1
    observed = sin_in_degrees(x)
    assert_almost_equal(observed, expected)

if __name__ == "__main__":
    test_sin_in_degrees_0()
    test_sin_in_degrees_90()
