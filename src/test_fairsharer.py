from fair_sharer import fair_sharer


def test_fair_sharer():
    values = [0, 0, 800, 1000]  # Max value is at the last index
    num_iterations = 1
    share = 0.1
    expected_values = [100, 0, 900, 800]
    result = fair_sharer(values, num_iterations, share)
    assert result == expected_values
def test_fair_sharer_result():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]