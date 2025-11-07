def test_return_type():
    assert isinstance((lambda: 5)(), int)
def test_param_type():
    assert (lambda x: x)(3) == 3
def test_type_conversion():
    assert int("5") == 5
class MyClass:
    pass
def test_class_instance():
    assert isinstance(MyClass(), MyClass)