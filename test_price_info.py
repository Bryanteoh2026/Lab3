import price_info 

def test_total_cost_shopping():

    expected_output = 46.75

    result = price_info.total_cost_shopping()

    assert result == expected_output

def test_cost_of_fruits():

    fruit_name = 'apple'
    quantity = 5
    expected_output = 6.0

    result = price_info.cost_of_fruits(fruit_name, quantity)

    assert result == expected_output