"""
We are going to write some programs using random numbers
"""

import random

print(random.randint(5, 20))
# The number I see is 16.
# The smallest number you could have seen is 5, and the biggest number you could have seen is 20.

print(random.randrange(3, 10, 2))
# The number I see is 7.
# The smallest number you could have seen is 3, and the biggest number you could have seen is 9.
# Line 2 can not produce 4.

print(random.uniform(2.5, 5.5))
# The number I see is 3.3584827237331405.
# The smallest number you could have seen is 2.5, and the biggest number you could have seen is 5.5.
print(random.randint(0, 100))
