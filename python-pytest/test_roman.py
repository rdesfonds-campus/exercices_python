from roman import to_roman

def test_1_donne_I():
    # On veut que 1 soit converti en 'I'
    resultat = to_roman(1)
    assert resultat == "I"

def test_5_donne_V():
    # On veut que 5 soit converti en 'V'
    resultat = to_roman(5)
    assert resultat == "V"

def test_10_donne_X():
        # On veut que 10 soit converti en 'X'
        resultat = to_roman(10)
        assert resultat == "X"
def test_10_donne_L():
    # On veut que 50 soit converti en 'L'
    resultat = to_roman(50)
    assert resultat == "L"

def test_100_donne_C():
    # On veut que 100 soit converti en 'C'
    resultat = to_roman(100)
    assert resultat == "C"

def test_500_donne_D():
        # On veut que 500 soit converti en 'D'
        resultat = to_roman(500)
        assert resultat == "D"


def test_1000_donne_M():
    # On veut que 1000 soit converti en 'M'
    resultat = to_roman(1000)
    assert resultat == "M"

    def test_2_donne_II():
        resultat = to_roman(2)
        assert resultat == "II"

    def test_4_donne_IV():
        resultat = to_roman(4)
        assert resultat == "IV"

    def test_9_donne_IX():
        resultat = to_roman(9)
        assert resultat == "IX"

    def test_14_donne_XIV():
        resultat = to_roman(14)
        assert resultat == "XIV"