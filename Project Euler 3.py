# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
from math import sqrt

x = 600851475143
largestFac = 0
isPrime = True

for i in range(2, round(sqrt(x))):
    if x % i == 0:
        for k in range(2, i):
            if i % k == 0:
                isPrime = False
                break
        if isPrime:
            largestFac = i
            isPrime = True

print('The largest prime factor of %i is: %i' % (x, largestFac))
