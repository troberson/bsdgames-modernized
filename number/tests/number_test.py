import bsdnumber.converter

def test_zero():
	assert bsdnumber.converter.number_to_string(0) == "zero"

def test_one():
	assert bsdnumber.converter.number_to_string(1) == "one"
