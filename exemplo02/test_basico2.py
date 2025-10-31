def eh_positivo(n):
    return n>0
def test_eh_positivo():
    assert eh_positivo(5) == 1
    assert eh_positivo(-8) == 0