#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#


def kangaroo(x1, v1, x2, v2):
    # Write your code here
    output = "NO"
    # x1 < x2
    while x1 < x2 and v1 > v2:
        x1 += v1
        x2 += v2

        if x1 == x2:
            output = "YES"
    return output


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # x1 = int(first_multiple_input[0])

    # v1 = int(first_multiple_input[1])

    # x2 = int(first_multiple_input[2])

    # v2 = int(first_multiple_input[3])

    # result = kangaroo(x1, v1, x2, v2)
    result = kangaroo(0, 2, 5, 3)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
