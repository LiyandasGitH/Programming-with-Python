import pytest

from convert import convert


def test_int_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000


def test_error():
    with pytest.raises(TypeError):
        convert("1")


def test_float_conversion():
    # testing tolerance allowance
#    assert convert(0.001) == pytest.approx(149597870.691)
    # abs - plus or minus
#    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1)
    # 1e-5 (1*10 -1/5 or -1/4 or -1/3 or -1/2) -1/2 passes
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)
    # first set a strict tolerance, make sure code corresponds
    # don't adjust tolerance
