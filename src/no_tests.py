"""This represents a file that is NOT tested.

Running `bazel coverage` should produce a coverage report that includes this file.
"""

def no_tests(x: int, y: int) -> int:
    return x + y
