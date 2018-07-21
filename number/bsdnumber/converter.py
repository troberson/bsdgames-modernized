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

import math

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


def number_to_string(i):
	result_parts=[]
	result=""

	i_int = int(math.floor(i))
	i_int = abs(i_int)

	if i_int == 0:
		result = "zero"

	elif i_int > 0 and i_int < 20:
		result = _process_one_part(i_int)

	elif i_int >= 20 and i_int < 100:
		result = _process_two_parts(i_int);

	elif i_int >= 100 and i_int < 1000:
		result = _process_three_parts(i_int)

	else:
		return None # Error: Invalid Number

	return result

def _process_one_part(i_int):
	i_int = abs(i_int)

	if i_int == 0: # done need anything
		return

	if i_int > (len(NAME1) - 1): # Number too large
		return None # Error

	return NAME1[i_int]

# Two digits of a number set (e.g. 42 -> forty-two)
def _process_two_parts(i_int):
	i_int = abs(i_int)

	if i_int == 0: # don't need anything
		return ""

	if i_int < 20: # only need one part
		return _process_one_part(i_int)

	if i_int > 99: # Number too large
		return None # Error

	result_parts=[]
	(q,r) = divmod (i_int, 10)
	result_parts.append(NAME2[q])

	if r > 0:
		result_parts.append(_process_one_part(r))

	return "-".join(result_parts)

# Three parts of a number set (e.g. 423 = "four hundred twenty-three")
def _process_three_parts(i_int):
	i_int = abs(i_int)

	if i_int == 0: # don't need anything
		return ""

	if i_int < 20: # only need one part
		return _process_one_part(i_int)

	if i_int > 999: # Number too large
		return None # Error

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
	print (number_to_string(float(sys.argv[1])))
