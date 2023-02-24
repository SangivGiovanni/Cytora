from cytora import evaluate
import test_data
import pytest


def test_evaluate_RULE_1():
    rule = test_data.RULE_1
    data = test_data.EXAMPLE_1
    assert evaluate(rule, data) == True

    rule = test_data.RULE_1
    data = test_data.EXAMPLE_6
    assert evaluate(rule, data) == False


def test_evaluate_RULE_2():
    rule = test_data.RULE_2
    data = test_data.EXAMPLE_7
    assert evaluate(rule, data) == False

    rule = test_data.RULE_2
    data = test_data.EXAMPLE_8
    assert evaluate(rule, data) == True


def test_evaluate_raise_error():
    with pytest.raises(ValueError, match="Invalid input_data"):
        rule = test_data.RULE_1
        data = test_data.EXAMPLE_3
        evaluate(rule, data)
    
    with pytest.raises(ValueError, match="Invalid rule"):
        rule = test_data.RULE_3
        data = test_data.EXAMPLE_1
        evaluate(rule, data)
