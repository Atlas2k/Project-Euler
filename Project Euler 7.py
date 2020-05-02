# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10 001st prime number?

i = 1
k = 3
notPrime = True

while True:
    for n in range(2, k):
        if k % n == 0:
            notPrime = True
            break
        else:
            notPrime = False
    if not notPrime:
        i += 1
        if i == 10001:
            break
    k += 1

print('The 10,001st prime number is: %i' % k)
