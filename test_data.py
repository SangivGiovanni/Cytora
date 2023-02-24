"----------EXAMPLES----------"

EXAMPLE_1 = {"credit_rating": 75, "flood_risk": 5, "revenue": 1000}
EXAMPLE_2 = {"something": 75, "flood_risk": 5, "revenue": 1000}
EXAMPLE_3 = True
EXAMPLE_4 = {"credit_rating": 75, "flood_risk": 5, "revenue": "1000"}
EXAMPLE_5 = {}
EXAMPLE_6 = {"credit_rating": 75, "flood_risk": 15, "revenue": 1000}
EXAMPLE_7 = {"credit_rating": 75, "flood_risk": 15, "revenue": 1000, "profit": 501}
EXAMPLE_8 = {"credit_rating": 75, "flood_risk": 15, "revenue": 1000000, "profit": 500}


"----------RULES----------"

"""Either:
  credit_rating is above 50
  AND
  flood_risk is below 10
OR
  revenue is above 1000000"""

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


"""Both:
  credit_rating is above 50
  OR
  flood_risk is below 10
AND
  revenue is above 1000000
  or profit is 500"""

RULE_2 = {
    "operator": "AND",
    "operands": [
        {
            "operator": "OR",
            "operands": [
                {"operator": ">", "variable": "credit_rating", "value": 50},
                {"operator": "<", "variable": "flood_risk", "value": 10}
            ]
        },
        {
            "operator": "OR",
            "operands": [
                {"operator": ">", "variable": "revenue", "value": 1000000},
                {"operator": "==", "variable": "profit", "value": 500}
            ]
        }
    ]
}

"invalid rule type"
RULE_3 = 3
