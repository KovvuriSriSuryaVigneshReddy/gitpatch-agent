from tests.sample import calculate_discount

def test_calculate_discount():
    # 100 with 20% (0.20) discount must equal 80.0
    assert calculate_discount(100.0, 0.20) == 80.0
