# CYTORA TECH TASK

## QuickStart
1) Clone the repo
2) Install python + pytest on your environment
3) Run cytora.py on your IDE or terminal with a print statement and your chosen rule/ data (see details on function arguments) or...
4) Run pytest test.py on your terminal to see the output of these tests
5) test data can be found and changed as you like in test_data.py

## Assumptions
1) rules represented like this:
```
Either:
  credit_rating is above 50
  AND
  flood_risk is below 10
OR
  revenue is above 1000000
```
are pre-translated into this:
```
RULE_1 = {
    "operator": "OR",
    "operands": [
        {
            "operator": "AND",
            "operands": [
                {"operator": ">", "variable": "credit_rating", "value": 50},
                {"operator": "<", "variable": "flood_risk", "value": 10}
            ]
        },
        {"operator": ">", "variable": "revenue", "value": 1000000}
    ]
}
```
before execution (see details below on function).
2) Users will give mostly sensible input_data, exceptions for types existing but things like missing keys or mismatching varibale are not caught - would add this given more time.
3) Scope of testing is very low - would test more scenarios, rules, bad data etc given more time.

## Whats going on?
### evaluate()
The evaluate function provides a way to evaluate complex rules against input data using recursion and logical operators.
The evaluate function takes in two arguments: a rule dictionary and an input_data dictionary. It evaluates the rule against the input_data and returns a boolean value indicating whether the rule is satisfied or not.

### Parameters
rule (dict): A dictionary representing the rule to be evaluated. The dictionary must contain an "operator" key with a valid operator string ("AND", "OR", "NOT", ">", "<", ">=", "<=", "==", "!=") and an "operands" key with a list of sub-rules or sub-conditions. If the operator is one of the comparison operators (">", "<", ">=", "<=", "==", "!="), the dictionary must also contain a "variable" key with a string representing the variable name to be compared and a "value" key with the value to be compared against.

input_data (dict): A dictionary representing the input data to be evaluated against the rule. The keys of the dictionary must correspond to the variable names used in the rule.

### Returns
bool: A boolean value indicating whether the rule is satisfied or not.
Exceptions:
ValueError: If the rule argument or the input_data argument is not a dictionary, or if an invalid operator is used.

Example usage:
```rule = {
    "operator": "OR",
    "operands": [
        {
            "operator": "AND",
            "operands": [
                {"operator": ">", "variable": "credit_rating", "value": 50},
                {"operator": "<", "variable": "flood_risk", "value": 10}
            ]
        },
        {"operator": ">", "variable": "revenue", "value": 1000000}
    ]
}

input_data = {"credit_rating": 75, "flood_risk": 5, "revenue": 2000000}

result = evaluate(rule, input_data)

print(result) # Output: True```

