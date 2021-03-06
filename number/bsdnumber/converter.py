# BsdNumber - Convert Arabic numerals to English (based on bsdgames/number)
# Tamara Roberson <tamara.roberson@gmail.com>
# Copyright (c) 2018 Tamara Roberson

### The Original Copyright and License follows:

# Copyright (c) 1988, 1993, 1994
# 	The Regents of the University of California.  All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the University nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

MAXNUM = 65 # Biggest number we handle.

NAME1 = [ "", "one", "two", "three", "four", "five", "six", "seven", "eight",
	"nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
	"sixteen", "seventeen", "eighteen", "nineteen" ]

NAME2 = [ "", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
	"eighty", "ninety" ]

NAME3 = [ "hundred", "thousand", "million", "billion", "trillion",
	"quadrillion", "quintillion", "sextillion", "septillion", "octillion",
	"nonillion", "decillion", "undecillion", "duodecillion", "tredecillion",
	"quattuordecillion", "quindecillion", "sexdecillion", "septendecillion",
	"octodecillion", "novemdecillion", "vigintillion" ]

from typing import Union
from decimal import *
import math

def number_to_string(i: Union[int, float, str, Decimal]) -> str:
	result_parts=[]

	# convert to Decimal
	try:
		num = Decimal(i)
	except:
		raise TypeError(f"Invalid Number: {i}")

	# Negative number
	if num < 0:
		result_parts.append("minus")
		num = abs(num)

	# fractions not yet supported
	if _check_fraction(num):
		raise NotImplementedError("Fractions are not yet supported")

	# process small numbers (<1000) easily
	if num < 1000:
		result_parts.append(_process_small_number(int(num)))

	# process large number
	if num >= 1000:
		result_parts.append(_process_large_number(num))

	return " ".join(result_parts)

def _check_fraction(num: Decimal) -> bool:
	return (num // 1 != num)

def _process_small_number(i: int) -> str:
	i_int = abs(int(i))

	if i_int == 0:
		return "zero"

	elif i_int > 0 and i_int < 20:
		return _process_one_part(i_int)

	elif i_int >= 20 and i_int < 100:
		return _process_two_parts(i_int);

	elif i_int >= 100 and i_int < 1000:
		return _process_three_parts(i_int)

	else:
		raise ValueError("Invalid Number: Number must be 0-999. "+
			f"Number was {i_int}.")

def _process_large_number (num: Decimal) -> str:
	result_parts=[]

	# magnitude is the number of digits divided into sets of 3,
	# not incluing the smallest set
	# e.g. 1,200,300,400 = 3
	# 3: "one billion (unit is "billion")
	# 2: "two hundred million (unit is "million")
	# 1: "three hundred thousand (unit is "thousand")
	# 0: "four hundred" (no unit -- "hundred" is processed as small number)
	magnitude = math.floor(math.log10(num)) // 3

	while magnitude >= 0:
		partial_number = num // (10**(3*magnitude)) % 1000
		unit = NAME3[magnitude] if magnitude > 0 else ""
		magnitude -= 1

		if partial_number == 0:
			continue

		partial_number_str = _process_small_number (partial_number)
		result_parts.append(partial_number_str)

		if unit:
			result_parts.append(unit)

	return " ".join(result_parts)

def _process_one_part(i_int: int) -> str:
	i_int = abs(i_int)

	if i_int == 0: # don't need anything
		return ""

	if i_int > 19: # Number too large
		raise ValueError("Invalid Number: Number must be 0-19. " +
			f"Number was {i_int}")

	return NAME1[i_int]

# Two digits of a number set (e.g. 42 -> forty-two)
def _process_two_parts(i_int: int) -> str:
	i_int = abs(i_int)

	if i_int == 0: # don't need anything
		return ""

	if i_int < 20: # only need one part
		return _process_one_part(i_int)

	if i_int > 99: # Number too large
		raise ValueError("Invalid Number: Number must be 0-99. " +
			f"Number was {i_int}")

	result_parts=[]
	(q,r) = divmod (i_int, 10)
	result_parts.append(NAME2[q])

	if r > 0:
		result_parts.append(_process_one_part(r))

	return "-".join(result_parts)

# Three parts of a number set (e.g. 423 = "four hundred twenty-three")
def _process_three_parts(i_int: int) -> str:
	i_int = abs(i_int)

	if i_int == 0: # don't need anything
		return ""

	if i_int < 20: # only need one part
		return _process_one_part(i_int)

	if i_int > 999: # Number too large
		raise ValueError("Invalid Number: Number must be 0-999. " +
			f"Number was {i_int}")

	i_str = str(i_int)

	first_digit = int(i_str[0])
	n_str = _process_one_part(first_digit) + " hundred"

	if (i_int % 100) == 0:
		return n_str

	result_parts=[]
	result_parts.append(n_str)
	result_parts.append(_process_two_parts(i_int % 100))

	return " ".join(result_parts)

if __name__ == "__main__":
	import sys
	print (number_to_string(sys.argv[1]))
