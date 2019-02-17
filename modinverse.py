def modinv(a, b, x):

    """ Gets the modular inverse """

    if (a * x) % b == 1:

        return x

    else:
        return modinv(a, b, x + 1)
