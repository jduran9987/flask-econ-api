from app import get_econ

def test_get_econ():
    assert get_econ("2019") == [{"debt": 22.719, "gdp": 19.092, "year": "2019"}]