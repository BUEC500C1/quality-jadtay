from numconverter import arabictoroman

def test_arabictoroman():
    assert arabictoroman(5) == "V"
    assert arabictoroman(4) == "IV"
    assert arabictoroman(3999) == "MMMCMXCIX"
    assert arabictoroman(148) == "CXLVIII"