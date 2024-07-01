#jetsadaphon bokprakhon 
import pytest
import source.print_promotion as print_promotion_function


def test_print_promotion():
    result = print_promotion_function.print_promotion(10.0)
    assert result == "Warning"

def test_print_promotion():
    result = print_promotion_function.print_promotion(True)
    assert result == "Warning"

def test_print_promotion():
    result = print_promotion_function.print_promotion("Hello")
    assert result == "Warning"

def test_print_promotion():
    result = print_promotion_function.print_promotion('A')
    assert result == "Warning"

def test_print_promotion():
    result = print_promotion_function.print_promotion(-1200)
    assert result == "Warning"

def test_print_promotion():
    result = print_promotion_function.print_promotion(120)
    assert result == "Thank you and see you next time"

 def test_print_promotion():
    result = print_promotion_function.print_promotion(1200)
    assert result == "Free ice cream cone = 1 and Free chocolate cake = 1"

 def test_print_promotion():
    result = print_promotion_function.print_promotion(6844)
    assert result == "Free ice cream cone = 2.0 and Free chocolate cake = 3.0"
