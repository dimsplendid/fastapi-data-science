import pytest

from introduction import add

@pytest.mark.parametrize(
    "a, b, expected", 
    [
        (1, 2, 3),
        (2, 2, 4),
        (3, 2, 5),
        (4, 2, 6),
    ]
)
def test_add(a, b, expected):
    assert add(a, b) == expected