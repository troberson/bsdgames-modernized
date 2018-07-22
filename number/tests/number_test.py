import pytest
import bsdnumber.converter

# ERROR: invalid format
def test_error_invalid():
	with pytest.raises(TypeError):
		bsdnumber.converter.number_to_string("42x")

# "zero" is only used for 0
def test_zero():
	assert bsdnumber.converter.number_to_string(0) == "zero"

# from the one-part list (1-19)
def test_one_part():
	assert bsdnumber.converter.number_to_string(19) == "nineteen"

# from the two-part list (20-99) with no remainder
def test_two_parts_even():
	assert bsdnumber.converter.number_to_string(20) == "twenty"

# two-part number with ones digit
def test_two_parts_both():
	assert bsdnumber.converter.number_to_string(25) == "twenty-five"

# three-part number (100-999), even
def test_three_parts_even():
	assert bsdnumber.converter.number_to_string(100) == "one hundred"

# three-part number, first and last
def test_three_parts_last():
	assert bsdnumber.converter.number_to_string(108) == "one hundred eight"

# three-part number, all digits
def test_three_parts_all():
	assert bsdnumber.converter.number_to_string(153) == "one hundred fifty-three"

# negative number
def test_negative():
	assert bsdnumber.converter.number_to_string(-420) == "minus four hundred twenty"

# string
def test_string():
	assert bsdnumber.converter.number_to_string("-72") == "minus seventy-two"

# large number
def test_large_number_even():
	assert bsdnumber.converter.number_to_string("1000000000") == "one billion"

# large number with all digits
def test_large_number():
	assert bsdnumber.converter.number_to_string("1234567890") == "one billion two hundred thirty-four million five hundred sixty-seven thousand eight hundred ninety"
