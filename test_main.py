from main import say_hello, add, sub


class TestCases():
    def test_add():
        assert add(2, 3) == 5
        print("test add passed")
    
    def test_sub():
        assert sub(5, 2) == 3
        print("test sub passed successfully")
