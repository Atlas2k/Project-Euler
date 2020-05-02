# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
newNum = 0

for i in range(350, 1000):
    for k in range(350, 1000):
        test = i * k
        testStr = str(test)
        if testStr[0] == testStr[-1] and testStr[1] == testStr[-2] \
           and testStr[2] == testStr[-3] and newNum < test:
            firstMulti = i
            secondMulti = k
            newNum = test

print('%i * %i = %i' % (firstMulti, secondMulti, newNum))
