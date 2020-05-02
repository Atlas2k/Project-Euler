# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def findProduct():
    for c in range(3, 1000):
        for a in range(1, 1000):
            for b in range(a + 1, 1000):
                if a**2 + b**2 == c**2:
                    if a + b + c == 1000:
                        triplets = '%i**2 + %i**2 = %i**2' % (a, b, c)
                        value = a * b * c
                        return triplets, value


print('The product of the triplet (%s) is: %i' % (findProduct()))
