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

	if i == 0:
		result = "zero"

	if i > 0 and i < 20:
		result = NAME1[i]

	if i >= 20 and i < 100:
		i_int = int(math.floor(i))
		(q,r) = divmod (i_int, 10)
		result_parts.append(NAME2[q])

		if r > 0:
			result_parts.append(NAME1[r])

		result = "-".join(result_parts)
	
	return result

if __name__ == "__main__":
	import sys
	print (number_to_string(float(sys.argv[1])))
