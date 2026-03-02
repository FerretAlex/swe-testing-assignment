import calc_logic as cl

def test_main_functionality():
    assert cl.addition(5, 8) == 13
    assert cl.subtraction(5, 8) == -3
    assert cl.multiplication(5, 8) == 40
    assert cl.division(50, 10) == 5
