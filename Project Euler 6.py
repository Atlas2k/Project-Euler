# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

naturalNumbers = [i for i in range(1, 101)]
sumSquare = 0
squareSum = 0

for i in naturalNumbers:
    sumSquare += i**2
    squareSum += i

difference = - sumSquare + (squareSum**2)

print('The difference of the sums is: %i' % difference)
