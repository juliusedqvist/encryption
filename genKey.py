from phi import lcm, phi
from modinverse import *


def findD(p1, p2, e):

    """ Formula to get D """

    f = p1 * p2
    n = int(lcm((phi(p1)), (phi(p2))))
    d = modinv(e, n, 0)
    generateKey(f, e, d)


def generateKey(n, e, d):

    """ Generates the encryption publicKey """

    publicKey = open('publicKey', 'w')

    publicKey.write(str(e) + "\n")
    publicKey.write(str(n))

    publicKey.close()

    privateKey = open('privateKey', "w")

    privateKey.write(str(d) + "\n")
    privateKey.write(str(n))

    privateKey.close()


def main():

    keyParam = [int(input('INPUT: FACTOR1 ')), int(input('INPUT: FACTOR2 ')), int(input('INPUT e '))]

    if lcm(phi(keyParam[0]), phi(keyParam[1])) % keyParam[2] != 0:
        findD(keyParam[0],keyParam[1],keyParam[2])
    else:
        print("e must be a coprime to ", int(lcm(phi(keyParam[0]), phi(keyParam[1]))))
        main()

main()

