import lab2.bmi as bmi 

def test_bmi_normal_weight():
    height = 1.75
    weight = 65

    result = bmi.calculate_bmi(height, weight)

    assert result == 0
    print("Test passed: BMI is normal weight.")

def test_bmi_over_weight():
    height = 1.75
    weight = 80

    result = bmi.calculate_bmi(height, weight)

    assert result == 1
    print("Test passed: BMI is over weight.")

def test_bmi_under_weight():
    height = 1.75
    weight = 50

    result = bmi.calculate_bmi(height, weight)

    assert result == -1
    print("Test passed: BMI is under weight.")