def sin_in_degrees(x):
    """Return the sine of the argument.

    Input
    -----
    x - degrees.  scalar.
    """
    import math
    return math.sin(x)

def test_sin_in_degrees_0():
    """Test that our sin_in_degrees function passes obvious cases."""
    x = 0
    expect = 0
    observed = sin_in_degrees(x)

    if expect == observed:
        print("Passed")
    else:
        print("Failed")

def test_sin_in_degrees_90():
    """Test that our sin_in_degrees function passes obvious cases."""
    x = 90
    expect = 1
    observed = sin_in_degrees(x)

    if expect == observed:
        print("Passed")
    else:
        print("Failed")

if __name__ == "__main__":
    test_sin_in_degrees_0()
    test_sin_in_degrees_90()
