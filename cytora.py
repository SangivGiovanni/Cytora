def evaluate(rule: dict, input_data: dict):
    if not isinstance(input_data, dict):
        raise ValueError("Invalid input_data type: {}".format(type(input_data)))
    if not isinstance(rule, dict):
        raise ValueError("Invalid rule type: {}".format(type(rule)))
    else:
        if rule.get("operator") == "AND":
            return all(evaluate(op, input_data) for op in rule["operands"])
        elif rule.get("operator") == "OR":
            return any(evaluate(op, input_data) for op in rule["operands"])
        elif rule.get("operator") == "NOT":
            return not evaluate(rule["operands"][0], input_data)
        else:
            data_value = input_data.get(rule["variable"])
            rule_value = rule["value"]
            if rule["operator"] == ">":
                return data_value > rule_value
            elif rule["operator"] == "<":
                return data_value < rule_value
            elif rule["operator"] == ">=":
                return data_value >= rule_value
            elif rule["operator"] == "<=":
                return data_value <= rule_value
            elif rule["operator"] == "==":
                return data_value == rule_value
            elif rule["operator"] == "!=":
                return data_value != rule_value
            else:
                raise ValueError("Invalid operator: {}".format(rule["operator"]))
