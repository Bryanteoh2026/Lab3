import lab2.Lab2 as Lab2

def find_min_max():
    float_list = [5.0, 67.0, 32.0]
    result = Lab2.calc_min_max_temp(float_list)
    assert result == 1
 
def find_average():
    float_list = [5.0, 67.0, 32.0]
    result = Lab2.calc_average_temp(float_list)
    assert result == -1
 
def find_median():
    float_list = [5.0, 67.0, 32.0]
    result = Lab2.calc_median_temp(float_list)
    assert result == 0