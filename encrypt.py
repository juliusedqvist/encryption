def encrypt(message):

    """ Function that encrypts the message"""

    key = open('publicKey', 'r')

    file = open('message', 'a')

    file.write(str((message ** int(key.readline())) % int(key.readline())) + " ")

    file.close()

    key.close()


def clearMes():

    """ Clears the message file """

    file = open('message', 'w')

    file.write("")

    file.close()
