import lab2.Lab2 as lab2 

def test_min_max():
    float_list = [1, 2, 3, 4, 5]

    result = lab2.calc_min_max_temp(float_list)

    assert result == 1

def test_cal_ave():
    float_list = [1, 2, 3, 4, 5]

    result = lab2.calc_average_temp(float_list)

    assert result == -1

def test_cal_median_temp():
    float_list = [1, 2, 3, 4, 5]

    result = lab2.calc_median_temp(float_list)

    assert result == 0
