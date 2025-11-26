from arit import somma
import pytest
@pytest.mark.parametrize("a,b,res",[
    (1,2,3)
    ("a","b","ab")
])
@pytest.fixture
def lista():
    return [1,2,3]
def test_somma(a,b,ris):
    assert somma(a,b) == ris
