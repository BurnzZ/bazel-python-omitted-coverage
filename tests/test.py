from src.has_tests import has_tests


def test_has_tests() -> None:
    assert has_tests(1, 2) == 3


if __name__ == "__main__":
    test_has_tests()
