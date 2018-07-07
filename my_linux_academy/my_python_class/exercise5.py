#!/usr/bin/env python
import math
import os
digits = os.getenv("DIGITS") or "10"
my_float = math.pi
digits =int(digits)
print("%.*f" % (digits, my_float))
#else:
# print("%.*f" % (10, my_float))
