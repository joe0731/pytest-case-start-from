"""
Example test file to demonstrate pytest-start-from plugin functionality
"""
import pytest


def test_first():
    """first test case"""
    print("\nExecuting test_first")
    assert True


def test_second():
    """second test case"""
    print("\nExecuting test_second")
    assert True


def test_third():
    """third test case"""
    print("\nExecuting test_third")
    assert True


def test_fourth():
    """fourth test case"""
    print("\nExecuting test_fourth")
    assert True


def test_fifth():
    """fifth test case"""
    print("\nExecuting test_fifth")
    assert True


class TestClass:
    """test class with multiple methods"""
    
    def test_class_first(self):
        """first test in class"""
        print("\nExecuting test_class_first")
        assert True
    
    def test_class_second(self):
        """second test in class"""
        print("\nExecuting test_class_second")
        assert True
    
    def test_class_third(self):
        """third test in class"""
        print("\nExecuting test_class_third")
        assert True


def test_with_parameters_a():
    """test with parameter in name"""
    print("\nExecuting test_with_parameters_a")
    assert True


def test_with_parameters_b():
    """another test with parameter in name"""
    print("\nExecuting test_with_parameters_b")
    assert True


def test_last():
    """last test case"""
    print("\nExecuting test_last")
    assert True
