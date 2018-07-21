import bsdnumber.converter

# "zero" is only used for 0
def test_zero():
	assert bsdnumber.converter.number_to_string(0) == "zero"

# from the one-part list
def test_nineteen():
	assert bsdnumber.converter.number_to_string(19) == "nineteen"

# from the two-part list with no remainder
def test_twenty():
	assert bsdnumber.converter.number_to_string(20) == "twenty"

# two-part number
def test_twenty_five():
	assert bsdnumber.converter.number_to_string(25) == "twenty-five"
