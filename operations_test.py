

from operations import add


def test_add():
    # given
    x = 5
    y = 10
    # when
    result = add(x,y)
    # then
    assert result == 15


def test_add_simple():
    assert add(5, 10) == 15