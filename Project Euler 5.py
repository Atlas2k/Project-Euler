# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

i = 1
k = 0
divisors = [k for k in range(1, 21)]
while True:
    test = i % divisors[k]
    if test == 0:
        k += 1
    else:
        i += 1
        k = 0
    if k == 19:
        break

print('The smallest possible number is: %i' % i)
