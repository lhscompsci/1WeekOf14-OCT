#  Starting off
print(22 / 7)
print(355 / 113)
import math

print(9801 / (2206 * math.sqrt(2)))


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# Experiment with the loop above alongside the actual value of Pi.  How many
# sides does it take to make the two close?

# Accumulators

acc = 0
for x in range(1, 6):
    acc = acc + x

print(acc)

# Compute the sum of the first 100 even numbers
# Compute the sum of the first 50 odd numbers
# Compute the average of the first 100 odd numbers
# Write a function that returns the average of the first N numbers, where
#   N is a parameter
# Write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter
# Each number in the Fibonacci sequence is the sum of the previous two numbers.
#   The first two numbers in the sequence are 1 and 1.  Compute the 10th
#   Fibonacci number.
# Write a function to compute the Nth Fibonacci number, where N is a parameter.
#   You may assume that N will be greater than or equal to 3.


# A Monte Carlo Simulation

import random

print(random.random())

# Boolean expressions
# >  greater than
# >= greater than or equal to
# <  less than
# <= less than or equal to
# == the same as [ equal to ]
# != NOT equal to

dogWeight = 25
print(dogWeight != 25)
catWeight = 15

# compound Boolean operators
# and
# or
# not

print(not catWeight < 20)


# Decision Making -- Selection statements
a = 5
b = 10
c = 75

if a <= b:
    c = 45

print(c)

if a > b:
    c = 45
    if b > c:
        a = 25
    else:
        a = -25
else:
    c = 1050
    if b == a:
        c = 25


print(a, b, c)
