def test_list_sorting():
    assert sorted([3, 1, 2]) == [1, 2, 3]
def test_dict_key_value():
    assert {"a": 1, "b": 2}["a"] == 1
def test_set_operations():
    assert {1, 2, 3} & {2, 3, 4} == {2, 3}
def test_list_comprehension():
    assert [x*x for x in range(3)] == [0, 1, 4]