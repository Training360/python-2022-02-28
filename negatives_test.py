from negatives import count_negatives


def test_normal():
    # Given
    input = [1, 2, 3, -4, 5, -6]
    # When
    actual_value = count_negatives(input)
    # Then
    assert 2 == actual_value

def test_only_negatives():
    # Given
    input = [-1, -1, -1, -1]
    # When
    actual_value = count_negatives(input)
    # Then
    assert 4 == actual_value

def test_only_positives():
    # Given
    input = [1, 2, 3, 4]
    # When
    actual_value = count_negatives(input)
    # Then
    assert 0 == actual_value