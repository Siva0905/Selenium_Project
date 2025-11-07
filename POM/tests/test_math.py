def test_fibonacci():
    assert [0, 1, 1, 2, 3, 5][5] == 5
def test_prime():
    assert all(7 % i != 0 for i in range(2, int(7**0.5)+1))
def test_statistics():
    assert sum([1,2,3,4,5])/5 == 3
