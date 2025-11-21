from checker import strength, breached

def test_strength():
    assert strength("Aa1!") == 100
    assert strength("abc") < 50

def test_breached():
    breach_list = ["password", "123456"]
    assert breached("password", breach_list) is True
    assert breached("securePass123!", breach_list) is False
