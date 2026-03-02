import calc_logic as cl

def test_edge_cases():
    assert cl.division(5, 0) == "Error"
    assert cl.multiplication(10.546, 7.456) == 78.630976