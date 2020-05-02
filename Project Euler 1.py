# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000

listOfNumbers = [k for k in range(1, 1000)]
listOfMultiples = []

for i in listOfNumbers:
    if i % 3 == 0 or i % 5 == 0:
        listOfMultiples.append(i)

print('The sum of your multiples is: %i' % sum(listOfMultiples))
