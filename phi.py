def phi(n):

    """ All nummer under n som inte har samma faktorer """

    phies = []

    nFactors = []


    for i in range(2,n+1):
        if n % i == 0:
            nFactors.append(i)

    for i in range(1,n):
        xFactors = []

        for factors in range(2,i+1):
            if i % factors == 0:
                xFactors.append(factors)

        commonElems = set(nFactors).intersection(xFactors)

        # print("Round", i)
        # print(commonElems)
        # print(nFactors)
        # print(xFactors)
        # print("")

        if len(commonElems) < 1:
            phies.append(i)


    return len(phies)


def gcd(a, b):

    """Returns the greatest common divisor of a and b."""

    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b)


def lcm(a, b):

    return (a * b) / gcd(a, b)
